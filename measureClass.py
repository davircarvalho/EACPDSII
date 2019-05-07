#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:48:23 2019

@author: mtslazarin
"""

#%% Importando bibliotecas

import pytta
import numpy as np
import copy as cp
import time
import pickle

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

#    def exportDict(self):
#       expdic = vars(self)
#       for key, value in expdic.items():
#           if isinstance(value,pytta.classes.SignalObj):
#               expdic[key] = vars(value)
#           elif isinstance(value,dict):
#               newdict = {}
#               for key2, value2 in value.items():
#                   if isinstance(value2,pytta.classes.SignalObj):
#                       newdict[key2] = vars(value2)
#                   else:
#                       newdict[key2] = value2
#               expdic[key] = newdict
#       return expdic
                   
    def exportDict(self):
       expdic = vars(self)
       
       def toDict(thing):
           if isinstance(thing,pytta.classes.SignalObj):
               mySigObj = vars(thing)
               for key, value in mySigObj.items():
                   if value is None:
                       mySigObj[key] = 0
                   if isinstance(mySigObj[key],dict) and len(value) == 0:
                       mySigObj[key] = 0
               mySigObjno_ = {}
               for key, value in mySigObj.items():
                   if key.find('_') >= 0:
                       key = key.replace('_','')
                   mySigObjno_[key] = value
                   
               return mySigObjno_
           
           elif isinstance(thing,dict):
               dictime = {}
               for key, value in thing.items():
                   if key.find(' ') >= 0:
                       key = key.replace(' ','')
                   dictime[key] = toDict(value)
               return dictime
           
           elif isinstance(thing,list):
               dictime = {}
               j = 0
               for item in thing:
                   dictime['T'+str(j)] = toDict(item)
                   j=j+1
               return dictime
           
           elif thing is None:
               return 0
           
           elif isinstance(thing,newMeasurement):
               return 0
           
           else:
               return thing
           
       return toDict(expdic)

#%% Classe do dicionário de dados medidos
        
class Data():
    
    def __init__(self,MS):
        self.MS = MS
        self.measuredData = {} # Cria o dicionário vazio que conterá todos os níveis de informação do nosso dia de medição
        self.status = {} # Cria o dicionário vazio que conterá o status de cada ponto de medição
        # Gerando chaves para configurações fonte-receptor
        for sourceCode in self.MS.outChannel:
            for rN in range(1,self.MS.receiversNumber+1):
                self.measuredData[sourceCode+'R'+str(rN)] = {} # Insere as chaves referente as configurações fonte receptor
                self.status[sourceCode+'R'+str(rN)] = {}
                for key in MS.excitationSignals:
                    self.measuredData[sourceCode+'R'+str(rN)][key] = {'binaural':0,'hc':0} # Insere as chaves referentes ao sinal de excitação e tipo de gravação            
                    self.status[sourceCode+'R'+str(rN)][key] = {'binaural':False,'hc':False}
        self.measuredData['noisefloor'] = [] # Cria lista de medições de ruído de fundo
        self.status['noisefloor'] = False
        self.measuredData['calibration'] = {} # Cria dicionário com os canais de entrada da medição
        self.status['calibration'] = {}
        for chN in self.MS.inChName:
            self.measuredData['calibration'][chN] = [] # Cria uma lista de calibrações para cada canal
            self.status['calibration'][chN] = False
            
    def dummyFill(self):
        # Preenche o dicionário de dados medidos com sinais nulos.
        dummyFill = cp.deepcopy(self.MS.excitationSignals)
        for key in dummyFill:
            dummyFill[key].timeSignal = dummyFill[key].timeSignal*0
        dummyFill['noisefloor'] = pytta.SignalObj(np.zeros(self.MS.noiseFloorTp*self.MS.samplingRate),domain='time',samplingRate=self.MS.samplingRate)
        dummyFill['calibration'] = pytta.SignalObj(np.zeros(self.MS.calibrationTp*self.MS.samplingRate),domain='time',samplingRate=self.MS.samplingRate) 
        for sourceCode in self.MS.outChannel:
            for rN in range(1,self.MS.receiversNumber+1):
#                self.measuredData[sourceCode+'R'+str(rN)] = {} # Insere as chaves referente as configurações fonte receptor
                for key in self.MS.excitationSignals:
                    self.measuredData[sourceCode+'R'+str(rN)][key] = {'binaural':cp.deepcopy([dummyFill[key],dummyFill[key],dummyFill[key]]),'hc':cp.deepcopy([dummyFill[key],dummyFill[key],dummyFill[key]])} # Insere as chaves referentes ao sinal de excitação e tipo de gravação
                    self.status[sourceCode+'R'+str(rN)][key] = {'binaural':True,'hc':True} # Insere as chaves referentes ao sinal de excitação e tipo de gravação
        self.measuredData['noisefloor'] = cp.deepcopy([[dummyFill['noisefloor'],dummyFill['noisefloor'],dummyFill['noisefloor']],[dummyFill['noisefloor'],dummyFill['noisefloor'],dummyFill['noisefloor']]]) # Cria lista de medições de ruído de fundo
        self.status['noisefloor'] = True # Cria lista de medições de ruído de fundo
        self.measuredData['calibration'] = {} # Cria dicionário com os canais de entrada da medição
        for chN in self.MS.inChName:
            self.measuredData['calibration'][chN] = cp.deepcopy([[dummyFill['calibration'],dummyFill['calibration'],dummyFill['calibration']],[dummyFill['calibration'],dummyFill['calibration'],dummyFill['calibration']]]) # Cria uma lista de calibrações para cada canal
            self.status['calibration'][chN] = True
            
    def getStatus(self):
        statusStr = ''
        cEnd = '\x1b[0m'
        cHeader = '\x1b[1;35;43m'
        cHeader2 = '\x1b[1;30;43m'
        cAll = '\x1b[0;30;46m'
        cTrue = '\x1b[3;30;42m'
        cFalse = '\x1b[3;30;41m'
        
#        cEnd = ''
#        cHeader = ''
#        cHeader2 = ''
#        cAll = ''
#        cTrue = ''
#        cFalse = ''
        
        for key in self.status:
            statusStr = statusStr+cHeader+'            '+key+'            '+cEnd+'\n'
            if key == 'noisefloor':
                if self.status[key]:
                    cNF = cTrue
                else:
                    cNF = cFalse
                statusStr = statusStr+''+cNF+str(self.status[key])+cEnd+'\n'
            elif key == 'calibration':
                for ch in self.status[key]:
                    if self.status[key][ch]:
                        cCal = cTrue
                    else:
                        cCal = cFalse
                    statusStr = statusStr+cAll+ch+':'+cEnd+' '+cCal+str(self.status[key][ch])+cEnd+'\n'
#                statusStr = statusStr+'\n'
            else:
                for sig in self.status[key]:
                    statusStr = statusStr+cHeader2+sig+'\n'+cEnd
                    if self.status[key][sig]['binaural']:
                        cBin = cTrue
                    else:
                        cBin = cFalse
                    if self.status[key][sig]['hc']:
                        cHc = cTrue
                    else:
                        cHc = cFalse
                    statusStr = statusStr+cAll+'binaural:'+cEnd+' '+cBin+str(self.status[key][sig]['binaural'])+cEnd+' '
                    statusStr = statusStr+cAll+'h.c.:'+cEnd+' '+cHc+str(self.status[key][sig]['hc'])+cEnd+'\n'
#                statusStr = statusStr+'\n'
#            statusStr = statusStr+'______________________________\n'
                
#        return print(statusStr)
        return statusStr
    
    def exportDict(self):
       expdic = vars(self)
       
       def toDict(thing):
           if isinstance(thing,pytta.classes.SignalObj):
               mySigObj = vars(thing)
               for key, value in mySigObj.items():
                   if value is None:
                       mySigObj[key] = 0
                   if isinstance(mySigObj[key],dict) and len(value) == 0:
                       mySigObj[key] = 0
               mySigObjno_ = {}
               for key, value in mySigObj.items():
                   if key.find('_') >= 0:
                       key = key.replace('_','')
                   mySigObjno_[key] = value
                   
               return mySigObjno_
           
           elif isinstance(thing,dict):
               dictime = {}
               for key, value in thing.items():
                   if key.find(' ') >= 0:
                       key = key.replace(' ','')
                   dictime[key] = toDict(value)
               return dictime
           
           elif isinstance(thing,list):
               dictime = {}
               j = 0
               for item in thing:
                   dictime['T'+str(j)] = toDict(item)
                   j=j+1
               return dictime
           
           elif thing is None:
               return 0
           
           elif isinstance(thing,newMeasurement):
               return 0
           
           else:
               return thing
           
       return toDict(expdic)
   
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
        j = 0
        inChannel = []
        channelName = []
        for i in self.channelStatus:
            if i:
                inChannel.append(self.MS.inChannel[j])
                channelName.append(self.MS.inChName[j])
            j=j+1
        if kind == 'newpoint':
            self.measurementObject.outChannel = self.MS.outChannel[self.source][0]
        self.measurementObject.inChannel = inChannel # Ao redefinir a propriedade inChannelo o PyTTa já reajusta a lista channelName com os nomes antigos + nomes padrão para novos canais
        self.measurementObject.channelName = channelName # Atribuiu os nomes corretos aos canais selecionados

    def run(self):
        self.measuredTake = []
#        if self.kind == 'newpoint':
        for i in range(0,self.averages):
            self.measuredTake.append(self.measurementObject.run())
#            self.measuredTake[i].plot_time()
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
                    if self.kind == 'noisefloor': 
                        SR = [self.receiver[0],self.receiver[1]] 
                    else: 
                        SR = [self.source+self.receiver[0],self.source+self.receiver[1]]
                    self.binaural[i].sourceReceiver = SR
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
                    if self.kind == 'noisefloor': 
                        SR = self.receiver[2]
                    else: 
                        SR = self.source+self.receiver[2]
                    self.hc1[i].sourceReceiver = SR
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
                    if self.kind == 'noisefloor': 
                        SR = self.receiver[3]
                    else: 
                        SR = self.source+self.receiver[3]
                    self.hc2[i].sourceReceiver = SR
                    self.hc2[i].temp = self.measuredTake[i].temp
                    self.hc2[i].RH = self.measuredTake[i].RH
                    self.hc2[i].timeStamp = self.measuredTake[i].timeStamp        

        # Salva dados no dicionário do objeto de dados dataObj
        if self.kind == 'newpoint':
            # Adiciona cada uma das três posições de receptor da última tomada de medição     
            if self.channelStatus[0] and self.channelStatus[1]:
                dataObj.measuredData[self.binaural[0].sourceReceiver[0]][self.binaural[0].comment]['binaural'] = self.binaural
                dataObj.status[self.binaural[0].sourceReceiver[0]][self.binaural[0].comment]['binaural'] = True
            if self.channelStatus[2]:
                dataObj.measuredData[self.hc1[0].sourceReceiver][self.hc1[0].comment]['hc'] = self.hc1
                dataObj.status[self.hc1[0].sourceReceiver][self.hc1[0].comment]['hc'] = True
            if self.channelStatus[3]:
                dataObj.measuredData[self.hc2[0].sourceReceiver][self.hc2[0].comment]['hc'] = self.hc2
                dataObj.status[self.hc2[0].sourceReceiver][self.hc2[0].comment]['hc'] = True
                
        if self.kind == 'noisefloor':
            newNF = {}
            if self.channelStatus[0] and self.channelStatus[1]:
                newNF[self.binaural[0].sourceReceiver[0]] = self.binaural
            if self.channelStatus[2]:
                newNF[self.hc1[0].sourceReceiver] = self.hc1
            if self.channelStatus[3]:
                newNF[self.hc2[0].sourceReceiver] = self.hc2
            dataObj.measuredData['noisefloor'].append(newNF)
            dataObj.status['noisefloor'] = True
            
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
            dataObj.status['calibration'][self.inChName[0]] = True
        if self.tempHumid != None:
            self.tempHumid.stop()
    
def save(MS,D,filename):
    timeStamp = time.ctime(time.time())
    msD = {'averages':MS.averages,
           'calibrationTp':MS.calibrationTp,
           'device':MS.device,
           'excitationSignals':MS.excitationSignals,
           'freqMax':MS.freqMax,
           'freqMin':MS.freqMin,
           'inChName':MS.inChName,
           'inChannel':MS.inChannel,
           'measurementObjects':MS.measurementObjects,
           'name':MS.name,
           'noiseFloorTp':MS.noiseFloorTp,
           'outChannel':MS.outChannel,
           'receiversNumber':MS.receiversNumber,
           'samplingRate':MS.samplingRate,
           'sourcesNumber':MS.sourcesNumber}
    dD = {'measuredData':D.measuredData,
          'status':D.status}
    saveDict = {'MS':msD,'Data':dD,'Timestamp':timeStamp}
    # write python dict to a file
    output = open(filename+'.pkl', 'wb')
    pickle.dump(saveDict,output)
    output.close()
    
def load(filename):
    #%% read python dict back from the file
    pkl_file = open(filename+'.pkl', 'rb')
    loadDict = pickle.load(pkl_file)
    pkl_file.close()            
    MS = newMeasurement(averages = loadDict['MS']['averages'],
                        calibrationTp = loadDict['MS']['calibrationTp'],
                        device = loadDict['MS']['device'],
                        excitationSignals = loadDict['MS']['excitationSignals'],
                        freqMax = loadDict['MS']['freqMax'],
                        freqMin = loadDict['MS']['freqMin'],
                        inChName = loadDict['MS']['inChName'],
                        inChannel = loadDict['MS']['inChannel'],
                        name = loadDict['MS']['name'],
                        noiseFloorTp = loadDict['MS']['noiseFloorTp'],
                        outChannel = loadDict['MS']['outChannel'],
                        receiversNumber = loadDict['MS']['receiversNumber'],
                        samplingRate = loadDict['MS']['samplingRate'],
                        sourcesNumber = loadDict['MS']['sourcesNumber'])    
    MS.measurementObjects = loadDict['MS']['measurementObjects']
    D = Data(MS)
    D.measuredData = loadDict['Data']['measuredData']
    D.status = loadDict['Data']['status']
    return MS, D