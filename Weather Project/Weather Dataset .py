#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python(Big Data Analysis)

# ## The Weather DataSet
Here The Weather DataSet is a time series data set with per hour information about weather condition at particular location
We are going to analyse the data set using pandas
# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"D:\Data Analyst Project\Weather Project\1. Weather Data.csv")


# In[3]:


data


# # How To Analyse DataFrame? 

# # .head()
It shows the first N rows in the data (by default, N=5).
# In[5]:


data.head()


# # .shape
It shows the total no. of rows and no. of columns of the dataframe
# In[6]:


data.shape


# # .index
This attribute provides the index of the dataframe
# In[7]:


data.index


# # .columns
 It shows the name of each column
# In[8]:


data.columns


# # .dtypes
It shows the data-type of each column
# In[9]:


data.dtypes


# # .unique() 
In a column, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe.
# In[11]:


data['Weather'].unique()


# # .nunique()
It shows the total no. of unique values in each column. It can be applied on a single column as well as on the whole dataframe.
# In[12]:


data.nunique()


# # .count 
 It shows the total no. of non-null values in each column. It can be applied on a single column as well as on the whole dataframe
# In[13]:


data.count()


# # .value_counts
 In a column, it shows all the unique values with their count. It can be applied on a single column only.
# In[14]:


data.value_counts()


# In[16]:


data['Weather'].value_counts()


# # .info()
Provides basic information about the dataframe.
# In[17]:


data.info()


# # Q. 1)  Find all the unique 'Wind Speed' values in the data.

# In[18]:


data.head(2)


# In[19]:


data.nunique()


# In[20]:


data['Wind Speed_km/h'].nunique()


# In[21]:


data['Wind Speed_km/h'].unique() #Answer


# # Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[22]:


data.head()


# In[24]:


#value_count
data.Weather.value_counts()


# In[26]:


#filtering
data.head(2)


# In[27]:


data[data.Weather == "Clear"]


# In[28]:


#groupby
data.head(2)


# In[29]:


data.groupby("Weather").get_group("Clear")


# # Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[30]:


data.head()


# In[32]:


data[data["Wind Speed_km/h"]==4]


# # Q. 4) Find out all the Null Values in the data.

# In[33]:


data.isnull()


# In[34]:


data.isnull().sum()


# In[35]:


data.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[36]:


data.head(3)


# In[38]:


data.rename(columns={"Weather": "Weather Condition"},inplace=True)


# In[39]:


data.head()


# # Q. 6) What is the mean 'Visibility' ?

# In[41]:


data.head()


# In[42]:


data.Visibility_km.mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[44]:


data.head()


# In[45]:


data.Press_kPa.std()


# # Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# In[46]:


data.head()


# In[49]:


data['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[50]:


#value_counts()
data.head()


# In[51]:


data["Weather Condition"].value_counts()


# In[52]:


#filtering 
data.head()


# In[53]:


data[data["Weather Condition"]=="Snow"]


# In[54]:


data[data["Weather Condition"]=="Snow"].value_counts()


# In[55]:


#str.contains 
data.head()


# In[57]:


data[data["Weather Condition"].str.contains("Snow")]


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[58]:


data.head()


# In[59]:


data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"]==25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# In[60]:


data.head()


# In[61]:


data.groupby("Weather Condition").mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# In[62]:


data.head()


# In[63]:


data.groupby("Weather Condition").max()


# In[64]:


data.groupby("Weather Condition").min()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[65]:


data[data["Weather Condition"]=="Fog"]


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[66]:


data[(data["Weather Condition"]=="Clear") | (data["Wind Speed_km/h"] > 40)]


# # Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'

# In[68]:


data[((data["Weather Condition"]=="Clear") | (data["Rel Hum_%"] > 50)) | (data["Visibility_km"] > 50)]


# In[ ]:




