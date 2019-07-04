# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:40:16 2019

@author: AKINSOJI
"""

import scipy as stat
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
d1 = np.random.randn(1000)
d3= d1*2
plt.subplot(231)
plt.hist(d1)
plt.savefig('image-d1-histogram')
plt.xlabel('range of d1')
plt.ylabel('set of value')

plt.subplot(233)
d2= np.random.randn(100)
plt.savefig('image-d2-histogram')
plt.hist(d2)

plt.subplot(234)
plt.savefig('image-2d-histogram')
plt.hist2d(d1,d3)

plt.subplot(236)
plt.hist(d1,color='green',alpha=0.6)
plt.hist(d2)
plt.savefig('image-combine-histogram')


#====================================================================================================
#using seaborn function to plot histogram
#=======================================================================================================
a1=np.random.randn(1000)
a2=np.random.randn(1000)
a= sns.jointplot(d1,a2)
a.savefig('image-histogram-seaborn-1')


a= sns.jointplot(d1,a1,kind='hex',color='purple')
a.savefig('image-histogram-seaborn-2')