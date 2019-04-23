#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:19:49 2019

@author: mtslazarin
"""

import measureClass as m
import pytta
from scipy import io

#%% Carrega sinais de excitação
excitationSignals = {}
excitationSignals['varredura'] = pytta.generate.sweep(freqMin=20, # Geração do sweep (também pode ser carregado projeto prévio)
                            freqMax=20000,
                            fftDegree=17,
                            startMargin=1,
                            stopMargin=1.5,
                            method='logarithmic',
                            windowing='hann')
excitationSignals['musica'] = pytta.read_wav('Piano Over the rainbow Mic2 SHORT.wav') # Carregando sinal de música
excitationSignals['fala'] = pytta.read_wav('Voice Sabine Short.WAV') # Carregando sinal de fala

#%% Cria novo Setup de Medição
SM = m.newMeasurement(name = 'Medição teste', # Nome da medição
#                      Sintaxe : device = [<entrada>,<saida>] ou <entrada/saida>
#                      Utilize pytta.list_devices() para listar os dispositivos do seu computador. 
#                     device = [0,1], # PC laza Seleciona dispositivo listado em pytta.list_devices()
                     device = 4, # Saffire Pro 40 laza Seleciona dispositivo listado em pytta.list_devices()
#                     device = 0, # Firebox laza Seleciona dispositivo listado em pytta.list_devices()
                     excitationSignals=excitationSignals, # Sinais de excitação
                     samplingRate = 44100, # [Hz]
                     freqMin = 20, # [Hz]
                     freqMax = 20000, # [Hz]
                     inChannel = [1,2,3,4], # Canais de entrada
                     channelName = ['Orelha E','Orelha D','Mic 1','Mic 2'], # Lista com o nome dos canais 
                     outChannel = [1,2], # Canais de saída
                     averages = 3, # Número de médias por medição (FALTA IMPLEMENTAR)
                     sourcesNumber = 2, # Número de fontes; dodecaedro e p.a. local
                     receiversNumber = 5, # Número de receptores
                     noiseFloorTp = 30, # [s] tempo de gravação do ruído de fundo
                     calibrationTp = 10) # [s] tempo de gravação do sinal de calibração

#%% Cria instância de dados medidos
D = m.Data(SM)

#%% Cria nova tomada de medição
measureTake = m.measureTake(SM,
                            kind = 'newpoint',
#                            kind = 'noisefloor', # FALTA IMPLEMENTAR
#                            kind = 'calibration', # FALTA IMPLEMENTAR
                            # Status do canal: True para Ativado e False para Desativado
                            channelStatus = [True, # canal 1
                                             True, # canal 2
                                             True, # canal 3
                                             True], # canal 4
                            # Configuração fonte receptor
                            # Obs. 1: manter itens para canais Desativados
                            # Obs. 2: para kind = 'calibration'
                            sourceReceiver = ['S1R2', # canal 1 (ATENÇÃO: canal 1 e 2 tem a mesma cfg.)
                                              'S1R2', # canal 2 (ATENÇÃO: canal 1 e 2 tem a mesma cfg.)
                                              'S1R5', # canal 3 
                                              'S1R4'], # canal 4
                            excitation = 'varredura') # escolhe sinal de excitacão  disponível no Setup de Medição
#%% Nova tomada de medição
measureTake.run()

#%% Salva tomada de medição no objeto de dados D
io.savemat('Medicao_teste', {'MeasurementData1':measureTake.save(D)})

#%% Para carregar arquivos medidos
io.loadmat('Medicao_teste.mat')