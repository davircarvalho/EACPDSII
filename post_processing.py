#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:22:24 2019

@author: mtslazarin
"""
#%%
import measureClass as m
from scipy import io
import numpy as np
import pytta

#%%
medName = 'med_hardware-test-lab'

#%%
SM, D = m.load(medName)

#%%
calibSig = D.measuredData['calibration']['Mic 1'][0][0]
calibSig.calib_pressure(calibSig,1,1000)
calibSig.plot_freq()

#%% 
Ddict = D.exportDict()
SMdict = SM.exportDict()

#%%
io.savemat(medName+'.mat',{'MeasurementSetup':SMdict,'Data':Ddict},format='5')