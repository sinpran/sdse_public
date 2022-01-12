# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Homework 1, Problem 5

# %%
import matplotlib.pyplot as plt
import numpy as np


# %% [markdown]
# 1) Complete the function below such that it returns the **inverse cummulative exponential distribution** with mean lambda, evaluated at x.

# %%
def inv_cum_exp(x,lbda):
    return np.NaN*x


# %% [markdown]
# 2) Use this function to generate a single plot with
# + the inverse cummulative distribution for 3 values of lambda: {1,5,10}
# + x varying from 0 to 1
# + grid lines
# + a legend.
# + set figsize=(10,5)

# %%

# %% [markdown]
# 3) Write a function that generates `n` samples of an exponential distribution with parameter `lbda` using `inv_cum_exp` and `np.random.rand`, *but not* `np.random.exponential`.

# %%
def sample_exp(n,lbda):
    return np.empty(n)


# %% [markdown]
# 4) Create a histogram with 1000 samples of an exponential distribution with a mean of 10 using `sample_exp`. (again use figsize=(10,5))

# %%

# %% [markdown]
# 5) Write a function that will return the sample mean for a sample of size `n` drawn from an exponential distribution with mean `lbda`.

# %%
def sample_mean(n,lbda):
    return np.NaN

# %% [markdown]
# 6) Write a list comprehension that creates a list of size `m=10` of sample means for samples of size `n=1000` and `lbda=10`

# %%

# %% [markdown]
# Use this list comprehension to create the following 3 histograms (figsize=(10,5)). All with `lbda=10` and `m=1000`: 
# + n=10
# + n=1000
# + n=10000
#
# Pass the parameters `bin=20` to create 20 bins. What theorem does this demonstrate (you don't have to submit the answer to this question). 

# %%
