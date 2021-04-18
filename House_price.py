#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[12]:


df = pd.read_csv('C:/Users/Specter/Desktop/resources/Data Files/1. ST Academy - Crash course and Regression files/House_Price.csv',header = 0
            
                )


# In[14]:


df.head()


# In[ ]:





# In[15]:


df.head()


# In[16]:


df.shape


# In[17]:


df.describe()


# In[18]:


sns.jointplot(x='n_hot_rooms',y='price',data=df) 


# In[20]:


sns.jointplot(x='rainfall',y='price',data=df)


# In[21]:


df.head()


# In[22]:


sns.countplot(x='airport',data=df)


# In[23]:


sns.countplot(x='waterbody',data=df)


# In[24]:


sns.countplot(x='bus_ter',data=df)


# In[ ]:


##Observations
#1.Missing values in n_hos_beds.
#2.Skewness or outliers in crime  rate.
#3.Outliers in n_hot_rooms and rainfall.
#4.Bus_ter has only one value

