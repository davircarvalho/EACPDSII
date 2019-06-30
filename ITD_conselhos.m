clear all; close all; clc;
% DAVI ROCHA CARVALHO; ENG. ACUSTICA - UFSM; MAIO/2019
% Obtenção de ITD a partir de medição com cabeça artificial
load('rirjanelada_em_1_segundo.mat')

%% Calculo do ITD
%todos o dataset possui a mesma taxa de amostragem
% fs = hrtf.s1r1.samplingRate; 
fs = 44100;
A= itaAudio; B=A;
n=0;
ITD = zeros(1, 10);
for i =1:2       %posições de fonte
    for j =1:5   % posições de receptor
        
        A = janela_um_segundo.esquerdo{i, j};
        B = janela_um_segundo.direito{i, j};
        IL = ita_start_IR(A);
        IR = ita_start_IR(B);
        
        n= n+1;
        ITD(1, n) = 1e6*abs(IL - IR)/fs; %valores em milissegundos 
    end
end

%%

azz =  [71, 27, 308, 305, 300, 162, 279, 284, 276, 65];
% az =  71  27  -52 ,-55 -60   162, -81, -76, -84, 65

ell =  [09, 01, 358, 001, 014, 158, 018, 003, 047, 07];
% el = [9    1  -2   1   14     2   18   3    47  7

% Colocar valores entre -180°:180°
for i = 1:length(azz)
    if azz(i)> 180
        azz(i) = azz(i) -360;    
    end
%     if ell(i) > 90
%        ell(i) = 180 - ell(i);   
%     end
end

% Organiza por sequência de azimute
% [td, idx] = sort(td);
[azz, idx] = sort(azz);
% Faz a mesma alteração feita no azimute 
ell(idx) = ell; 
ITD(idx) = round(ITD, 1);

%%
clc
itd = eye(10).*ITD;
 k = 1:10;
 l(idx) = k;
imagesc(l, l, itd);



set(gca,'XTick', linspace(8, 9, 10));
set(gca,'YTick', linspace(8, 9, 10));
yticklabels(ell)
xticklabels(azz)

title('ITD')
xlabel('Azimute [°]')
ylabel('Elevação [°]')
c = colorbar;
d = sort(ITD);
% set(c,'Ticks', d)
set(c,'TickLabels', d)
c.Label.String = 'Tempo [\mus]';
set(gca,'FontSize',13)

a = [1,2,3,4,5];
b = [2,1,3,4,5];
a(b)=a;