#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[4]:


import numpy as np 


# In[5]:


#comparision of trends uing line graphs

x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
y= [3314, 3124, 3879, 4769, 3850, 5792, 5711, 6559, 7632, 7212, 8845, 9324, 9480, 10067, 10425, 10539, 10675, 13824, 11530, 12189]
z = [1386, 1456, 1565,2221, 1729,2707,2410,2376,2987,2504,3398,3387,3856,4254,4500,4678,4847,7251,5578,6361]
a = [1651,1730,1862,2383,2062,2866,2666,2561,3104,2774,3486,3402,3908,4129,4391,4407,4537,6265,5163,5676]
b = [1623,1781,1934,2251,2179,2889,2770,2696,3401,3049,3770,3554,4234,4234,4419,4484,4607,6001,5054,5584]
c = [1039,1244,1370,1456,1423,2206,2173,1790,2456,1976,2701,2177,2888,2712,3047,2929,3017,3670,3395,3624]
d = [1407,1513,1800,1788,1748,2635,2416,2135,2812,2235,2771,2488,3096,2908,3333,3148,3177,3732,3616,3800]
plt.plot(x,y,linestyle='dotted', marker = '.')
plt.plot(x,z,linestyle='dotted', marker = '.')
plt.plot(x,a,linestyle='dotted', marker = '.')
plt.plot(x,b,linestyle='dotted', marker = '.')
plt.plot(x,c,linestyle='dotted', marker = '.')
plt.plot(x,d,linestyle='dotted', marker = '.')
plt.legend(["HDB 1/2 Room","HBD 3 Room","HDB 4 Room","HBD 5 Room", "Condominium","Landed Properties"])
plt.xlabel("Year")
plt.ylabel("SGD")
plt.grid(True, linewidth=0.5)
plt.title("Government Transfers")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.annotate('Covid-19', xy=(2020, 1000), xytext=(2021, 2000), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.savefig('/Madhu-Python/Graph1.png', dpi=500)


# In[6]:


#Bargraph for HDB 1/2 Room
plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 1/2 Rooms")


# In[7]:


#Bargraph for HDB 3 Room
plt.bar(x,z)
plt.legend(["HDB 3 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 3 Rooms")


# In[10]:


#Bargraph for HDB 4 Room
plt.bar(x,a)
plt.legend(["HDB 4 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 4 Rooms")


# In[11]:


#Bargraph for HDB 5 Room
plt.bar(x,b)
plt.legend(["HDB 5 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 5 Rooms")


# In[12]:


#Bargraph for Condominiums
plt.bar(x,c)
plt.legend(["Condominium"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - Condominiums ")


# In[13]:


#Bargraph for Landed Properties
plt.bar(x,d)
plt.legend(["Landed Properties"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - Landed Properties")


# In[ ]:




