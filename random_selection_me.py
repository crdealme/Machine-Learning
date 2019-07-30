# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:51:58 2019

@author: crdea
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range (0,N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward + reward
    
plt.hist(ads_selected)
plt.title('Histogram of ads selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()