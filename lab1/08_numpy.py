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
# # <center><font color=purple>[Numpy](https://numpy.org/)</font> </center>
# ---
#
# + NumPy is a package for performing computations with **numerical lists**. 
# + Many scientific computing libraries are built on NumPy.
#     + SciPy
#     + pandas
#     + scikit-learn
#     + python-control
# + [Tutorial](https://numpy.org/devdocs/user/quickstart.html)
#
# ## Standard import statement

# %%
import numpy as np

# %% [markdown]
# ## NumPy arrays
#
# The main type in NumPy is the the "numpy array" or **ndarray** (for n-dimensional array).
#
# Create an ndarray with `np.array()`:

# %%
x = np.array([1,2,1])

print(x)

# %% [markdown]
# A NumPy array is
# + Multi-dimensional (arrays of arrays)
# + Homogeneous (all elements are of the same type)
# + Numerical (integers, floats, or complex)
#
# ## Why prefer NumPy over native lists?
#
# 1. Specialized functionality.
# 2. Tuned for speed.
#
# | NumPy arrays | Lists |
# | --- | --- |
# | low level types | Objects |
# | homogeneous | multiple types |
# | contiguous memory | scattered |

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen> [Creating arrays](https://numpy.org/doc/stable/reference/routines.array-creation.html) </font> </center>
# ---
#
#
# # 1-D arrays
#
# ### [`np.array(x)`](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

# %%

# %% [markdown]
# ### [`empty(shape)`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty) [`zeros(shape)`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros) [`ones(shape)`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones)

# %%

# %% [markdown]
# ### [`linspace(start,stop,num)`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace)

# %%

# %% [markdown]
# # 2-D arrays

# %%
b = np.array([[1.5,2,4], [4,5,6]])
print(b)

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen> [Manipulating arrays](https://numpy.org/doc/stable/reference/routines.array-manipulation.html) </font> </center>
# ---

# %% [markdown]
# ### [`append(x,values)`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append):  Append `values` to the end of `x`.

# %%
x = np.array([1,2,3,4])

np.append(x,[100,200])

# %% [markdown]
# ### [`insert(x,ind,values)`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert): Insert `values` into `x` at `ind`

# %%
x = np.array([1,2,3,4])

np.insert(x,2,[100,200])

# %% [markdown]
# ### [`concatenate((x1,x2,...))`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate): Concatenate a collection of arrays.

# %%
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
np.concatenate((x1,x2))

# %% [markdown]
# ### [`unique(x)`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique): Find the unique elements in `x`.

# %%
x = np.array([1,2,1,2,4,4,4,4])
print(x)
print(np.unique(x))

# %% [markdown]
# ---
# # <center> <font color=darkgreen> [Indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html) </font> </center>
# ---
#
# ## 1D: `[x]` where `x` is a list of indexes or a slice

# %%
a = np.array([4,7,9,4,9,30,6,20,54])

print(a[3:8:2])

# %% [markdown]
# ## more than 1D: [x,y]   (instead of lists' [x][y])

# %%
b = np.array([(1.5,2,3), (4,5,6)])

print(b)

b[0:1,[0,2] ]

# %% [markdown]
# ## Boolean indexing

# %%
print(a)

print(a[a>7])

# %% [markdown]
# ---
# # <center> <font color=darkgreen> Iteration </font> </center>
# ---
#
# Just like native Python iterables.

# %%
for x in b:
    print("x:",x)
    for y in x:
        print(y)

# %% [markdown]
# ---
# # <center> <font color=darkgreen> Array operations </font> </center>
# ---
#
#
#
# # array + array
#
# + Adding two Python lists involves a `for` loop, or a comprehension.
# + With NumPy you can add two arrays with `+`.
# + Similar for other arithmetic operations.

# %%
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

# %% [markdown]
# # array + scalar 

# %%
print(a+7)

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[Array methods](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)</font>  </center>
# ---

# %%
a.

# %% [markdown]
# ### [`dot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html): Matrix product

# %%
A = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

print("A\n",A)
print("b\n",b)
print("Ab\n", A.dot(b) )     # as method of ndarray
print("AA\n", A.dot(A) )     # as method of ndarray

# %% [markdown]
# ### [`T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html): Transpose

# %%
A.T

# %% [markdown]
# ###  [`all()`](https://numpy.org/devdocs/reference/generated/numpy.all.html) [`any()`](https://numpy.org/devdocs/reference/generated/numpy.any.html): Methods on boolean arrays

# %%
A = np.arange(10)
B = A>4
print(B)
print(np.all(B))
print(np.any(B))

# %% [markdown]
# ### [`cumsum()`](https://numpy.org/devdocs/reference/generated/numpy.cumsum.html): Cumulative sum.

# %%
print(A)
print( np.cumsum(A) )

# %% [markdown]
# ### [`diff()`](https://numpy.org/devdocs/reference/generated/numpy.diff.html): Differences between subsequent elements

# %%
print(len(A))
print( len(np.diff(A) ))

# %% [markdown]
# ### [`ceil()`](https://numpy.org/devdocs/reference/generated/numpy.ceil.html) [`floor()`](https://numpy.org/devdocs/reference/generated/numpy.floor.html) [`round()`](https://docs.python.org/dev/library/functions.html#round): Rounding methods

# %%
B = A/3
print(B)
print( np.ceil(B) ) 
print( np.floor(B) ) 
print( np.round(B) ) 

# %% [markdown]
# ### [`max()`](https://docs.python.org/dev/library/functions.html#max),  [`min()`](https://docs.python.org/dev/library/functions.html#min), [`argmax()`](https://numpy.org/devdocs/reference/generated/numpy.argmax.html), [`argmin()`](https://numpy.org/devdocs/reference/generated/numpy.argmin.html): Largest and smallest elements

# %%
import random
random.shuffle(A)

print(A)
print( np.max(A) ) 
print( np.argmax(A) ) 
print( np.min(A) ) 
print( np.argmin(A) ) 

# %% [markdown]
# ### [`maximum()`](https://numpy.org/devdocs/reference/generated/numpy.maximum.html), [`minimum()`](https://numpy.org/devdocs/reference/generated/numpy.minimum.html): Element-wise max and min between two arrays

# %%
A = np.array([1,2,3,4,5])
B = np.array([5,4,3,2,1])
print( A )
print( B )
print( np.maximum(A,B) )
print( np.minimum(A,B) )

# %% [markdown]
# ### [`median()`](https://numpy.org/devdocs/reference/generated/numpy.median.html) [`mean()`](https://numpy.org/devdocs/reference/generated/numpy.mean.html) [`std()`](https://numpy.org/devdocs/reference/generated/numpy.std.html): Descriptive statistics
#

# %%
A = np.array([0,0,0,0,1,2,3,4,5,6])
print(A)
print( np.median(A) )
print( np.mean(A) )
print( np.std(A) )

# %% [markdown]
# ###  [`sum()`](https://numpy.org/devdocs/reference/generated/numpy.sum.html) [`prod()`](https://numpy.org/devdocs/reference/generated/numpy.prod.html): Aggregation
#

# %%
print( np.sum(A) )
print( np.prod(A) )

# %% [markdown]
# ### [`sort()`](https://numpy.org/devdocs/reference/generated/numpy.sort.html) [`argsort()`](https://numpy.org/devdocs/reference/generated/numpy.argsort.html): Sorting

# %%
import random

a = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(a)
stra = [str(x) for x in a]

A = np.array(a)
strA = np.array(stra)


ind = np.argsort(A)


print(A)
print(ind)

print(A[ind])
print(strA[ind])
