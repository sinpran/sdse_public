# -*- coding: utf-8 -*-
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
#
# # <center> <font color=darkgreen>Iterables</font>  </center>
#
# ---
#
# <img src="data_types.png" width="500">
#
# ---

# %% [markdown]
# Iterable types in Python contain sets of elements. There are
# + **string** - ordered sequence of characters
# + **set** - sets of unique objects
# + **tuple** - immutable ordered sets of objects
# + **list** - mutable ordered sets of objects
# + **dictionary** - mutable sets of key/value pairs.
#
# We will study each of these, but first we will look at built-in functions that apply to iterables in general.

# %% [markdown]
# ## Checking membership:  `in` and `not in`
#
# `a in A` evaluates to `True` if `a` is an element of the iterable `A`, and `False` otherwise. 
#
# You can also use `a not in A` to get the opposite behavior.
#
# In the following example, `A` is a list.

# %%
A = [ 1/2, 0.4, 'hi', [0,1] ]

print(A)

# %% [markdown]
# ## Unpacking
#
# Unpacking is a shorthand syntax for assigning each of the elements of an iterable to different scalar variables. 

# %%

# %% [markdown]
# **Question**: What do you think happens if the number of variable names does not match the number of elements in the iterable?

# %% [markdown]
# ---
# # <center> <font color=darkgreen> Indexing iterables</font>  </center>
# ---
#
# + Strings, tuples, and lists are **ordered iterables**. 
#
# + Indexing is **0-based** and uses square brackets `[]`.
#
# + Sets and dictionaries are not ordered. Therefore they cannot be indexed.

# %% [markdown]
# **Example** : Index a string

# %%
astring = 'Food is an important part of a balanced diet - Fran Lebowitz'

# %% [markdown]
# **Example** : Index a list

# %%
alist = [4.45, 'hello', 4+5j]

# %% [markdown]
# **Example** : Index a tuple

# %%
atuple = (4.45, 'hello', 4+5j)

# %% [markdown]
# **Lists are mutable, tuples and strings are not**

# %%

# %% [markdown]
# ## Slice indexing
# + You can get a 'slice' of an iterable using the colon symbol `:`
# + This returns a new iterable that is a portion of the original object.
# + `astring[a:b]` is the substring starting at index `a` and ending at `b-1`.

# %%

# %% [markdown]
# + Leaving out the start index means 'from the beginning'
# + Leaving out the end index means 'to the end'

# %%

# %% [markdown]
# ## Negative indices
# Negative indices count backward from the end.

# %%

# %% [markdown]
# ## Skipping values
#
# You can specify a "skip" value after a second colon: `A[start:end:skip]`

# %%
A = [0,1,2,3,4,5,6,7,8,9]

# What will this return?
A[0:-2:3]

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[Strings methods](https://docs.python.org/3/library/stdtypes.html#string-methods)</font>  </center>
# ---
#
# Things we can do with strings,
# + create them,
# + change cases in various ways,
# + search for a substring,
# + split strings,
# + etc.

# %%
strA = 'ABC'
strB = '123'

# %% [markdown]
# ## String `+`

# %%
print(strA + strB)

# %% [markdown]
# ## Formatting strings - [`.format()`](https://docs.python.org/3/library/stdtypes.html#str.format)
#
# The `format()` method is especially useful for building strings that involve numerical or other variables. The function is powerful, and you can find advanced examples [here](https://docs.python.org/3/library/string.html\#format-examples). However the simple form works most of the time. Here is an example.
#
# ### Example: "Johann Sebastian Bach was born in 1685, and died in 1750."

# %%
name = 'Johann Sebastian Bach'
birth_year = 1685
death_year = 1750

# using the 'format' method
str1 = '{0} was born in {1}, and died in {2}.'.format(name, birth_year, death_year)

print(str1)

# "f-string" method
str2 = f'{name} was born in {birth_year}, and died in {death_year}.'

print(str2)

# %% [markdown]
# ### `.split()`

# %%
a = '1,phone,None,-4.5,'
print(a)
b = a.split(',')
print(b)

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center>
# ---
# Use `split` to extract the name of the author in `astring`.

# %%
print(astring)

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Lists: `[]` </font>  </center>
# ---
# A **list** is a sequence of objects that is:
# + **ordered**: They can be indexed with `[]`.
# + **inhomogeneous**: They can contain a variety of object types.
# + **mutable**: You can modify them by adding and/or deleting items after they are created.

# %%

# %% [markdown]
# ## [List methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
#
# The methods attached to list objects provide functionality for adding, removing, and changing the order of the elements in a list. 

# %% [markdown]
# ## Building lists
#
# The `append`, `extend`, and `insert` methods can be used to populate a list. Later we will learn about "list comprehensions" which give us a compact syntax for building large lists (as well as sets and dictionaries).

# %% [markdown]
# ### `.append()` Puts a value at the end of the list.

# %% [markdown]
# ### `.extend()` Appends each value of an iterable to the list.

# %% [markdown]
# ### `.insert` Inserts an element at a given location in the list.

# %% [markdown]
# ## Removing items from lists
#
# ### `.remove()` Remove the first instance of a given object.

# %% [markdown]
# ### `.pop()` Extract the item at a given index and return it.

# %% [markdown]
# ### `del`
# Remove an item at a given index.

# %%
a=[4,1,9]
del a[1]
print(a)

# %% [markdown]
# ### `.clear()` Remove all items from the list.

# %%
a=[4,1,2,1,9]
a.clear()
print(a)

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center> 
# ---
# 1. Create this list: [4,1,9]
# 2. Use list object methods to put it in reverse order: [9,4,1]
#
# **HINT**: `help(a.sort)` and`help(a.reverse)` 

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences): `()`</font>  </center>
# ---
#
# A **tuple** is a sequence of objects that is:
# + **ordered**
# + **inhomogeneous**
# + **mutable**
#
# Tuples offer only 2 methods: `count()` and `index()`.
#
# ### Why use a *tuple* instead of a *list*?
#
# + return values from functions
# + keys in dictionaries

# %%
a = (1,'asdf',4.3)

print(a)

a.index(4.3)

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen>[Sets](https://docs.python.org/3/tutorial/datastructures.html#sets): `{}`</font>  </center>
# ---
#
# A **set** is a sequence of objects that is:
# + **inhomogeneous**
# + **not ordered**
# + **mutable**
# + **contains no duplicates**
#

# %%
a = {4,6,3,3}

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center> 
# ---
#
# Use a `set` to count the number of unique words in the following paragraph.
#
# X = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms. The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation."

# %%
X = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms. The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation."

words = X.split(' ')
unique_words = set(words)

print(len(words))

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries): `{:}`</font>  </center>
# ---
# A **dictionary** is a mapping from a set of *keys* to a set of *values*.
# + The keys in a dictionary must be **immutable** (scalars, strings, tuples). 
# + The values in a dictionary can be **anything**. 
# + Dictionaries are created with **curly brackets** and **colons**: { a1:b1 , a2:b2 }

# %%
JSB = { 'name' : 'Johann Sebastian Bach' ,
        'birth_year' : 1685 ,
        'death_year' : 1750 }

print(JSB)

# %% [markdown]
# ### Querying the dictionary: square brackets

# %%
JSB['name']

# %% [markdown]
# ### Get the set of keys

# %%
type(set(JSB.keys()))

# %% [markdown]
# ### Change a value

# %%
JSB['death_year'] = 2030
print(JSB)

# %% [markdown]
# ### Add a new key-value pair

# %%
