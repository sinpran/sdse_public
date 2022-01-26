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
# # <center><font color=purple>[Matplotlib](https://matplotlib.org/)</font> </center>
#
# ### <center>Plots</center>
#
#
# ---
# + Matplotlib designed to be Matlab-like.
# + main package: `pyplot`
# + [Tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html)
# + [Types of plots](https://matplotlib.org/gallery/index.html)
#
# ## Standard import statement ([pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot))

# %%
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Figures and axes</font>  </center>
# ---

# %% [markdown]
# <img src="figure_axes.png" width="300">

# %% [markdown]
# Create a figure with [`plt.figure()`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure) and axes with [`plt.subplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot). 
#
# + Use `figsize` to control the size of the figure.

# %%
fig = plt.figure(figsize=(12,4))
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

# %% [markdown]
#
#

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Line plots</font>  </center>
# ---

# %%
# create a figure with a single Axes
fig = plt.figure(figsize=(10,4))

# data
x = np.linspace(0,2*np.pi,20)
y = np.sin(x)

print(len(x))

# plot it on the axes
plt.plot(x, y)

# %% [markdown]
# ## Configuring the axes: [`set()`](https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axes.Axes.set.html#examples-using-matplotlib-axes-axes-set)
#
# Pass keyword arguments such as: `xlabel`, `ylabel`, `xlim`, `ylim`, `title`
#         

# %% [markdown]
# ## Example: `subplots()`, `set_*()`, `grid()`, `legend()`.

# %%
# this is a shortcut for creating the figure and axes at the same time.
fig = plt.figure(figsize=(10,4))

# plot returen a list of Line2D objects
line = plt.plot(x,np.sin(x))

# explore the set_ methods
line[0].set_linewidth(8)
line[0].set_linestyle(':')
line[0].set_color('r')

# add a grid
plt.grid()

# add a legend -- note that it takes a list!
plt.legend(['This is the legend.'])

# %% [markdown]
# ## Example: Using [keyword arguments](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.axes.Axes.plot.html) instead of `set_`

# %%
# this is a shortcut for creating the figure and axes at the same time.
fig = plt.figure(figsize=(10,4))

# plot returen a list of Line2D objects
plt.plot(x,np.sin(x),label='sine',linewidth=3,linestyle='--',color='r')

# add a grid
plt.grid()

# add a legend -- note that it takes a list!
plt.legend()

# %% [markdown]
# ---
# ## <center><font color=dark> >> 3-minute challenge << </font></center>
# ---
#
# + Copy the code from the previous cell.
# + Add a second line, for the cosine, in blue.
# + Add a legend item for the cosine.

# %%
# this is a shortcut for creating the figure and axes at the same time.
fig = plt.figure(figsize=(10,4))

# plot returen a list of Line2D objects
plt.plot(x,np.sin(x),label='sine',linewidth=3,linestyle='--',color='r')
plt.plot(x,np.cos(x),label='cosine',linewidth=3,linestyle='-',color='b')

# add a grid
plt.grid()

# add a legend -- note that it takes a list!
plt.legend()



# %% [markdown]
# ## Example: Markers

# %%
fig = plt.figure(figsize=(10,4))
plt.plot(x,np.sin(x),color='r',marker='o',label='sine')
plt.plot(x,np.cos(x),color='b',marker='+',label='cosine')  

plt.grid()
plt.legend()

# %% [markdown]
# ## Example: Markers only (`linestyle='none'`)

# %%
fig = plt.figure(figsize=(10,4))

x = np.linspace(0,10)
y_clean = np.cos(x)
y_noisy = y_clean + np.random.normal(0,.3,50)

plt.plot(x,y_clean,label='average', color='m', linewidth=2)
plt.plot(x,y_noisy,label='samples', color='b', linestyle='none',marker='o',markersize=4)

plt.grid()
plt.legend()

# %% [markdown]
# **Note**: You can also use [`scatter()`](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter) for this.

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Histograms [`hist()`](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.axes.Axes.hist.html)</font>  </center>
# ---
#

# %%
import random
my_data = [random.gauss(0,1) for i in range(400)]

fig = plt.figure(figsize=(10,4))
plt.hist(my_data,100)
plt.grid()

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Bar plots [`bar()`](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar)</font>  </center>
# ---
#

# %%
state_population = {
    'California':39_512_223,
    'Texas':28_995_881,
    'Florida':21477737,
    'New York':19453561,
    'Pennsylvania':12801989,
    'Illinois':12671821,
    'Ohio':11689100,
    'Georgia':10617423,
    'North Carolina':10488084 }


fig = plt.figure(figsize=(12,5))
plt.bar(state_population.keys(),state_population.values())
plt.ylabel('population (tens of millions)',fontsize=16)
plt.title('US largest states',fontsize=20)
plt.grid()

# %% [markdown]
# ---
# # <center> <font color=darkgreen>Save the figure: [`savefig()`](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.savefig.html) </font>  </center>
# ---

# %%
my_data = [random.gauss(0,1) for i in range(400)]

fig = plt.figure(figsize=(10,4))
plt.hist(my_data,30)
plt.grid()

from pathlib import Path
filename = str(Path.home()) + '/myfig.png'

print(filename)
plt.savefig(filename)
