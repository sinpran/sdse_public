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
# # <center> <font color=purple>[scikit-learn](https://scikit-learn.org/stable/)</font>  </center>
# ## <center>Machine learning algorithms</center>
#
#
# ---
#
# ---
# # <center> <font color=darkgreen>The supervised learning problem</font>  </center>
# ---
#
#
# The machine learning problem is to model a **"black box"** system given samples of inputs and outputs. 
#
# <img src="mlprob.svg" width="300">
#
# + The system has some number $m$ of **measured inputs** ($x_1...x_m$) and a single output $Y$.
# + We use a capital letter $Y$ to indicate that the output is a **random variable**.
# + This means that it is distributed according to a **probability distribution**, which depends on the inputs.
# + We are given a dataset $D$, consisting of $n$ samples of the system (inputs and outputs).
# + $D$ is represented as a *table*:
# <img src="table.svg" width="150">
#
# ## Problem statement: 
# Given a dataset $D$, construct a **model** of the system. A model is any algorithm that, given a new set of inputs, can predict the expected output (hopefully with high acuracy). 
#
# ## Notes
#
# + This is called **supervised** learning because the dataset includes the "answers" $y^k$. The other large class of machine learning problems are the **unsupervised** problems, in which only the inputs are given. In unsupervised learning, we are limitted to finding patterns in the input data (e.g clusters).
#
# + $k$ is the sample index. 
# + The inputs $x_1...x_m$ are known as the **features**. These can be real-valued or discrete-valued (categorical). 
# + The output $Y$ can be real-valued or categorical. 
#     + $Y$ is real-valued $\rightarrow$ **regression**
#     + $Y$ is categorical $\rightarrow$ **classification**
#
# ---
# # <center> <font color=darkgreen>A standard workflow</font>  </center>
# ---
#
# <img src="mlworkflow.svg" width="500">
#
# 1. **Algorithm selection**: Choose an estimator according to your problem type (e.g. linear regression versus SVM)
# 2. **Hyper-parameter selection**: Hyper-parameters are kept fixed during model training.
# 3. **Data preparation**: Clean, impute, normalize.
# 4. **Data splitting**: Training vs. Testing data. 
# 5. **Parameter fitting**: Find parameters that best fit the data.
# 6. **Performance evaluation**: Evaluate the model using the testing data. 
#
# ## Cross-validation
#
# Compute a more robust (cross-validated) score by repeating the process with different data splits. 
# <!-- <img src="../figs/crossvalidation.svg" width="500"> -->
#
#
# ## Hyper-parameter tuning
#
# Optimize the hyper-parameters (in addition to the fitted parameters) using grid-search or random sampling.
#
# <img src="hptuning.svg" width="500">
#

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen>Example : A linear regression for the progression of diabetes</font>  </center>
# ---
#
# + scikit-learn includes several [toy datasets](https://scikit-learn.org/stable/datasets/index.html#) that you can use for practice. 
# + [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes) dataset.

# %%
from sklearn import datasets
diab = datasets.load_diabetes()

print(diab['DESCR'])

# %% [markdown]
# ## 1. Data prep (pandas)
#
# scikit-learn is built on **NumPy**. **It does not require pandas**. Even so, pandas can be helpful for
#
# 1. preparing the data
#
# 2. visualizing the data

# %%
import pandas as pd

df = pd.DataFrame(diab['data'],columns = diab['feature_names'])
df['target']=diab['target']

df.head()

# %%
df['target'].plot(kind='hist')

# %% [markdown]
# ## 2. Data splitting : [`train_test_split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

# %%
import numpy as np 
import sklearn.model_selection as model_selection

X = df.loc[:,['bmi','age']].values
y = df.loc[:,'target'].values

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.6)

# %% [markdown]
# ## 3. Parameter fitting : `fit()`

# %%
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

# %% [markdown]
# ## 4. Performance evaluation : `predict()`

# %%
y_pred = regr.predict(X_test)

from sklearn import metrics

print('Mean squared error: %.2f' % metrics.mean_squared_error(y_test, y_pred))
print('Coefficient of determination: %.2f' % metrics.r2_score(y_test, y_pred))

# %% [markdown]
# ## Plot the result

# %%
import matplotlib.pyplot as plt
plt.scatter(X_test[:,0], y_test, color='black')
plt.scatter(X_test[:,0], y_pred, color='blue')

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen>Example : Recognizing handwritten digits</font>  </center>
# ---
#

# %%
# load the data
digits = datasets.load_digits()

print(digits['DESCR'])

# %%
# put it into pandas (optional)
df = pd.DataFrame(digits['data'],columns = digits['feature_names'])
df['target'] = digits['target']

df

# %%
# Split data 
X_train, X_test, y_train, y_test = model_selection.train_test_split( digits['data'], digits['target'], train_size=0.7)

# %%
from sklearn import svm
model = svm.SVC(gamma=0.001) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)

# %%
pd.DataFrame(np.vstack([y_test,y_pred]).T,columns=['test','pred'])

# %%
print(metrics.classification_report(y_test, y_pred))

# %%
metrics.plot_confusion_matrix(model, X_test, y_test)

# %% [markdown]
# # [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) [`cross_val_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score)
#
# Cross-validation is a method for computing a more robust estimate of the performance of a model with limited data. 
#
# <img src="cv.png" width="450">

# %%
from sklearn.model_selection import cross_val_score

X = digits['data']
y = digits['target']

# Train on 80%, test on 20%
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, train_size=0.8 )

single_score = svm.SVC(gamma=0.001).fit(X_train, y_train).score(X_test, y_test)

# 5-fold cross validation
cv_scores = cross_val_score(svm.SVC(gamma=0.001), X, y, cv=5)

print(single_score)
print(cv_scores)

# %% [markdown]
#
# ---
# # <center> <font color=darkgreen>Additional topics</font>  </center>
# ---
#
# + [Hyper-parameter tuning](https://scikit-learn.org/stable/modules/grid_search.html)
# + [Pipelines](https://scikit-learn.org/stable/modules/compose.html)
