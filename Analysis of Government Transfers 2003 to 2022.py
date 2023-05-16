#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


from matplotlib import pyplot as plt


# In[117]:


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


# In[149]:


import numpy as np
from sklearn.datasets import make_regression

x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
y= [3314, 3124, 3879, 4769, 3850, 5792, 5711, 6559, 7632, 7212, 8845, 9324, 9480, 10067, 10425, 10539, 10675, 13824, 11530, 12189]
plt.scatter(x,y,linestyle='dotted', marker = '.')
plt.legend(["HDB 1/2 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")

coefficients = np.polyfit(x, y, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[145]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
z = [1386, 1456, 1565,2221, 1729,2707,2410,2376,2987,2504,3398,3387,3856,4254,4500,4678,4847,7251,5578,6361]
plt.scatter(x,z,linestyle='dotted', marker = '.')
plt.legend(["HDB 3 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")

from sklearn.linear_model import LinearRegression

coefficients = np.polyfit(x, z, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[144]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
a = [1651,1730,1862,2383,2062,2866,2666,2561,3104,2774,3486,3402,3908,4129,4391,4407,4537,6265,5163,5676]
plt.scatter(x,a,linestyle='dotted', marker = '.')
plt.legend(["HDB 4 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")

from sklearn.linear_model import LinearRegression

coefficients = np.polyfit(x, a, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[135]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
b = [1623,1781,1934,2251,2179,2889,2770,2696,3401,3049,3770,3554,4234,4234,4419,4484,4607,6001,5054,5584]
plt.scatter(x,b,linestyle='dotted', marker = '.')
plt.legend(["HDB 5 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")

from sklearn.linear_model import LinearRegression

coefficients = np.polyfit(x, b, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[141]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
c = [1039,1244,1370,1456,1423,2206,2173,1790,2456,1976,2701,2177,2888,2712,3047,2929,3017,3670,3395,3624]
plt.scatter(x,c,linestyle='dotted', marker = '.')
plt.legend(["Condominium"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")
from sklearn.linear_model import LinearRegression

coefficients = np.polyfit(x, c, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[142]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
d = [1407,1513,1800,1788,1748,2635,2416,2135,2812,2235,2771,2488,3096,2908,3333,3148,3177,3732,3616,3800]
plt.scatter(x,d,linestyle='dotted', marker = '.')
plt.legend(["Landed Properties"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("ScatterPlot - Government Transfers")
from sklearn.linear_model import LinearRegression

coefficients = np.polyfit(x, d, 1)
regression_line = np.polyval(coefficients, x)

# Plot the regression line
plt.plot(x, regression_line, color='red')

plt.show()


# In[87]:


plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 1/2 Rooms")


# In[155]:


plt.bar(x,z)
plt.legend(["HDB 3 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 3 Rooms")


# In[156]:


plt.bar(x,y)
plt.legend(["HDB 4 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 4 Rooms")


# In[157]:


plt.bar(x,a)
plt.legend(["HDB 5 Room"])
plt.xlabel("Year")
plt.ylabel("SGD")
x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)
plt.title("Government Transfers - HDB 5 Rooms")


# In[120]:


x = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
c = [1039,1244,1370,1456,1423,2206,2173,1790,2456,1976,2701,2177,2888,2712,3047,2929,3017,3670,3395,3624]
d = [1407,1513,1800,1788,1748,2635,2416,2135,2812,2235,2771,2488,3096,2908,3333,3148,3177,3732,3616,3800]
plt.bar([a-0.25 for a in x],c,width=0.25,align='center')
plt.bar([a+0.25 for a in x],d,width=0.25,align='center')

x_ticks = np.arange(2000, 2025, 5)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.legend(["Condominiums", "Landed Properties"])
plt.xlabel("Year")
plt.ylabel("SGD")
plt.title("Comparision of Government Transfers: Condominiums and Landed Properties")
plt.style.use('seaborn')
plt.show()


# In[ ]:





# In[113]:


labels = ['HDB 1/2 Room', 'HDB 3 Room', 'HDB 4 Room', 'HDB 5 Room', 'Condominiums', 'Landed Properties']
views = [12189,6361,5676,5584,3624,3800]

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.5})

plt.title('Proportion of Government Transfer 2022')
plt.axis('equal') 
plt.show()


# In[151]:


labels = ['HDB 1/2 Room', 'HDB 3 Room', 'HDB 4 Room', 'HDB 5 Room', 'Condominiums', 'Landed Properties']
views = [7212,2504,2774,3049,1976,2235]

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.5})

plt.title('Proportion of Government Transfer 2012')
plt.axis('equal') 
plt.show()


# In[ ]:




