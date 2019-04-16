#!/usr/bin/env python
# coding: utf-8

# # UFSM
# ## Engenharia Acústica 
# ## Processamento Digital de Sinais II
# ### Trabalho Integrado: rotina de medição

#%% Importando bibliotecas

# Carregando as bibliotecas que utilizaremos
import pytta

#%% Configuração da medição

# Dados
#device = [0,1] PC laza # Seleciona dispositivo listado em pytta.list_devices()
#device = 4 # Saffire Pro 40 laza Seleciona dispositivo listado em pytta.list_devices()
device = 0 # Firebox laza Seleciona dispositivo listado em pytta.list_devices()
samplingRate = 44100 # [Hz]
freqMin = 20 # [Hz]
freqMax = 20000 # [Hz]
inChannel = [1,2,3,4] # Canais de entrada
channelName = ['Orelha E','Orelha D','Mic 1','Mic 2'] # Lista com o nome dos canais 
outChannel = [1,2] # Canais de saída
averages = 1 # Número de médias por medição (FALTA IMPLEMENTAR NO PYTTA)
sourcesNumber = 2 # Número de fontes; dodecaedro e p.a. local
receiversNumber = 5 # Número de receptores

# Sinais de excitação
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

# Criando objetos de medição
playRec = {'varredura' : pytta.generate.measurement('playrec',
                                                excitation=excitationSignals['varredura'],
                                                averages=averages,
                                                samplingRate=samplingRate,
                                                freqMin=freqMin,
                                                freqMax=freqMax,
                                                device=device,
                                                inChannel=inChannel,
                                                outChannel=outChannel,
                                                channelName=channelName,
                                                comment='varredura'),
           'musica' : pytta.generate.measurement('playrec',
                                                excitation=excitationSignals['musica'],
                                                averages=averages,
                                                samplingRate=samplingRate,
                                                freqMin=freqMin,
                                                freqMax=freqMax,
                                                device=device,
                                                inChannel=inChannel,
                                                outChannel=outChannel,
                                                channelName=channelName,
                                                comment='musica'),
           'fala' : pytta.generate.measurement('playrec',
                                                excitation=excitationSignals['fala'],
                                                averages=averages,
                                                samplingRate=samplingRate,
                                                freqMin=freqMin,
                                                freqMax=freqMax,
                                                device=device,
                                                inChannel=inChannel,
                                                outChannel=outChannel,
                                                channelName=channelName,
                                                comment='fala')}

#%% Criando dicionário de dados medidos
           
measurementData = {} # Cria o dicionário vazio que conterá todos os níveis de informação do nosso dia de medição
for sN in range(1,sourcesNumber+1):
    for rN in range(1,receiversNumber+1):
        measurementData['S'+str(sN)+'R'+str(rN)] = {} # Insere as chaves referente as configurações fonte receptor
        for key in excitationSignals:
            measurementData['S'+str(sN)+'R'+str(rN)][key] = {'binaural':None,'hc':None} # Insere as chaves referentes ao sinal de excitação e tipo de gravação

#%% Fake measureTake
            
# Load de sinal de áudio qualquer para demonstração do código
dummySignal = pytta.read_wav('Piano Over the rainbow Mic2 SHORT.wav')   

# Cria signalObj de 4 canais como seria numa tomada da medição
merge1 = pytta.merge(dummySignal,dummySignal)
measureTake_fake = pytta.merge(merge1,merge1)
measureTake_fake.channelName = channelName
measureTake_fake.comment = 'music'
measureTake_fake.sourceReceiver = ['S1R1','S1R1','S1R2','S1R3']
measureTake_fake.temp = 24.666
measureTake_fake.RH = 69

# measureTake = measureTake_fake

#%% Nova tomada da medição
#%% Opções de nova tomada da medição

# Status do canal: True para ligado e False para desligado
channelStatus = [True, # canal 1
                 True, # canal 2
                 True, # canal 3
                 True] # canal 4

# Configuração fonte receptor
# Obs.: manter itens para canais desativados
sourceReceiver = ['S1R1', # canal 1 (ATENÇÃO: canal 1 e 2 tem a mesma cfg.)
                  'S1R1', # canal 2 (ATENÇÃO: canal 1 e 2 tem a mesma cfg.)
                  'S1R2', # canal 3 
                  'S1R3'] # canal 4

excitation = 'varredura'
#excitation = 'musica'
#excitation = 'fala'


#%% Aplicando opções
#%% Redefinindo lista inChannel

j = 1
inChannel = []
for i in channelStatus:
    if i:
        inChannel.append(j)
    j=j+1
playRec[excitation].inChannel = inChannel # Ao redefinir a propriedade inChannelo o PyTTa já reajusto a lista channelName
playRec[excitation].channelName = [channelName[i-1] for i in inChannel]

#%% Medindo

measureTake = playRec[excitation].run()
measureTake.plot_time()
measureTake.temp = 24 # FALTA INTEGRAR LABJACK
measureTake.RH = 69 # FALTA INTEGRAR LABJACK

#%% Armazenamento da última tomada da medição
#%% Prepara última tomada da medição para armazenamento no dicionário de dados medidos

# Desmembra o SignalObj measureTake de 4 canais em 3 SignalObj referentes ao arranjo biauricular 
# em uma posição e ao centro da cabeça em duas outras posições
chcont = 0
if channelStatus[0] and channelStatus[1]:
    binaural = pytta.SignalObj(measureTake.timeSignal[:,chcont:chcont+2],
                               'time',
                               samplingRate=measureTake.samplingRate,
                               channelName=[channelName[0],channelName[1]],
                               comment=excitation)
    binaural.sourceReceiver = [sourceReceiver[0],sourceReceiver[1]]
    binaural.temp = measureTake.temp
    binaural.RH = measureTake.RH
    chcont = chcont + 2
if channelStatus[2]:
    hc1 = pytta.SignalObj(measureTake.timeSignal[:,chcont],
                          'time',
                          samplingRate=measureTake.samplingRate,
                          channelName=[channelName[2]],
                          comment=excitation)
    hc1.sourceReceiver = sourceReceiver[2]
    hc1.temp = measureTake.temp
    hc1.RH = measureTake.RH
    chcont = chcont + 1
if channelStatus[3]:
    hc2 = pytta.SignalObj(measureTake.timeSignal[:,chcont],
                          'time',
                          samplingRate=measureTake.samplingRate,
                          channelName=[channelName[3]],
                          comment=excitation)
    hc2.sourceReceiver = sourceReceiver[3]
    hc2.temp = measureTake.temp
    hc2.RH = measureTake.RH

# Neste ponto já teríamos tomado uma medição e desmembrado o SignalObj resultante em 3 novos SignalObj, sendo um 
# para o microfone biauricular e dois para os microfones de centro da cabeça.

#%% Adicionando tomada de medição no dicionário de dados medidos
    
# Adiciona cada uma das três posições de receptor da última tomada de medição     
if channelStatus[0] and channelStatus[1]:
    measurementData[binaural.sourceReceiver[0]][binaural.comment]['binaural'] = binaural
if channelStatus[2]:
    measurementData[hc1.sourceReceiver][hc1.comment]['hc'] = hc1
if channelStatus[3]:
    measurementData[hc2.sourceReceiver][hc2.comment]['hc'] = hc2


#%% Acessando dados no dicionário de dados medidos

#measurementData['S1R1']['sweep']['binaural'].play()a