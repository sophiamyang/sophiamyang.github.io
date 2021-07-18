# How to host Jupyter Notebook slides on Github
*Minimal effort to make slides and host an html file on Github*

Checkout the slideshow of this article here: https://sophiamyang.github.io/slides_github_pages/.

There are two parts to this article:

1. How to turn your Jupyter Notebooks into a slideshow and output to an html file.
2. How to host an html file on Github.

## Jupyter Notebook slides
First, let's create a new enviornment slideshow, install a Jupyter notebook extension RISE, and launch Jupyter Notebook:

```
conda create -n slideshow -c conda-forge python=3.9 rise
conda activate slideshow
jupyter notebook
```

Then create a Jupyter Notebook file as usual:
- Click View-Toolbar-Slideshow to define the slide type for each cell.
- RISE creates a button “Enter/Exit Live Reveal Slideshow” in the top right of the toolbar.
- Click this tool bar, you will be able to view your notebook as a slideshow.

## Slides to html
If you have code cells and would like to show all the code cells, use:

```
jupyter nbconvert github_page_example.ipynb --to slides --stdout > index.html
```

If you would like to hide all the code cells:
```
jupyter nbconvert github_page_example.ipynb --no-input --no-prompt --to slides --stdout > index.html
```

If you would like to hide code for certain cells, we can add a tag for those code cells via View - Cell Toolbar - Tags. Here I use the tag "remove_input".
```
jupyter nbconvert github_page_example.ipynb --TagRemovePreprocessor.remove_input_tags "remove_input" --to slides --stdout > index.html
```

## Host html file on Github
To publish an html file on Github Pages, we need to push to gh-pages branch.

Create new git repo locally with gh-pages branch:
```
git init
git checkout -b gh-pages
git add index.html
git commit
```

Go to Github and create a new empty repo, and then push our files to the gh-pages branch.
```
git remote add origin git@github.com:YOUR_USER_NAME/YOUR_REPO_NAME.git
git branch -M gh-pages
git push -u origin gh-pages
```

Now you can see this slideshow hosted on a Github page: https://YOUR_USER_NAME.github.io/YOUR_REPO_NAME

Check mine out: https://sophiamyang.github.io/slides_github_pages/.

## Reference:  
https://rise.readthedocs.io/en/stable/

https://pages.github.com/

By Sophia Yang on July 18, 2021