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
# # <center><font color=purple>Code organization : Functions, modules, and packages </font> </center>
# ---
#
# Now that we have covered the basic syntax of Python, we will begin to learn how to build code to solve interesting problems. Programming is often a group or even community activity, and it is therefore important to write code that is clear and well organized. 
#
# Here are a few tips.
#
# + Use informative variable names, even if they are a bit longer.
# `flow_m3perhr` is better than `x`.
# + Include lots of *comments*. `#`
# + Gather reusable code **functions**. 
# + Gather functions into **modules**. 
# + Gather modules into **packages**. 

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Functions</font>  </center>
# ---
#
# Functions are the building blocks of your programs. These are chunks of code that depend on some data (the inputs) to produce other data (the outputs).
#
# We have already used many functions.
#
# Let's now learn how to create our own.
#
# # Syntax
#
# ```python
# def <name of the function>( <arguments> ):
#    <body>
#    return <output>
# ```
#
# + `def` tells Python that what follows is a function.
# + The body of the function is indented with respect to `def`.
# + `<arguments>` is optional.
# + Notice the `:`
# + The `return` statement tells Python to exit the function and return `<output>`. There may be multiple (or no) `return` statements in the function. 
# + Functions in Python must be defined **before** they are used. 
#
# ### Example
#
# Write a function that adds one to a numer.

# %%
def addone(x):
    return x+1


# %% [markdown]
# Th following will not work because the function is used before it is defined. 

# %%
print(multiply_by_7(2))

def multiply_by_7(a):
    b = a*7
    return b


# %% [markdown]
# ---
# # Input 
#
# Inputs can be passed to functions via either *positional* or *keyword* arguments. 
#
# ## Positional arguments
# This is the style used in most programming languages, including C, C++, Java, Fortran, Javascript, and Matlab. Here the multiple inputs must be passed by the caller in the same order as they are listed in the function declaration.

# %%
def compute_change(unit_price,quantity,payment):
    change = payment - unit_price*quantity
    return change
    
change = compute_change(10,2,30)
print("Return ${0}.".format(change)) 

# %% [markdown]
# This approach can be a source of errors. The *keyword* or *named* style of calling functions is preferred.
#
# ## Keyword arguments
# Here the name of each input argument is used when calling the funciton. When we do this, the order of the arguments no longer matters. Notice in the example below that the order is changed. 

# %%
change = compute_change(payment=30,unit_price=10,quantity=2)
print("Return ${0}.".format(change)) 


# %% [markdown]
# ## Default values
# It is legal in Python to not provide values for every single input parameter, so long as the ones left out have *default values*. The default values are provided in the function definition. 

# %%
def compute_change_with_defaults(unit_price=1,quantity=1,payment=0):
    change = payment - unit_price*quantity
    return change
    
change = compute_change_with_defaults(payment=30,unit_price=10)
print("Return ${0}.".format(change)) 


# %% [markdown]
# ---
# # Output
# Functions are allowed to return only a single object. 
#
# The **positional** style for returning multiple values is to package them into a **tuple**, and unpack them on the output. 

# %%
def integer_division(num,den):
    q = num//den
    r = num - q*den
    return (q,r)

q, r = integer_division(5,2)

print(q, r)


# %% [markdown]
# The **keyword** style is to use a **dictionary**.

# %%
def integer_division_d(num,den):
    q = num//den
    r = num - q*den
    return {'q':q,'r':r}

X = integer_division_d(5,2)

print(X['q'], X['r'])

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Modules and Packages</font>  </center>
# ---
#
# ## Module
#
# A [**module**](https://docs.python.org/3.8/tutorial/modules.html) is a *file* containing functions.
#
# + A module is contained in a single `.py` file. (e.g. mymodule.py)
# + A module can include a "main function": `if __name__ == "__main__":` 
#
# ## Package
#
# A [**package**](https://docs.python.org/3.8/tutorial/modules.html#packages) is a set of modules that work together. 
#
# + A package is contained in a single folder. (e.g. mypackage/)
# + ~~A package folder must contain a file called `__init__.py`~~. **Note: This is no longer true, even though the documentation says so.**
# + A package folder *may* contain a file called `__init__.py` with package initialization information. This can include:
#     + specifying which modules to load, by setting `__all__`
#     + providing the location of package components that reside in other folders, by setting `__path__`. 
#     + defining global variables.
#     
#
# ---
#
# # [`import`](https://docs.python.org/3/reference/import.html)
#
# `import` a module into your workspace. Calls `__init__.py`.
#
# ---
#
# ### Import a single module from a package
#
# Import `moduleA` from `mypackage`

# %%
import mypackage.moduleA

# %% [markdown]
# + `mypackage.moduleA` is now a valid prefix for functions in `moduleA`. (`moduleA` isn't).
# +  Call a function from `moduleA` as follows

# %%
mypackage.moduleA.sayHi()

# %% [markdown]
# ### `from` 
#
# + Import only some modules from the package.
# + Make the package name a valid prefix. Ie. invoke with `module.function()` instead of `package.module.function()`

# %%
from mypackage import moduleB, moduleA

moduleB.sayHi()

# %% [markdown]
# We can also use `from` to import individual functions from a module. In this case, the functions can be called directly with no prefix.

# %%
from mypackage.moduleB import sayHi, sayB

sayHi()


# %% [markdown]
# **Rule of thumb**: Begin the function call with whatever follows `import`.

# %% [markdown]
# ### `as`: Replace the prefix with an alias.

# %%
from mypackage import moduleA as mA
from mypackage import moduleB as mB

mA.sayHi()
mB.sayHi()

# %% [markdown]
# The same applies to importing functions from modules. 

# %%
from mypackage.moduleA import sayHi as AAA

AAA()

# %%
