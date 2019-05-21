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
import copy as cp

#%%
medName = 'med-sala_conselhos'

#%%
m.med_to_mat(medName)
#%%
SM,D = m.load(medName)
#%%
calibSig = cp.deepcopy(D.measuredData['calibration']['Orelha E'][0][0])
calibSig.plot_freq()
#%%
calibdSig = cp.deepcopy(calibSig)
calibdSig.calib_pressure(0,calibSig,1,1000)
calibdSig.plot_freq()

#%% 
Ddict = D.exportDict()
SMdict = SM.exportDict()

#%%
io.savemat(medName+'.mat',{'MeasurementSetup':SMdict,'Data':Ddict})