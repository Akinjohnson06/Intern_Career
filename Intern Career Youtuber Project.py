#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = r"C:\Users\DELL\Desktop\youtubers_df.csv" #file path


# In[3]:


youtuber = pd.read_csv(file)
youtuber.head()


# In[4]:


# Data Exploration
# explore the dataset
youtuber.shape


# In[5]:


youtuber.info()


# In[6]:


youtuber.columns


# In[9]:


youtuber.describe(include = 'all')


# In[8]:


# Clean data
# Dropping the link column
youtuber.drop(columns=['Links'], inplace = True) 
#inplace makes it permanent. Without it, it will just display what you want to see, and it will be temporary


# In[22]:


youtuber.head()


# In[23]:


# Renaming columns
youtuber.rename(columns = {'Username':'Youtube Names', 'Visits':'Streams', 'Suscribers':'Subscribers'}, inplace = True)


# In[24]:


youtuber


# In[25]:


youtuber.info()


# In[26]:


youtuber


# In[27]:


# Removing the decimal point in the Subcriber, streams, likes, and comments column
youtuber[['Subscribers', 'Streams', 'Likes', 'Comments']] = youtuber[['Subscribers', 'Streams', 'Likes', 'Comments']].astype(int)
youtuber.head()


# In[28]:


# check for null values
#youtuber.isnull()
youtuber.isnull().sum()


# In[29]:


# dealing with missing value
# we can input it into another variable, just so that we dont tamper with the original Dataframe
youtubers = youtuber.fillna(value = 'None')
youtubers


# In[30]:


# Check if it worked
youtubers.isnull().sum()


# In[31]:


youtubers.head(20)


# In[32]:


# Trends amongst the top streamers
# which categories are the most popular
x = youtubers.sort_values('Streams', ascending = False)#.head(10)
x[['Categories', 'Streams']].head(10)


# In[33]:


# correlation between the number of subscribers and the number of likes or comments
youtubers['Subscribers'].corr(youtubers['Likes'])
# the result shows that they are a little bit correlated based on the correlation range of -1 to 1


# In[34]:


# distribution of streamer audiences by country.
x = youtubers.sort_values('Streams', ascending = False)
x[['Country', 'Streams']].head(10)


# In[35]:


youtubers


# In[36]:


# average number of subscribers, visits, likes, and comments.
x = youtubers ['Subscribers'].mean()
y = youtubers ['Streams'].mean()
z = youtubers ['Likes'].mean()
zz = youtubers ['Comments'].mean()

print(f'average subscriber is {x}')
print(f'average stream is {y}')
print(f'average likes is {z}')
print(f'average comments is {zz}')


# In[37]:


# categories have the highest number of streamers
youtubers[['Categories', 'Streams']].sort_values('Streams', ascending = False).head(10)
#youtubers[['Categories', 'Streams']].head(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




