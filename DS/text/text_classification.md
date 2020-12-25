# An overview of text classification
*How to approach a text classification problem*

![](text_classification0.png)
*[source](https://unsplash.com/photos/8EzNkvLQosk)*


Imagine we have a large number of text files and we need to classify these text files into different topics. What should we do? This article will walk you through an overview of text classification and how I would approach this problem on a high-level basis. I would like to address this problem in three steps — data preparation and exploration, labeling, and modeling.

## Data Preparation and Data Exploration
The first step is data preparation and exploration. I will transform our text data into a matrix representation through different word embedding methods. Then, I will perform an N-gram analysis and topic modeling to explore the data in more detail.

### Word Embedding
#### Bag of words
Most text analysis and machine learning models use the bag of words embedding, which tokenizes our text into tokens, normalize tokens, count occurrences, apply weights (optional), filter out stopwords, and create a document-term matrix. Bag of words assumes the independence of the words and does not take into account the sequence of the words. I will use the bag of words approach for my data exploration and machine learning models.

#### Word2vec Embedding
Deep learning models often use the pre-trained word2vec embeddings, which incorporate the information of word similarities. The advantage of word2vec is that it has much fewer dimensions than the bag of words approach, and our document-term matrix will be a dense matrix, and not sparse. I plan to use a word2vec embedding (e.g., word2vec-google-news-300) for my deep learning models.

#### Character Embedding
Some deep learning models use character embedding and build models at the character-level directly [1][2]. Characters can include English characters, digits, special characters, and others. The advantage of character embedding is that it can model with uncommon words and unknown words. I might try character embedding with my deep learning models to compare with the word2vec embedding.

### N-gram analysis
With the bag of words approach, we can investigate the single word (unigram), and combinations of two words and three words (Bigram/Trigram). With N-gram analysis, we can have a descriptive view of which words or word combinations are being used the most.

### Topic modeling
Next is topic modeling. There are two ways to do topic modeling: NMF models and LDA models. Non-Negative Matrix Factorization (NMF) is a matrix decomposition method, which decomposes a matrix into the product of W and H of non-negative elements. The default method optimizes the distance between the original matrix and WH, i.e., the Frobenius norm [3]. Latent Dirichlet Allocation (LDA) is a generative probabilistic model optimizing the posterior distribution of the topic assignment [4].
Both NMF and LDA require users to define the number of topics. How do we know how many topics we should put in the model? We can use a grid search and find the optimal parameters (topics, learning rate, etc.) that can optimize the log-likelihood value [5].

The output is a list of topics and their associated words, which can then be used to predict the topic of each file. However, since it is unsupervised, we cannot validate and iterate the model, and the performance of this prediction is often less than ideal. So instead of using the model to predict file topics, my goal for this step is to come up with a list of topics, so that we can use this list of topics to facilitate labeling.
For the implementations of N-gram analysis and topic modeling, check out [this article](https://sophiamyang.github.io/DS/text/text_basics.html).

## Labeling
Now, we should have a list of topics produced from the topic modeling. We can then label our files to this list of topics.
If we have resources, we can hire third parties to do the labels. Otherwise, we can label the topics ourselves. We can even construct our labeling task as a survey, with dropdown choices from prepopulated topics. We will also include the “Other, please specify” option if none of the topics match with the file.
Topic modeling also predicts the topic for each file. Although it might not be the most accurate, we can still use this information to try choosing a balanced sample of topics to label.

## Modeling
### Machine learning model
We randomly sample our labeled data into training (70%), validation(20%), and testing (10%) datasets (the percentages depend on the sample size). The input of my machine learning model is the bag of words matrix for the text files. For any additional information of text (e.g., file source), we can dummy code this information and concatenate the dummies to our document-term matrix. The output is the labels.

I would like to test four machine learning models and compare their performances on model accuracy and confusion matrix through k-folds cross-validations.
- Multinomial logistic regression
- Multinomial Naive Bayes
- Support vector machine
- XGBoost

Multinomial logistic regression is the most basic and easiest to interpret. However, I suspect multinomial logistic regression would perform the worst. Multinomial Naive Bayes is another popular model for text classification that can give us a benchmark result. Support vector machine and XGBoost should provide us better results. We will need to do some hyperparameter tuning to find the best performing model. From my experience, with various hyperparameters and methods to avoid overfitting, XGBoost usually works the best. For implementation details, check out `sklearn` and `xgboost` documentations.

### Deep learning model
Three types of deep learning models are suited for NLP tasks — recurrent networks (LSTMs and GRUs), convolutional neural networks, and transformers. The recurrent network takes a long time and is harder to train, and not great for text classification tasks. The convolutional neural network is easy and fast to train, can take many layers, and outperform the recurrent network [6][7]. The transformers model is the state of the art method, however, I do not have much experience with transformers. Thus, I will only talk about the convolutional neural network.

The input of the deep learning model is the matrix of the word2vec embedding for each text file. Again, we randomly sample our labeled data into training (70%), validation (20%), and testing (10%) datasets. We can increase the percentage of our training set if our sample size is small.

We will randomly separate training data into different batches. The sample size for each input needs to be the sample for each batch. Thus, we need to find the longest input text and pad all the other input text to match the length of the longest text.

For constructing the deep learning model, we can add multiple layers of convolutional blocks and then feed the results into a softmax layer to get the classification result (see figure 1). Note that with text analysis, we need to make sure that our receptive field is as large as possible so that the network is looking at the entire length of the input text for each document. Thus, we use many layers and dilated convolutions to increase the receptive field. The code below shows an example code of a convolutional block (note that for text generation, we will need to use a causal convolutional block. But for text classification, many-layered dilated convolution will be fine). For each layer, we can increase the number of dilations by a factor of 2. Then we can tune and train the model and apply various techniques to prevent overfitting until we are satisfied with the model performance. And the final step is to predict all file labels with our trained deep learning model.

Now you have a high-level view of text classification. Enjoy!

<script src="https://gist.github.com/sophiamyang/555a87b4ac68e41b7abc17579cb7ea60.js"></script>

![](text_classification.png)
*Figure 1. Illustration of a convolutional network for classification [7].*


References:

[1] http://proceedings.mlr.press/v32/santos14.html

[2] https://arxiv.org/pdf/1508.06615.pdf

[3] https://scikit-learn.org/stable/modules/decomposition.html#nmf

[4] https://scikit-learn.org/stable/modules/decomposition.html#latentdirichletallocation

[5] https://www.machinelearningplus.com/nlp/topic-modeling-python-sklearn-examples/

[6] http://web.stanford.edu/class/cs224n/slides/cs224n-2020-lecture11-convnets.pdf

[7] http://www.philkr.net/dl_class/lectures/sequence_modeling/04.pdf

By Sophia Yang on [November 18, 2020](https://towardsdatascience.com/an-overview-of-text-classification-b1ec14db358c)