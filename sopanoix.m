%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Cálculo de média e incerteza.
% 
% Desenvolvido pelo professor da Engenharia Acústica 
%                                William D'Andrea Fonseca, Dr. Eng.
%
% Última atualização: 04/12/2017
% Compatível com Matlab R2015a
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Adaptação por Sidney Volney Cândido 
% Data: 16/05/2019
% 
% Adaptação toma como entrada o vetor no qual se deseja fazer o plot do
% intervalo de confiança por distribuição normal
function Plot = sopanoix(cinf)
%% Inputs
% Alterar o basePath
basePath = 'C:\Users\Acer Aspire\Google Drive\Grupo 4\Process\'; % Use a barra "\" no fim
Name = input('O que estamos fazendo? (Escreva uma string com o titulo do gráfico) ');      % Alterar para o fone do grupo
confianca = input('Qual é o intervalo de confiança? ');
cor = input('digite um número de 1 a 11 para escolher cor (Veja colors.m para mais detalhes) ');
SaveFig = 0; % Alterar para 1 para salvar as figuras
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Frequency 
% CUIDADO COM O FSPAN, PODE SER QUE NÃO CARREGUE O SWEEP DE ENTRADA
f.span = linspace(10^-5,20000,131073); if f.span(1)==0; f.spanLog = [10^-5 f.span(2:end)']'; else; f.spanLog = f.span; end;
f.plot=[20, 100, 1000, 10000, 20000]; 
A = sep_convert(f.plot,'%5.0f','virgula',0); B = sep_convert(f.plot,'%5.0f','virgula',1);
f.str = [A(1:2) B(3:end)]; clear A B
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Transposição (necessária)
vetor=cinf';
% Numero de medições
n_ponto = size(cinf);
n_ponto = n_ponto(2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Intervalo de confiança para o lado direito NÃO ALTERAR
%%% Fazendo a incerteza utilizando o desvio padrão da média p/ distribuição normal 
mediaN = stat_conf(vetor,'N',confianca,0,1,'dB20','med',20E-6);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Plot com incerteza  
%%%% Plot é realizado duas vezes para o patch da incerteza sair correto na legenda
%%% Plot sem transparência
Plot.shade1  = shadedErrorBar(f.spanLog, vetor, {@(x) meanEdb(x,'20dBNPS'), ...
    @(CI) abs(mediaN.intervaldB)}, {'Color',colors(cor),'LineWidth', 2.0}, 0, 0.30, 'log', 0); hold on;            
%%% Plot com transparência
Plot.shade1t = shadedErrorBar(f.spanLog, vetor, {@(x) meanEdb(x,'20dBNPS'),...
    @(CI) abs(mediaN.intervaldB)}, {'Color',colors(cor),'LineWidth', 2.0}, 1, 0.15, 'log', 0); hold on;      
      
%%% Para gráficos que não sejam em dB
% Plot.shade = shadedErrorBar(f.spanLog, fone.esq, {@mean, @(CI) abs(fone.esqCI.interval)}, {'Color',colors(2),'LineWidth', 2.0}, 1, 0.15, 'log', 0); hold on;      
%%%% Ajusta eixos, legenda e títulos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ylim([20 120]); xlim([20 20000]); % Limites dos eixos
xlabel('Frequência (Hz)'); ylabel(['NPS dB ref. 20 ' char(181) 'Pa'],'Interpreter','tex'); grid on; 
set(gca,'XTick',f.plot); set(gca,'XTickLabel',f.str);

Plot.leg = {[ 'Intervalo de ' strrep(num2str(mediaN.calc.alpha,'%4.2f'), '.', ',') '$\%$' ... 
    ' - $\bar{A}\,\pm$ ' strrep(num2str(mediaN.z(1,2),'%3.2f'), '.', ',') ...
    '$\,\sigma/\sqrt{n}$'],'M\''edia'};

Plot.lgd = legend(Plot.leg,'Interpreter','latex','Location','Southwest'); Plot.lgd.FontSize = 12;
title([ Name ' - ' num2str(n_ponto) ' medições']);
%%% Tamanho %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Plot.width = 1077; Plot.height=630; set(gcf,'color','white');
set(gcf,'units','pixels','position',[50,50,Plot.width,Plot.height]);  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Export figure
% if SaveFig == 1
%   export_fig(gcf,sprintf('%s', Fone), '-pdf', '-png','-r300', '-q99', '-bookmark', '-transparent', '-painters');  
% end