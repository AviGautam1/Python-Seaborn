#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import seaborn as sns

exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", y="pulse",
                hue="kind",
                data=exercise)


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[4]:


c = np.random.normal(loc=5, size=100, scale=2)


# In[6]:


sns.distplot(c)


# In[7]:


a = sns.load_dataset("iris")
b = sns.FacetGrid(a, col="species")
b.map(plt.hist, "sepal_length")


# In[8]:


a = sns.load_dataset("flights")
b = sns.PairGrid(a)
b.map(plt.scatter)


# In[9]:


sns.set(style = "darkgrid")
a = sns.load_dataset("flights")
b = sns.PairGrid(a)
b.map(plt.scatter)


# In[11]:


sns.set(style = "white", color_codes = True)
a = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a)


# In[12]:


c = sns.color_palette()
sns.palplot(c)


# In[ ]:




