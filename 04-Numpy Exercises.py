#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[2]:


import numpy as np


# #### Create an array of 10 zeros 

# In[3]:


np.zeros(10)


# #### Create an array of 10 ones

# In[4]:


np.ones(10)


# #### Create an array of 10 fives

# In[8]:


np.ones(10) * 5


# #### Create an array of the integers from 10 to 50

# In[13]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[15]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[21]:


np.arange(9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[22]:


np.identity(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[23]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[30]:


np.random.randn(25)


# #### Create the following matrix:

# In[34]:


np.arange(1,101).reshape(10,10) /100


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[41]:


np.arange(1,101,5).reshape(4,5) /100


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[67]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[40]:





# In[55]:


mat[2:,1:]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[58]:


mat[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[61]:


mat[:3,1]


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[66]:


logo depois [4,0:5]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[68]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[69]:


mat.std()


# #### Get the sum of all the columns in mat

# In[70]:


mat.sum(axis=0)


# # Great Job!
