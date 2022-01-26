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
# # <center> <font color=darkgreen>Comprehensions</font>  </center>
# ---
#
# + Comprehensions are a succinct way of creating iterables from other iterables.
# + iterable A -> filter -> map -> iterable B
#
# ## List comprehensions
#
# It is commonplace to have to apply a function the a selection of elements in a list (or set or dictionary). 
#
# **Example** Find the squares of odd numbers between 0 and 9.

# %%
S = []
for i in [0,1,2,3,4,5,6,7,8,9]:
    if i%2==0:
        S.append(i**2)
print(S)

# %% [markdown]
# This is a filter-then-map operation on `[0,1,2,3,4,5,6,7,8,9]`
#
# A **list comprehension** is a succinct (and computationally efficient) was of doing that:

# %%
S = [i**2 for i in [0,1,2,3,4,5,6,7,8,9] if i%2==0]
print(S)

# %% [markdown]
# **Syntax** `[<single line of code> for <var> in <iterable or range> if <conditional>]`

# %% [markdown]
# ## [`range()`](https://docs.python.org/3/library/functions.html#func-range) 
#
# Produces lists of integers. 
#

# %%
S = [i**2 for i in range(10) if i%2==0]

# %% [markdown]
# `range` also accepts a "step" parameter. 

# %%
S = [i**2 for i in range(0,10,3) if i%2==0]
print(S)

# %% [markdown]
# The three parameters of `range(start,end,step)` follow the same rules as for a *slice* `start:end:step`.

# %% [markdown]
# ## Set comprehensions
#
# + Replace the `[]` with `{}`
# + Removes duplicates.
#
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center> 
#
# Use a comprehension to count the number of distinct words in this song:
#
# The foot bone's connected to the leg bone.  <br />
# The leg bone's connected to the knee bone. <br />
# The knee bone's connected to the thigh bone. <br />
# Doin' the skeleton dance.
#
# ---

# %%
song = "The foot bone's connected to the leg bone. " \
"The leg bone's connected to the knee bone. " \
"The knee bone's connected to the thigh bone. " \
"Doin' the skeleton dance."

words = {len(i) for i in song.split(' ')} 

print(words)

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center> 
# ---
#
# Use a comprehension to find the words in this sentence with less than 5 letters.

# %%
sentence = "Use a comprehension to collect the non-numerical words " \
            "in this sentence that have less than 5 letters."

print([word for word in sentence.split(" ") if len(word)<5 and word.isalpha()])

# %%
