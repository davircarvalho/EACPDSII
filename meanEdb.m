function out = meanEdb(in,type,dbref)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Função para calcular a media e depois converter para dB
% 
% Desenvolvido pelo professor da Engenharia Acústica 
%                                William D'Andrea Fonseca, Dr. Eng.
%
% Última atualização: 04/12/2017
% 
% Compatível com Matlab R2016b
%
% in: matriz com os valores.
% type: '20dBNPS', '10dBNPS', '20dB' e '10dB'.
% dbref: referência para o cálculo do dB.
%
% Exemplo:
% media = meanEdb(A);
% media = meanEdb(A,'20dBNPS');
% media = meanEdb(A,'10dB',1E-3);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Input check
if nargin < 1
    error('I need at least the input matrix.');
end
if nargin < 2
    type = '20dBNPS'; dbref = 20E-6;
end
if nargin < 3 && ~strcmp(type,'20dBNPS') && ~strcmp(type,'10dBNPS'); 
    dbref = 1;
end

%% Processing
if     strcmp(type,'20dBNPS'); dbref = 20E-6;
    out = mean(in); out = 20.*log10(out./dbref);
elseif strcmp(type,'10dBNPS'); dbref = 20E-6;
    out = mean(in); out = 10.*log10((out./dbref).^2);
elseif strcmp(type,'20dB')
    out = mean(in); out = 20.*log10(out./dbref);    
elseif strcmp(type,'20dB2')
    out = mean(in); out = 20.*log10((out./dbref).^2);       
elseif strcmp(type,'10dB')
    out = mean(in); out = 10.*log10(out./dbref);  
elseif strcmp(type,'10dB2')
    out = mean(in); out = 10.*log10((out./dbref).^2);      
else
    disp('Hum... I will try do it, but have a look to the results.');
    out = mean(in); out = 20.*log10(out./20E-6);
end

%%% See you later
end