# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')

# %%
def f(x1, x2):
    return (x1**3)/3 -4*x1 + (x2**3)/3 -16*x2

# %%
# Part (b)
s1 = np.array([2, -2, 2, -2])
s2 = np.array([4, 4, -4, -4])
print(f(s1, s2))

# %%
# Part (c)
x1 = np.arange(-10, 10, 0.25)
x2 = np.arange(-10, 10, 0.25)
X1, X2 = np.meshgrid(x1, x2)
fig, ax = plt.subplots( figsize=(10,10), subplot_kw={"projection": "3d"})
ax.plot_wireframe(X1, X2, f(X1,X2), linewidth=0.5)
ax.scatter3D(s1, s2, f(s1, s2), c='m', marker='o', s=100, alpha=1)
plt.show()

