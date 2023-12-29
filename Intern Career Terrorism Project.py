#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = r"C:\Users\DELL\Desktop\Terrorism.xlsx"


# In[3]:


ter = pd.read_excel(file)
ter.head()


# In[58]:


ter


# In[59]:


ter.shape


# In[60]:


ter.describe(include = 'all')


# In[61]:


ter.info()


# In[62]:


ter.columns


# In[63]:


ter.isnull().sum().sum()


# In[64]:


terr = ter.fillna(value='None')


# In[65]:


terr


# In[66]:


terr.columns


# In[67]:


terr.drop(columns=['region','attacktype1','attacktype2','attacktype3'], inplace = True) 
#df.drop(['C', 'D'], axis=1)
#df.drop(columns =['C', 'D'])


# In[68]:


terr.drop(columns = ['targtype1','targsubtype1','natlty1',
                     'targtype2','targsubtype2','natlty2',
                     'targtype3','targsubtype3','natlty3'], inplace = True)


# In[69]:


terr.drop(columns = ['gname','gsubname','gsubname2',
                     'gname3','gsubname3','motive','guncertain1',
                     'guncertain2','guncertain3','individual',
                     'nperps','nperpcap','claimed','claimmode',
                     'claimmode_txt','claim2','claimmode2',
                     'claimmode2_txt','claim3','claimmode3',
                     'claimmode3_txt','compclaim'], inplace = True)


# In[70]:


terr


# In[71]:


terr.columns


# In[72]:


terr.drop(columns = ['gname2','ishostkid', 'nhostkid', 'nhostkidus', 'nhours', 'ndays', 'divert',
       'kidhijcountry', 'ransom', 'ransomamt', 'ransomamtus', 'ransompaid',
       'ransompaidus', 'ransomnote', 'hostkidoutcome', 'hostkidoutcome_txt',
       'nreleased', 'addnotes', 'scite1', 'scite2', 'scite3', 'dbsource',
       'INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY', 'related'], inplace = True)


# In[73]:


terr.columns


# In[103]:


# Create visualizations that display the number of terrorist attacks over time.
Q1 = terr[['iyear', 'attacktype1_txt']].groupby('iyear').count().sort_values('attacktype1_txt', ascending = False)
Q1


# In[112]:


Q1.to_excel('overtime.xlsx',index=True)


# In[86]:


# Analyze trends in attack types and weapons used.
terr[['iyear', 'attacktype1_txt','attacktype2_txt', 'attacktype3_txt',
      'weapsubtype1_txt', 'weaptype1_txt', 
      'weapsubtype2_txt', 'weaptype2_txt',
      'weapsubtype3_txt', 'weaptype3_txt',
      'weapsubtype4_txt', 'weaptype4_txt']][0:20]#.head()#.groupby('iyear')#.count().sort_values('attacktype1_txt', ascending = False)


# In[109]:


# Visualize attack locations on a map.
Q2 = terr[['attacktype1_txt','latitude', 'longitude']]
Q2


# In[111]:


Q2.to_excel('map.xlsx', index= False )


# In[114]:


#  Compare casualties by region or year.
Q3 = terr[['region_txt','nkill']]
Q3


# In[126]:


Q3 = Q3['nkill'].replace({'None': 0}, inplace=True)


# In[127]:





# In[115]:


Q3.to_excel('region.xlsx', index = False)


# In[125]:





# In[ ]:




