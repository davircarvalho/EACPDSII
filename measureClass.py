#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:48:23 2019

@author: mtslazarin
"""

#%% Importando bibliotecas

import pytta

import copy as cp

#%% Classe da medição

class newMeasurement():
    
    def __init__(self,
                 name,
                 device,
                 excitationSignals,
                 samplingRate,
                 freqMin,
                 freqMax,
                 inChannel,
                 inChName,
                 outChannel,
                 averages,
                 sourcesNumber,
                 receiversNumber,
                 noiseFloorTp,
                 calibrationTp):
        self.name = name
        self.device = device
        self.excitationSignals = excitationSignals
        self.samplingRate = samplingRate
        self.freqMin = freqMin
        self.freqMax= freqMax
        self.inChannel = inChannel
        self.inChName = inChName
        self.outChannel = outChannel
        self.averages = averages
        self.sourcesNumber = sourcesNumber
        self.receiversNumber = receiversNumber
        self.noiseFloorTp = noiseFloorTp
        self.calibrationTp = calibrationTp
        # Criando objetos de medição tipo pytta.PlayRecMeasure e pytta.RecMeasure
        self.measurementObjects = {'varredura' : pytta.generate.measurement('playrec',
                                                        excitation=self.excitationSignals['varredura'],
                                                        samplingRate=self.samplingRate,
                                                        freqMin=self.freqMin,
                                                        freqMax=self.freqMax,
                                                        device=self.device,
                                                        inChannel=self.inChannel,
                                                        outChannel=self.outChannel['S1'][0],
                                                        channelName=self.inChName,
                                                        comment='varredura'),
                   'musica' : pytta.generate.measurement('playrec',
                                                        excitation=self.excitationSignals['musica'],
                                                        samplingRate=self.samplingRate,
                                                        freqMin=self.freqMin,
                                                        freqMax=self.freqMax,
                                                        device=self.device,
                                                        inChannel=self.inChannel,
                                                        outChannel=self.outChannel['S1'][0],
                                                        channelName=self.inChName,
                                                        comment='musica'),
                   'fala' : pytta.generate.measurement('playrec',
                                                        excitation=self.excitationSignals['fala'],
                                                        samplingRate=self.samplingRate,
                                                        freqMin=self.freqMin,
                                                        freqMax=self.freqMax,
                                                        device=self.device,
                                                        inChannel=self.inChannel,
                                                        outChannel=self.outChannel['S1'][0],
                                                        channelName=self.inChName,
                                                        comment='fala'),
                   'noisefloor' : pytta.generate.measurement('rec',
                                                         lengthDomain='time',
                                                         timeLength=self.noiseFloorTp,
                                                         samplingRate=self.samplingRate,
                                                         freqMin=self.freqMin,
                                                         freqMax=self.freqMax,
                                                         device=self.device,
                                                         inChannel=self.inChannel,
                                                         comment='noisefloor'),
                   'calibration' : pytta.generate.measurement('rec',
                                                         lengthDomain='time',
                                                         timeLength=self.calibrationTp,
                                                         samplingRate=self.samplingRate,
                                                         freqMin=self.freqMin,
                                                         freqMax=self.freqMax,
                                                         device=self.device,
                                                         inChannel=self.inChannel,
                                                         comment='calibration')}

#%% Classe do dicionário de dados medidos
        
class Data():
    
    def __init__(self,MS):
        self.measuredData = {} # Cria o dicionário vazio que conterá todos os níveis de informação do nosso dia de medição
        for sourceCode in MS.outChannel:
            for rN in range(1,MS.receiversNumber+1):
                self.measuredData[sourceCode+'R'+str(rN)] = {} # Insere as chaves referente as configurações fonte receptor
                for key in MS.excitationSignals:
                    self.measuredData[sourceCode+'R'+str(rN)][key] = {'binaural':0,'hc':0} # Insere as chaves referentes ao sinal de excitação e tipo de gravação
        self.measuredData['noisefloor'] = [] # Cria lista de medições de ruído de fundo
        self.measuredData['calibration'] = {} # Cria dicionário com os canais de entrada da medição
        for chN in MS.inChName:
            self.measuredData['calibration'][chN] = [] # Cria uma lista de calibrações para cada canal

#%% Classe das tomadas de medição
class measureTake():
    
    def __init__(self,
                 MS,
                 kind,
                 channelStatus,
                 tempHumid,
                 source=None,
                 receiver=None,
                 excitation=None):
        self.tempHumid = tempHumid
        if self.tempHumid != None:
            self.tempHumid.start()
        self.MS = MS
        self.kind = kind
        self.channelStatus = channelStatus
        self.source = source
        self.receiver = receiver
        if excitation == None:
            self.excitation = kind
        else:
            self.excitation = excitation
        if self.kind == 'newpoint':
            if self.excitation != None and self.excitation not in self.MS.excitationSignals:
                raise ValueError('Sinal de excitação não existe em '+MS.name)            
            self.averages = MS.averages
            self.measurementObject = cp.deepcopy(MS.measurementObjects[excitation])
        if self.kind == 'calibration':            
            if self.channelStatus.count(True) != 1:
                raise ValueError('Somente 1 canal por tomada de calibração!')
            self.measurementObject = cp.deepcopy(MS.measurementObjects[kind])
            self.averages = MS.averages
        if self.kind == 'noisefloor':
            self.measurementObject = cp.deepcopy(MS.measurementObjects[kind])
            self.averages = MS.averages
        j = 1
        inChannel = []
        for i in self.channelStatus:
            if i:
                inChannel.append(j)
            j=j+1
        if kind == 'newpoint':
            self.measurementObject.outChannel = self.MS.outChannel[self.source][0]
        self.measurementObject.inChannel = inChannel # Ao redefinir a propriedade inChannelo o PyTTa já reajusta a lista channelName com os nomes antigos + nomes padrão para novos canais
        self.measurementObject.channelName = [MS.inChName[i-1] for i in inChannel] # Atribuiu os nomes corretos aos canais selecionados

    def run(self):
        self.measuredTake = []
#        if self.kind == 'newpoint':
        for i in range(0,self.averages):
            self.measuredTake.append(self.measurementObject.run())
            self.measuredTake[i].plot_time()
            # Adquire do LabJack U3 + EI1050 a temperatura e umidade relativa instantânea
            if self.tempHumid != None:
                self.measuredTake[i].temp, self.measuredTake[i].RH = self.tempHumid.read()
            else:
                self.measuredTake[i].temp, self.measuredTake[i].RH = (None,None)
            
    def save(self,dataObj):
        # Desmembra o SignalObj measureTake de 4 canais em 3 SignalObj referentes ao arranjo biauricular 
        # em uma posição e ao centro da cabeça em duas outras posições
        if self.kind == 'newpoint' or self.kind == 'noisefloor':
            chcont = 0
            self.binaural=[]
            self.hc1=[]
            self.hc2=[]
            if self.channelStatus[0] and self.channelStatus[1]:
                for i in range(0,self.averages):
                    self.binaural.append(pytta.SignalObj(self.measuredTake[i].timeSignal[:,chcont:chcont+2],
                                               'time',
                                               samplingRate=self.measuredTake[i].samplingRate,
                                               channelName=[self.MS.inChName[0],self.MS.inChName[1]],
                                               comment=self.excitation))
                    self.binaural[i].sourceReceiver = [self.source+self.receiver[0],self.source+self.receiver[1]]
                    self.binaural[i].temp = self.measuredTake[i].temp
                    self.binaural[i].RH = self.measuredTake[i].RH
                    self.binaural[i].timeStamp = self.measuredTake[i].timeStamp
                chcont = chcont + 2
            if self.channelStatus[2]:
                for i in range(0,self.averages):
                    self.hc1.append(pytta.SignalObj(self.measuredTake[i].timeSignal[:,chcont],
                                          'time',
                                          samplingRate=self.measuredTake[i].samplingRate,
                                          channelName=[self.MS.inChName[2]],
                                          comment=self.excitation))
                    self.hc1[i].sourceReceiver = self.source+self.receiver[2]
                    self.hc1[i].temp = self.measuredTake[i].temp
                    self.hc1[i].RH = self.measuredTake[i].RH
                    self.hc1[i].timeStamp = self.measuredTake[i].timeStamp
                chcont = chcont + 1
            if self.channelStatus[3]:
                for i in range(0,self.averages):
                    self.hc2.append(pytta.SignalObj(self.measuredTake[i].timeSignal[:,chcont],
                                          'time',
                                          samplingRate=self.measuredTake[i].samplingRate,
                                          channelName=[self.MS.inChName[3]],
                                          comment=self.excitation))
                    self.hc2[i].sourceReceiver = self.source+self.receiver[3]
                    self.hc2[i].temp = self.measuredTake[i].temp
                    self.hc2[i].RH = self.measuredTake[i].RH
                    self.hc2[i].timeStamp = self.measuredTake[i].timeStamp        

        # Salva dados no dicionário do objeto de dados dataObj
        if self.kind == 'newpoint':
            # Adiciona cada uma das três posições de receptor da última tomada de medição     
            if self.channelStatus[0] and self.channelStatus[1]:
                dataObj.measuredData[self.binaural[0].sourceReceiver[0]][self.binaural[0].comment]['binaural'] = self.binaural
            if self.channelStatus[2]:
                dataObj.measuredData[self.hc1[0].sourceReceiver][self.hc1[0].comment]['hc'] = self.hc1
            if self.channelStatus[3]:
                dataObj.measuredData[self.hc2[0].sourceReceiver][self.hc2[0].comment]['hc'] = self.hc2
                
        if self.kind == 'noisefloor':
            newNF = {}
            if self.channelStatus[0] and self.channelStatus[1]:
                newNF[self.binaural[0].sourceReceiver[0]] = self.binaural
            if self.channelStatus[2]:
                newNF[self.hc1[0].sourceReceiver] = self.hc1
            if self.channelStatus[3]:
                newNF[self.hc2[0].sourceReceiver] = self.hc2
            dataObj.measuredData['noisefloor'].append(newNF)
            
        if self.kind == 'calibration':
            self.calibAverages = []
            # Pegando o nome do canal calibrado
            j=0
            for i in self.channelStatus:
                if i:
                    self.inChName = [self.MS.inChName[j]]
                j=j+1
            for i in range(0,self.averages):
                self.calibAverages.append(pytta.SignalObj(self.measuredTake[i].timeSignal[:,0],
                                      'time',
                                      samplingRate=self.measuredTake[i].samplingRate,
                                      channelName=self.inChName,
                                      comment=self.excitation))
#                self.calibAverages[i].sourceReceiver = self.sourceReceiver[2]
                self.calibAverages[i].temp = self.measuredTake[i].temp
                self.calibAverages[i].RH = self.measuredTake[i].RH
                self.calibAverages[i].timeStamp = self.measuredTake[i].timeStamp
            dataObj.measuredData['calibration'][self.inChName[0]].append(self.calibAverages)
        if self.tempHumid != None:
            self.tempHumid.stop()