# Conda environment 101

Conda is an open source package management and environment management tool for Python and other languages. Whenever you use Python, you will be working in a Python environment, which contains the specific Python version you are running on and various Python packages with specific package versions and specifications.

If you use Anaconda or Miniconda, you can easily use Conda to manage your Python environment. To see which environment you are currently on, run:

```
conda env list 
```

It always starts with the base environment, which could be /anaconda3 or /miniconda. For Anaconda users, your base environment will include a bunch of data science packages preinstalled, which is super handy and ready to use. However, it is recommended to always create and use your own environment and don’t use the base environment. I learned this lesson the hard way. If you break your base environment, you won’t be able to remove your base environment and you will have to uninstall and reinstall Anaconda/Miniconda completely. In addition, different projects requires different packages and versions of packages. To avoid such environment conflicts, we can just create different conda environment for different projects by running the following:

```
conda create --name myenv
```

or create an environment with a specific Python version:

```
conda create --name myenv python=3.7
```

Now `conda env list` should list the new environment you just created. To activate this new environment, simply run `conda activate myenv` and to deactivate run `conda deactivate`.
Once you are in your new environment, conda list lists everything installed in your environment. It should be empty now. For my new conda environment, I’d like to start with installing some basic packages I use every day for almost all my projects:
```
conda install jupyter notebook dask distributed fastparquet pandas
```

Then you can install additional packages to meet the needs of each project.

When install packages, try to use `conda install` and avoid `pip install` if possible. Although pip works in conda environment, conda works better for conda packages. If a package you are looking for is not in the conda default channel, please checkout the conda-forge channel to see if the package is available there. To install a package (e.g., qscintilla2) from conda-forge, run `conda install -c conda-forge qscintilla2`. pip has its own way of managing packages, and sometimes it can create conflicts with conda.

The most amazing thing about Conda environment is that conda let you rollback to your previous Conda environments!
```
conda list --revisions
```

Running this will give you a list of all your revision histories. If you would like to go back to revision 10, run
```
conda install --revision 10
```

Then your previous environment will be magically restored.
Finally, there are a lot of myths and misconceptions about Conda. Jake VanderPlas wrote this amazing [article](http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/) explained all the myths and misconceptions. Check it out!

References: 

https://conda.io/en/latest/

http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/

By Sophia Yang on [May 8, 2019](https://sophiamyang.medium.com/conda-environment-101-f9fd21299859)