#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:22:24 2019

@author: mtslazarin
"""
#%%
import measureClass as m
from scipy import io

#%%
medName = 'med_hardware-test-lab'

#%%
SM, D = m.load(medName)

#%% PÓS PROCESSAMENTO AQUI

#%% 
Ddict = D.exportDict()
SMdict = SM.exportDict()

#%%
io.savemat(medName+'.mat',{'MeasurementSetup':SMdict,'Data':Ddict})