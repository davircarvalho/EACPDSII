%% CALCULO DO FATOR DE CALIBRA��O
% Sidney Volney C�ndido 27/05
% Calcula fator de corre��o para ser carregado na fun��o de aplica��o na
% medi��o do trabalho integrado
function [fat cor] = recalquefat(pcalib)
% load('calib_pressao.mat');
% Fator de calibra��o
calib.Pref = 1; calib.dBRef = 2e-5;
calib_pressao = pcalib;
%
sinal.ita = itaAudio(calib_pressao, 44100, 'time');
sinal.ita.channelUnits = {'Pa'};
% % M�todo via Pico
% med = abs(max(sinal.ita.freq));
% fat = calib.Pref/med;
% cor = sinal.ita*fat;
WF.bla = fdesign.bandpass('N,F3dB1,F3dB2', 4, 990, 1010, 44100);
WF.oi = design(WF.bla,'butter');
WF.janelado = filter(WF.oi,calib_pressao);
WF.janelado2 = itaAudio(WF.janelado, 44100, 'time');
% M�todo via Pico JANELADO
med = abs(max(sinal.ita.freq));
fat = calib.Pref/med;
cor = sinal.ita*fat;