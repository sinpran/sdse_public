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
# # <center><font color=purple>[Control flow](https://docs.python.org/3/tutorial/controlflow.html)</font> </center>
#
#  <center> if statements and loops </center>
#
# ---
#
# ## On the use of whitespace in Python
#
# + Other programming languages (C, C++, Java, Matlab, etc):
#     + *whitespace* (spaces and tabs) is ignored. 
#     + Blocks of code are demarcated with special symbols (curly brackets in C, C++, Java; 'end' in Matlab, etc.).
#
# + In contrast, Python *indentation levels* to demarcate blocks of code.
# + **Consistency** is important.
# + Common practice:
#     + **tab character** or 
#     + **4 white spaces**

# %%

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)</font>  </center>
# ---
#
# An *if* statement (or *conditional* statement) determines which of several blocks of code should be executed, depending on the value of a boolean expression. 
#
# **Syntax**
#
# ```python
# if <boolean expression 1>:
#     <code block 1>
# elif <boolean expression 2>:
#     <code block 2>
#     # ...
# elif <boolean expression N-1>:
#     <code block N-1>
# else:
#     <code block N>
# ```
#
# ### Example : Issuing a speeding ticket

# %%
speed = 140
license_expired = False
speed_limit = 120

if speed>speed_limit and license_expired:
    print("You get a big ticket!")
if speed>speed_limit and not license_expired:
    print("You get a small ticket.")
elif speed < 0:
    print("Wrong way!")
else:
    print("Have a nice day!")

# %% [markdown]
# **Note**:
# + The boolean expressions can include `and`, `or`, and `not`.
# + At most one code block will be executed. 
# + Don't forget the `:`

# %% [markdown]
# ---
# ## <center><font color=dark> >> 5-minute challenge << </font></center> 
# ---
#
# Write code that will print whether you are at work or not depending on the day and time. 

# %%
workdays = {"Sunday","Monday","Tuesday","Wednesday","Thursday"}
start_time = 8
end_time = 16

day = "Sunday"
time = 12

# %% [markdown]
# ---
# # <center> <font color=darkgreen>while loops</font>  </center>
# ---
#
# A **while** loop executes a block of code as long as a boolean expression evaluates to `True`.
#
# `while <boolean expression>:
#     <code block>
# `
#
# **Example**

# %%
a=1
while a<10:
    print(a)
    a = a+1

# %% [markdown]
# ---
# # <center> <font color=darkgreen>[for loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)</font>  </center>
# ---
#
# A **for** loop executes the block of code as many times as there are items in a given iterable (set, list, tuple, string, or dict). A variable is assigned successive values from the iterable. If the iterable is non-sequential (i.e. a set or dict), then the order is not guaranteed. 
#
# ```python
# for <variable> in <iterable>:
#     <code block>
# ```
#
# ### Example : iterate through a list

# %%
alist = ['5',9+1j,0.1]
for n in alist:
    print(n)

# %% [markdown]
# ### Example : iterate through a set

# %%
aset = {'5',9+1j,0.1,0.1,0.1}
for n in aset:
    print(n)

# %% [markdown]
# **Note** The order is not necessarily preserved.

# %% [markdown]
# ### Example : iterate through a tuple

# %%
atuple = ('5',9+1j,0.1,0.1,0.1)
for n in atuple:
    print(n)

# %% [markdown]
# ### Example : iterate through a dict

# %%
adict = {0:'5',1:9,2:0.1}
for n in adict.values():
    print(n)
    
adict

# %% [markdown]
# **Note**. `adict.items()` returns key/value pairs as tuples.

# %% [markdown]
# # [`break` and `continue`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
#
# Used within loops (both `for` and `while`).
# + `break`: exit the for (or while) loop immediately. 
# + `continue`: ignore the rest of the block and go on to next iteration.

# %% [markdown]
# **Example**: It is common to use `while True:` with a `break` statement.

# %%
x=0
while True:
    x = x + 0.5
    print(x)
    if x**2>=9:
        break

# %% [markdown]
# # [range](https://docs.python.org/3/library/functions.html#func-range)
# It is very common to iterate through a uniformly spaced list of numbers. The `range` function (it is actuatlly a type) is useful for this.
#
# **Syntax**
# `range(start,stop,step)`  (step is optional)
#
# ## Examples

# %%
a = range(4,10,2)
list(a)

# %%
# Iterate through numbers from 0 to 4
for index in range(0,500,2):
    print(index)
