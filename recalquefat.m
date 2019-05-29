%% CALCULO DO FATOR DE CALIBRAÇÃO
% Sidney Volney Cândido 27/05
% Calcula fator de correção para ser carregado na função de aplicação na
% medição do trabalho integrado
function [fat cor] = recalquefat(pcalib)
% load('calib_pressao.mat');
% Fator de calibração
calib.Pref = 1; calib.dBRef = 2e-5;
calib_pressao = pcalib;
%
sinal.ita = itaAudio(calib_pressao, 44100, 'time');
sinal.ita.channelUnits = {'Pa'};
% % Método via Pico
% med = abs(max(sinal.ita.freq));
% fat = calib.Pref/med;
% cor = sinal.ita*fat;
WF.bla = fdesign.bandpass('N,F3dB1,F3dB2', 4, 990, 1010, 44100);
WF.oi = design(WF.bla,'butter');
WF.janelado = filter(WF.oi,calib_pressao);
WF.janelado2 = itaAudio(WF.janelado, 44100, 'time');
% Método via Pico JANELADO
med = abs(max(sinal.ita.freq));
fat = calib.Pref/med;
cor = sinal.ita*fat;