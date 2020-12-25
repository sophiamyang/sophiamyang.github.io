# Deep learning basics — batch normalization

## What is batch normalization?

Batch normalization normalizes the activations of the network between layers in batches so that the batches have a mean of 0 and a variance of 1. The batch normalization is normally written as follows:

![](batch_normalization.png)
*[source](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html)*


"The mean and standard-deviation are calculated per-dimension over the mini-batches and γ and β are learnable parameter vectors of size C (where C is the input size). By default, the elements of γ are set to 1 and the elements of β are set to 0.(https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html)"

The mean and standard deviation are calculated for each batch and for each dimension/channel. γ and β are learnable parameters which can be used to scale and shift the normalized value, so that we can control the shape of the data when going into the next layer (e.g., control the percentage of positive and negative values going into a ReLU).

Ideally we would do this activation normalization for the entire dataset, however, it is often not possible due to the large size of the data. Thus, we try do to the normalization for each batch. Note that we prefer to have large batch sizes. If the batch size is too small, the mean and standard deviation would be very sensitive to outliers. If our batch sizes are large enough, the mean and standard deviations would be more stable.

## Why do we need batch normalization?
- Reduce the internal covariate shift, which is the “change in the distribution of network activations due to the change in network parameters during training” (Ioffe & Szegedy, 2015).
- Faster training. Because batch normalization reduces the internal covariate shift and fix the distribution of network activations, the network can use larger learning rates and the network can be trained faster.
- Regularizes the network.

## How do we implement batch normalization?
### Training
In the training stage, we can simply add `torch.nn.BatchNorm2d` between two layers in the network. There is also `torch.nn.BatchNorm1d` and `torch.nn.BatchNorm3d` depending on your data dimensions.

`torch.nn.BatchNorm2d` can be before or after the Convolutional layer. And the parameter of `torch.nn.BatchNorm2d` is the number of dimensions/channels that output from the last layer and come in to the batch norm layer.

```
torch.nn.Sequential(
torch.nn.Conv2d(n_input, n_output, kernel_size=3, padding=1, stride=stride, bias=False),
torch.nn.BatchNorm2d(n_output),
torch.nn.ReLU(),
torch.nn.Conv2d(n_output, n_output, kernel_size=3, padding=1, bias=False),
torch.nn.BatchNorm2d(n_output),
torch.nn.ReLU()
)
```

### Testing
At the testing stage, we don’t train the data and we can’t calculate the mean and standard deviation for the batches like we do for the training data. Instead, we use the running average estimate of the mean and standard deviation that we got from the training data. We use those estimates to approximate the mean and standard deviation for the entire data.

When we train the data, we use the training mode using model.train(). And when we are ready to evaluate the model and test the model on the test data, we need to switch to the testing mode by callingmodel.eval(). Then the running average mean and standard deviation will be used directly to evaluate the model.

Reference:  
https://arxiv.org/abs/1502.03167  
https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html 

By Sophia Yang on [September 2, 2020](https://medium.com/analytics-vidhya/deep-learning-basics-batch-normalization-ae105f9f537e).