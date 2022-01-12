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
# # <center><font color=purple>Jupyter notebooks</font> </center>
# ---

# %% [markdown]
# ## Pros
# + Story-telling environment, great for presentations, demos.
# + Good for fast prototyping
#
# ## Cons
# + `.ipynb` files are binary -- not good for version control, which creates difficulties for collaboration.
# + complexities of non-sequential execution. 
# + no advanced IDE features (breakpoints, variable inspection, step-by-step execution, autocomplete, etc.) 
# + Alternatives: **Spyder** or **PyCharm**.

# %% [markdown]
# A Jupyter notebook consists of a sequence of **cells**:

# %%

# %%

# %%

# %% [markdown]
# A cell can be a **code** cell...

# %%
# This is a code cell

print("Hello!")

# %% [markdown]
# ... or a **markdown** cell, like this one.

# %% [markdown]
# ---
# ## Anatomy of a Jupyter notebook
#
#   
# + Check out the Menubar and the Toolbar.
# + Two notebook modes:
#     + <font color=blue>**Command mode [Esc]**</font> -- Edit whole cells
#         + Use the toolbar or 
#         + keyboard shortcuts.
#             + `a`: Insert new cell above.
#             + `b`: Insert new cell below.
#             + `x`: Cut cell
#             + `c`: Copy cell
#             + `v`: Paste cell
#     + <font color=green>**Edit mode [Enter]**</font> -- Edit text within a cell
#         + Type code.

# %% [markdown]
# ## Running cells
#
# + You can run individual cells, a selection of cells, or all cells.
#     + from the Cell menu
#     + from the Toolbar
#     + `Ctrl-Enter` : Run this cell without going to next cell
#     + `Shift-Enter`: Run this cell and go to next cell.

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Code cells</font>  </center>
# ---
#
# + The last line if a cell is printed immediately following the cell.
# + Code cells can include *inline* plots. (We will learn about those later)
# + Use `Shift-Tab` to get information about a variable.
#
# ### Try it out...

# %%
a = "hello!"
a

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Markdown cells</font>  </center>
# ---
#
# Markdown cells can contain:
# + Text
# + Lists
# + Images
# + Hyperlinks 
# + Tables
# + Formatted code
# + Latex

# %% [markdown]
# ### Horizontal lines
# ---
#
# ### Lists
#
# + this is a
# + bullet 
#     + list 
#
#
# 1. this is a
# 2. numbered
# 3. list
#
# ### Images
#
# <img src="uc_berkeley.jpg" width="600">
#
# ### Hyperlinks
#
# [Click here!](https://engineering.berkeley.edu/)
#
# ### Tables
#
# | This | is   |
# |------|------|
# |   a  | table|
#
# ### Formatted code
#
# ```python
# A = (0,1,2,3)
# for i in range(4):
#     print(A[i])
# ```
#
# ### Latex
#
# The area $A$ of a circle is, $$A=\pi r^2$$

# %% [markdown]
# ---
#
# ## Text
#
# Font can be 
# + *italics*, **bold**
# + 
# <font color=blue>Blue</font> 
# <font color=red>Red</font> 
# <font color=green>Green</font> 
# <font color=pink>Pink</font> 
# <font color=yellow>Yellow</font> 
# + Headings:
# # H1
# ## H2
# ### H3
# #### H4
