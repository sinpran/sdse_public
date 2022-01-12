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
# # <center> <font color=purple>[pandas](https://pandas.pydata.org/)</font>  </center>
#
# ### <center>A tabular data structure for machine learning</center>
#
# ---
#
# `pandas` provides data structures and functionality for dealing with **tabular** data sets. 
#
# <!-- It is the basis for many machine learning libraries, including [scikit-learn](https://scikit-learn.org/stable/). -->
#
# + [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)
#
#
# ## Why use pandas
#
# Pandas tables (called "data frames") have advantages over NumPy arrays and Python lists:
# + columns have **labels**,
# + columns are **homogeneous** (values within a column have the same type),
# + pandas provides **additional data types** often found in real data. e.g. dates,
# + pandas provides functionality for dealing with **missing data**.
#
# ## Standard import

# %%
import pandas as pd

# %% [markdown]
# ## Data types
#
# + `Series`
#     + A homogeneous array of values.
#     + Represents a **column** in a table.
#     + Possibly with a name (column header)
# + `DataFrame`
#     + A collection of `Series`, with an additional 'index' column.
#     + Represents a **table**.
#     
#     
# The **index** column is the first (left-most) column of the DataFrame. 
# + Each row has a unique index.
# + You can assign an index, or let pandas assign it for you.

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Creating a DataFrame</font></center>
# ---
#
# Pandas offers many readers for creating DataFrames from external data sources. Try listing them with `pd.read_` + `Tab`

# %%
# pd.read_

# %% [markdown]
# You can also create a DataFrame from data that is already in memory using constructor.
#
# ## Create a data frame from a Python dictionary

# %%
bla = pd.DataFrame({'col_integers':[0,1,3] , 'col_strings':['str1','str2','str3']})

bla.head()

# %% [markdown]
# ## Create a DataFrame from a file

# %%
celeb_heights = pd.read_csv('celebrity-heights.csv')
celeb_heights

# %% [markdown]
# ## Create a DataFrame from online data
#
# We will load aggregate case data for the COVID-19 pandemic from the [California Open Data
# ](https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state1/resource/67c82c61-370a-4b4c-9067-15a68400b9ff) portal.

# %%
url = 'https://data.chhs.ca.gov/dataset/f333528b-4d38-4814-bebb-12db1f10f535/resource/e2c6a86b-d269-4ce1-b484-570353265183/download/covid19casesdemographics.csv'
covid19 = pd.read_csv(url)

covid19

# %% [markdown]
# ## Quick viewing: `head()`, `tail()`, `describe()`, `info()`

# %%

# %% [markdown]
# ---
# # <center> <font color=darkgreen>The index of the data frame</font></center>
# ---
#
# In the same way that columns are identified by a column header, rows are identified by an **index**. If no index is specified, pandas will generate one. You can change the index to something more convenient using `set_index()`.
#
# ## Build a data frame with a prescribed index

# %%
df_str = pd.DataFrame({'colA' : [4,7,2],
                       'colB' : ['a','b','c'],
                       'colC' : [0.1,0.2,0.3]},
                      index=['rowA', 'rowB', 'rowC'])

df_str.head()

# %% [markdown]
#
# ## Change the index: [`set_index()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
#
# You can set one of the columns of the data frame as the index using `set_index()`. If you do this "in place", it will modify the existing data frame. Otherwise it will create a new one. 

# %%
celeb_heights.set_index('fullname',inplace=True)
celeb_heights.head()

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Selecting data</font>  </center>
# ---
#
# There are several ways to select data from a DataFrame. 
#
# + `[]`: Index-based selection
# + `.loc[]` : Label-based selection
# + `.iloc[]` : Integer-based selection

# %% [markdown]
# ## `[]` Index-based selection
#
# Syntax: `X[selector]`
# + To select columns the `selector` can be
#     + A column label (string)
#     + A list of column labels (list of strings)
# + To select rows the `selector` can be
#     + A slice
#     + A boolean mask

# %% [markdown]
# ### Example: Select a single column (string)

# %%
celeb_heights['firstname']

# %% [markdown]
# ### Example: Select multiple columns (list of strings)

# %%
celeb_heights[['firstname','lastname']]

# %% [markdown]
# ### Example: Select rows (slice)

# %%
celeb_heights[0:20:3]

# %% [markdown]
# ### Example:  Boolean masking
#
# You can use a boolean list or a boolean Series as a mask for filtering rows.

# %%
celeb_heights[celeb_heights['gender']=="F"]

# %% [markdown]
# ## `loc[]` : Label-based selection
#
# Syntax: `X.loc[rowselector,columnselector]` (`columnselector` is optional)
#  
# `rowselector` can be
# + An index (integer, string, date, etc.)
# + A list of indexes.
# + A slice (only if the index is integer-based)
# + A boolean mask
#
# `columnselector` can be 
# + A string label. 
# + A list of strings labels.

# %% [markdown]
# ### Example: Select multiple rows

# %%
celeb_heights.loc[['Kristin Chenoweth','Bo Svenson']]

# %% [markdown]
# ### Example: Select multiple rows and columns

# %%
celeb_heights.loc[['Kristin Chenoweth','Bo Svenson'],['feet','inches','meters']]

# %% [markdown]
# ### Example: Boolean masking

# %%
covid19

# %% [markdown]
# ## `iloc[]`:  Integer-based selection
#     
# Syntax: `iloc[rowselector,columnselector]` (`columnselector` is optional)
#  
# `rowselector` and `columnselector` can be
# + An integer or list of integers
# + A slice
#
#     
# ### Examples

# %%
celeb_heights.iloc[0:10:2,[1,2]]

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Preparaing the data</font>  </center>
# ---

# %% [markdown]
# ## `drop(cols,args)` Delete columns and rows
# Use argument `axis=0` for rows and `axis=1` for columns.
#
# ### Example: Delete columns

# %%
celeb_heights.drop(['id','midname','ftin','feet','inches'],axis=1,inplace=True)

celeb_heights.head()

# %% [markdown]
# ### Example: Delete rows

# %%
celeb_heights.drop( 'Verne Troyer' , axis=0 , inplace=True)
celeb_heights.head()

# %% [markdown]
# ## `rename()` Rename a column

# %%
covid19.rename(columns={
    'demographic_category' : 'demcat',
    'demographic_value' : 'demval'}, inplace=True)

covid19.head()

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Time series data</font>  </center>
# ---

# %% [markdown]
# + pandas includes a special data type for representing date/time information: `Timestamp`. 
# + Use [`to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) to convert date/time strings to `Timestamp`

# %%
covid19['date'] = pd.to_datetime(covid19['report_date'])
covid19.set_index('date',inplace=True)
covid19.head()

# %% [markdown]
# ### Time-based indexing
#
# With a time-based index, we can easily get data for a particular day:

# %%
covid19.head()
covid19.loc['2020-04-25'].head()

# %% [markdown]
# or a month or a year:

# %%
covid19.loc['2020-04'].head()

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Operations</font>  </center>
# ---

# %% [markdown]
# ## [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) Aggregate over classes 
# 1. Splits a table into several tables, according to classes in one of the columns.
# 2. Applies some function to the columns of these tables.
# 3. Joins the results back into a single table with the grouping classes as index.
#
# ### Example: Find the totals for each county.

# %%
# covid19_bycounty = covid19.groupby('county').sum()
# covid19_bycounty.head()

# %% [markdown]
# ## [`sort_values()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) Sort values
# **Example** Sort the counties from most to least cases confirmed.

# %%
covid19_sort = covid19.sort_values(by='total_cases', ascending=False)
covid19_sort.head()

# %% [markdown]
# ---
# ---
# # <center> <font color=darkgreen>Plotting</font>  </center>
#
# ---
#
# + [`DataFrame.plot()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) is an all-purpose tool for plotting data in data frames.
# + See the documentation for important parameters: `x`, `y`, `kind`, etc.
#
#
# ---

# %% [markdown]
# ## `kind='bar'` 

# %%
covid19_sort['total_cases'].head().plot(kind='bar',rot=0, ylabel='Confirmed cases')

# %% [markdown]
# ## `kind='hist'` 

# %%
h = celeb_heights['meters'].plot(kind='hist',bins=60,figsize=(10,4),grid=True)
h.set_xlabel('meters')

# %% [markdown]
# ## `kind='scatter'` 

# %%
# covid19.plot(kind='scatter',x='nconf',y='ndeath',figsize=(10,4),grid=True)

# %% [markdown]
# ## `kind='line'` 

# %%
X = covid19.loc[ (covid19['demcat']=='Age Group') & (covid19['demval']=='0-17'),'total_cases']
X.plot(kind='line', figsize=(10, 6), legend=True, grid=True)

# %%
X.diff().plot(kind='line', figsize=(10, 6), legend=True, grid=True)

# %%
