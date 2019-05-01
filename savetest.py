#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:53:20 2019

@author: mtslazarin
"""

#%%
import pickle

#%% write python dict to a file
output = open('myfile.pkl', 'wb')
pickle.dump(D.measuredData, output)
output.close()

#%% read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()