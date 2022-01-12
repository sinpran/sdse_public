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
# ---
# # <center> [The Standard Library](https://docs.python.org/3/tutorial/stdlib.html) </center> 
# + We will introduce three modules from the Standard Library: **math**, **random**, and **statistics**.
# + Read the manual for a method with `help(<module name>.<method name>)`
# + Google everything! (and read the docs!)
# ---

# %% [markdown]
# ---
# # <center> <font color=darkgreen> [math](https://docs.python.org/3/library/math.html#module-math) </font>  </center>
# ---

# %%
import math

dir(math)

# %%
math.isclose( 0.0 , math.cos(math.pi) )

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[random](https://docs.python.org/3/library/random.html#module-random)
# </font>  </center>
#
# ---

# %%
import random 
x = [1,2,3,4,5]

# %% [markdown]
# ### `shuffle(x)` : Shuffle x in place

# %%
random.shuffle(x)
print(x)

# %% [markdown]
# **Question**: Does this work for tuples? sets?

# %% [markdown]
# ### `choice(x)` : Pick an element from x

# %%
random.choice( ('red', 'black', 'green') )

# %% [markdown]
# **Question**: Does this work for tuples? sets?

# %% [markdown]
# ### `sample(x,k)` : Pick k unique elements from x without replacement.

# %%
random.sample( range(500) , 10)

# %% [markdown]
# **Question**: Does this work for tuples? sets?

# %% [markdown]
# ### `randint(a,b)` : Pick a random integer in [a,b]

# %%
random.randint(0, 5)

# %% [markdown]
# ### `random()` : Sample from uniform distribution on [0, 1)

# %%
random.random()

# %% [markdown]
# ### `uniform(a,b)` : Sample from uniform distribution on [a, b)

# %%
random.uniform(0,100)

# %% [markdown]
# ### `gauss(mu,sigma)` : Sample from a Gaussian distribution with mean mu and std. deviation sigma.

# %%
random.gauss(1,0.3)

# %% [markdown]
# ### Note 
# It is often useful (e.g. when debugging) to fix the random number generator seed. To do this use `seed()`.

# %%
random.seed(5)
for i in range(3): 
    print(random.random())

print('-----------')
random.seed(20)
for i in range(3): 
    print(random.random())

print('-----------')

random.seed(5)
for i in range(3): 
    print(random.random())


# %% [markdown]
#
# ---
# # <center> <font color=darkgreen> [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) </font>  </center>
# ---
#
# Different *averaging* functions
#

# %%
import statistics as stats

# %% [markdown]
# ###  [`mean(x)`](https://docs.python.org/3/library/statistics.html#statistics.mean),  [`geometric_mean(x)`](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean),  [`harmonic_mean(x)`](https://docs.python.org/3/library/statistics.html#statistics.harmonic_mean)

# %%
import math

x = [1,3,6,7,8]

print(stats.mean(x))
print(sum(x)/len(x))

print(stats.geometric_mean(x))
print(math.prod(x)**(1/len(x)))

print(stats.harmonic_mean(x))
print(len(x)/sum([1/a for a in x]))

# %% [markdown]
# ### [`median(x)`](https://docs.python.org/3/library/statistics.html#statistics.median) , [`median_low(x)`](https://docs.python.org/3/library/statistics.html#statistics.median_low) , [`median_high(x)`](https://docs.python.org/3/library/statistics.html#statistics.median_high)

# %%
x = [1,3,5,6,7,8]

print(stats.median(x))
print(stats.median_low(x))
print(stats.median_high(x))

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center>
#
# Sample a standard normal distribution (zero mean, unit variance) 300 times, save the result to a list and order it from smallest to largest. 
#
# **HINT**: We have not seen how to sort lists.

# %%
x = sorted([random.gauss(0,1) for i in range(300)])


# %% [markdown]
# ### Follow-up questions
# + Did you use `list.sort()` or `sorted(list)`?
# + What is the difference?
