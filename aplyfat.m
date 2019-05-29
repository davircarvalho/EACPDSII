%% Sidney Volney Cândido 28/05
% Sub-rotina de aplicação de fator de calibração
% Essa sub-rotina faz parte do processamento dos dados da medição na sala
% de conselhos, especificamente. Foram utilizados 4 microfones, devidamente
% calibrados. Utilizando a sub-rotina recalquefat.m, essa rotina pega o
% fator de calibração e adiciona em CADA MEDIÇÃO
% SERÁ ENTRE UM STRUCT COM:
% Fatores de calibração PRÉ E PÓS MEDIÇÃO, SINAIS CORRIGIDOS E DRIFS ENTRE
% PRÉ E PÓS MEDIÇÃO
%% COMEÇANDO
% Importando as medições de calibração (Ja carregada pela sub-rotina
% loadcommedias.m)
function s = aplyfat(Data)
    %% Pré medisom
    % SISTEMA BIAURICULAR, ORELHA ESQUERDA
    earE_pre = (Data.measuredData.calibration.OrelhaE.T0.T0.timeSignal+...
        Data.measuredData.calibration.OrelhaE.T0.T1.timeSignal+...
        Data.measuredData.calibration.OrelhaE.T0.T2.timeSignal)/3;
    % SISTEMA BIAURICULAR, ORELHA DIREITA
    earD_pre = (Data.measuredData.calibration.OrelhaD.T0.T0.timeSignal+...
        Data.measuredData.calibration.OrelhaD.T0.T1.timeSignal+...
        Data.measuredData.calibration.OrelhaD.T0.T2.timeSignal)/3;
    % MICROFONE 1
    Mic1_pre = (Data.measuredData.calibration.Mic1.T0.T0.timeSignal+...
        Data.measuredData.calibration.Mic1.T0.T1.timeSignal+...
        Data.measuredData.calibration.Mic1.T0.T2.timeSignal)/3;
    % MICROFONE 2
    Mic2_pre = (Data.measuredData.calibration.Mic2.T0.T0.timeSignal+...
        Data.measuredData.calibration.Mic2.T0.T1.timeSignal+...
        Data.measuredData.calibration.Mic2.T0.T2.timeSignal)/3;
    %% Pós medisom
    % SISTEMA BIAURICULAR, ORELHA ESQUERDA
    earE_pos = (Data.measuredData.calibration.OrelhaE.T1.T0.timeSignal+...
        Data.measuredData.calibration.OrelhaE.T1.T1.timeSignal+...
        Data.measuredData.calibration.OrelhaE.T1.T2.timeSignal)/3;
    % SISTEMA BIAURICULAR, ORELHA DIREITA
    earD_pos = (Data.measuredData.calibration.OrelhaD.T1.T0.timeSignal+...
        Data.measuredData.calibration.OrelhaD.T1.T1.timeSignal+...
        Data.measuredData.calibration.OrelhaD.T1.T2.timeSignal)/3;
    % MICROFONE 1
    Mic1_pos = (Data.measuredData.calibration.Mic1.T1.T0.timeSignal+...
        Data.measuredData.calibration.Mic1.T1.T1.timeSignal+...
        Data.measuredData.calibration.Mic1.T1.T2.timeSignal)/3;
    % MICROFONE 2
    Mic2_pos = (Data.measuredData.calibration.Mic2.T1.T0.timeSignal+...
        Data.measuredData.calibration.Mic2.T1.T1.timeSignal+...
        Data.measuredData.calibration.Mic2.T1.T2.timeSignal)/3;
%% USANDO RECALQUEFAT.M
%% Para calcular o fator de calibração e sinal corrigido
    % Fator e sinal corrigido ORELHA ESQUERDA PRÉ medição
    [s.fat_earE_pre s.cor_earE_pre] = recalquefat(earE_pre);
    % Fator e sinal corrigido ORELHA DIREITA PRÉ medição
    [s.fat_earD_pre s.cor_earD_pre] = recalquefat(earD_pre);
    % Fator e sinal corrigido MICROFONE 1 PRÉ medição
    [s.fat_Mic1_pre s.cor_Mic1_pre] = recalquefat(Mic1_pre);
    % Fator e sinal corrigido MICROFONE 2 PRÉ medição
    [s.fat_Mic2_pre s.cor_Mic2_pre] = recalquefat(Mic2_pre);
    % Fator e sinal corrigido ORELHA ESQUERDA PÓS medição
    [s.fat_earE_pos s.cor_earE_pos] = recalquefat(earE_pos);
    % Fator e sinal corrigido ORELHA DIREITA PÓS medição
    [s.fat_earD_pos s.cor_earD_pos] = recalquefat(earD_pos);
    % Fator e sinal corrigido MICROFONE 1 PÓS medição
    [s.fat_Mic1_pos s.cor_Mic1_pos] = recalquefat(Mic1_pos);
    % Fator e sinal corrigido MICROFONE 2 PÓS medição
    [s.fat_Mic2_pos s.cor_Mic2_pos] = recalquefat(Mic2_pos);
%% OBSERVE O DRIFT
    % Utiliza do fator pré medição e aplica no sinal de calibração pós
    % medição.
    %
    % OBS: Por facilidade estou apensar retirando o fator pré
    % medição do sinal itaAudio de calibração e aplicando o fator pós
    % medição.
    %
    % DRIF NA ORELHA ESQUERDA
    s.drift_earE = s.fat_earE_pre*(s.cor_earE_pre/s.fat_earE_pre);   
    % DRIF NA ORELHA DIREITA
    s.drift_earD = s.fat_earD_pre*(s.cor_earD_pre/s.fat_earD_pre);   
    % DRIF NO MICROFONE 1
    s.drift_Mic1 = s.fat_Mic1_pre*(s.cor_Mic1_pre/s.fat_Mic1_pre);   
    % DRIF NO MICROFONE 2
    s.drift_Mic2 = s.fat_Mic2_pre*(s.cor_Mic2_pre/s.fat_Mic2_pre);       
    %% VEJA SE O SINAL ESTA EM 93,97 dB
end