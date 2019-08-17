#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:





# In[2]:


print(purchase_data.columns)


# In[3]:


purchase_data.head()


# In[4]:


#.index= gives a count of the first column of the data field
#purchase_data.duplicated("SN")
#total_count = purchase_data.drop_duplicates("SN", keep = "first")
total_count = purchase_data["SN"].unique()
data = {"Total Players": len(total_count)}
#print(len(total_count))
df = pd.DataFrame(data, index = [0])
df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:





# In[5]:


unique_items = purchase_data["Item ID"].unique()
items_count = len(unique_items)
item_avg = "${:,.2f}".format(purchase_data["Price"].mean()) 
purchase_num = len(purchase_data.index)
total_revenue = "$" + f'{purchase_data["Price"].sum():,}'
analysis_data = {"Number of Unique Items":items_count, 
                 "Average Price": item_avg, 
                 "Number of Purchases": purchase_num, 
                 "Total Revenue":total_revenue}
analysis_df = pd.DataFrame(analysis_data, index = [0])
analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:





# In[6]:


count_gender = purchase_data.groupby("Gender").agg({'SN': 'nunique'})
#count_gender.sort_values(by = ["SN"], ascending = False)
count_gender["Percentage of Players"] = round(count_gender["SN"]/count_gender["SN"].sum() * 100,2)
del count_gender.index.name
count_gender.rename(columns={"SN":"Total Count"}) 


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:





# In[7]:


def f(x):
    d = {}
    d['Purchase Count'] = round(x['Purchase ID'].count())
    d['Average Purchase Price'] = round(x['Price'].mean(),2)
    d['Total Purchase Value'] = round(x['Price'].sum(),2)
    d['Avg Total Purchase per Person'] = round(x['Price'].sum()/x['SN'].nunique(),2)
    return pd.Series(d, index = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value','Avg Total Purchase per Person'])
gender_data = purchase_data.groupby('Gender').apply(f)
gender_data


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:





# In[8]:


# total_count = purchase_data.groupby("Age")
#.agg({"SN":"count"})
age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 45]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Range"] = pd.cut(purchase_data['Age'], age_bins, labels = age_labels)
sn_count = purchase_data.groupby("Age Range").agg({"SN":"nunique"})
sn_count['Percentage of Players'] = round(((sn_count["SN"]/sn_count['SN'].sum()))*100,2)
sn_count.rename(columns = {"SN":"Total Count"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:





# In[12]:



def f(x):
    d = {}
    d['Purchase Count'] = round(x['Purchase ID'].count())
    d['Average Purchase Price'] = round(x['Price'].mean(),2)
    d['Total Purchase Value'] = round(x['Price'].sum(),2)
    d['Avg Total Purchase per Person'] = round(x['Price'].sum()/x['SN'].nunique(),2)
    return pd.Series(d,index = [
        'Purchase Count', 'Average Purchase Price', 'Total Purchase Value','Avg Total Purchase per Person'])
#make age bins, do group by of age bins, add clmns for results set
age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 44]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Range"] = pd.cut(purchase_data['Age'], age_bins, labels = age_labels)
#apply- applies a function the index of our dataframe (performs the function to each row)
age_data = purchase_data.groupby('Age Range').apply(f)
age_data.sort_values(['Age Range'], axis=0, ascending=True, inplace=True) 

age_data


# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:





# In[10]:


def f(x):
    d = {}
    d['Purchase Count'] = int(x['Purchase ID'].count())
    d['Average Purchase Price'] = round(x['Price'].mean(),2)
    d['Total Purchase Value'] = x['Price'].sum()
    return pd.Series(d, index = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value'])
top_purchases = purchase_data.groupby('SN').apply(f)
top_purchases.sort_values(['Total Purchase Value'], axis=0, ascending=False, inplace=True) 
top_purchases.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:





# In[13]:


def f(x):
    d = {}
    d['Purchase Count'] = x['Purchase ID'].count()
    d['Item Price'] = x['Price'].min()
    d['Total Purchase Value'] = x['Price'].sum()
    return pd.Series(d, index = ['Purchase Count', 'Item Price', 'Total Purchase Value'])
popular_items = purchase_data.groupby(['Item ID', 'Item Name']).apply(f)
popular_items.sort_values(['Purchase Count'], axis=0, ascending=False, inplace=True) 
popular_items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:





# In[13]:


def f(x):
    d = {}
    d['Purchase Count'] = x['Purchase ID'].count()
    d['Item Price'] = x['Price'].min()
    d['Total Purchase Value'] = x['Price'].sum()
    return pd.Series(d, index = ['Purchase Count', 'Item Price', 'Total Purchase Value'])
popular_items = purchase_data.groupby(['Item ID', 'Item Name']).apply(f)
popular_items.sort_values(['Total Purchase Value'], axis=0, ascending=False, inplace=True) 
popular_items.head()


# In[ ]:


# You must include a written description of three observable trends based on the data.
# 1) The item with the highest price is different from the item with the highest purchase value, 
#    meaning that higher priced items are not necessarily the most profitable
# 2) The most popular item has the highest purchse value
# 3) The average total purchase per person is fairly evenly distributed across the age bins

