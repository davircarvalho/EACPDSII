%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%          2019.1 
%% Rotina de processamento de dados
    % 12/05: Vers�o 1, sugest�es para pr�ximas vers�es: arrumar os
    % gr�ficos; saves 

%% Carregue esses arquivos (Espere um pouco)
    [calib noise ent med]= loadcommedias(Data,MeasurementSetup);
%% Load .mat (verificar se o .time do odeon ta exportando os 2 canais)
    % load('medicaobucha.mat')
   [odeon Fs] = audioread('odeon.Wav');
    med.odeon = itaAudio; med.odeon.time = odeon ;med.odeon.channelNames = {'S2R2: Simula��o'};
%% Fator de corre��o aplicado? (Implementar sub-rotina para fator de corre�o)
%% Subrotina para calculo de RIR
% A subrotina rirnhrtfmaker.m pega os sinais do loadcommedias .mat como entrada (med e input, ou saida e entrada)
% e faz a divis�o espectral (pega o vetor .freq do itaAudio) da medi��o com o sweep de entrada
[rir hrtf] = rirnhrtfmaker(med,ent);
%% 1. Plot ruido de fundo com medi��o

    corr.ruido = noise.ch1 ;          % Carregando ru�do de fundo da orelha esquerda(com fator aplicado)
    corr.ruido.channelUnits = {'Pa'};
    corr.med = med.S1R1SW.esq ;      % Carregando a medi��o com varredura
    corr.med.channelUnits = {'Pa'};
        % Plot do Ita com a jun��o (merge dos dois canais
        results.first = merge(corr.ruido,corr.med);
        results.first.comment = 'Compara��o do Ru�do de fundo com varredura (orelha esquerda)';       
        ita_plot_freq(results.first) 
%% 2. Espectrograma
    %% 2.1. Modo manual (By Tales)
 
        NFTT = 2^18;
        Fs = 44100; %1000 % Sampling frequency
        T = 1/Fs; % Sampling period
        X = med.S1R1SW.esq;
        L = length(X.time);

        BL = 256; %% n�mero de blocos
        BS = round(L/BL); %% block size
        freq=linspace(0,22000*2,BS); %% vetor de frequ�ncia
        time=linspace(0,(NFTT-1)/Fs,BL); %% vetor de tempo
    
        for n=1:BL

            bo(:,n)=abs((2*fft(sqrt(8/3)*(hann(BS)).*(X.time((BS*(n-1))+1:BS*(n))))/BS)); %% sinal para janela hanning

            bod(:,n)=20.*log10((bo(:,n))./(1./time(n)));
        end


        figure
        pcolor((time),(freq),(bod)); shading interp; colormap hot
        colormap hot

        c=colorbar('FontSize',16);
        c.Label.String = 'Pot�ncia/Frequ�ncia [dB/Hz]';
        title('Espectrograma manual')
        xlabel('Tempo [s]','fontsize',16)
        ylabel('Frequ�ncia [Hz]','fontsize',16)
        xlim([0 6])
        ylim([0 22000])
    %% 2.2. Modo matlab

        figure()
        spectrogram(med.S1R1SW.esq.time, 2000,'yaxis');
    %% 2.3. Spectrograma da fala
        figure()
        spectrogram(med.S1R1FN.esq.time, 2000,'yaxis');
    %% 2.4. Espectrograma da m�sica
        figure()
        spectrogram(med.S1R1MS.esq.time, 2000,'yaxis');
%% 3. RESPOSTAs IMPULSIVA
    %% 3.1. 5 pontos de uma fonte plotados num grafico s� (centro de cabe�a)
        % Fonte escolhida S1;
        % results.h31 � um itaAudio com 5 canais, cada canal � uma resposta
        % impulsiva de centro de cabe�a
        results.h31 = ita_merge(rir.H_cen11,rir.H_cen12, rir.H_cen13, rir.H_cen14, rir.H_cen15);
        results.h31.comment = 'Respostas impulsivas da Fonte S1';
        ita_plot_freq(results.h31)
        %% 3.1.1. Intervalo de confian�a
        % Subrotina que plota o intervalo de confian�a com distribui��o
        % normal (rotininha de instrumenta��o), coloque uma string para
        % t�tulo do gr�fico
        results.plot31 = sopanoix(results.h31.freq);
    %% 3.2. HRTF S2R2
            % importa da subrotina rirnhrtfmaker as hrtfs (s�o itaAudios)
            results.h32 = (hrtf.s2r2);
            % Vizualise no tempo
            ita_plot_time(results.h32)
            % HRTF
            ita_plot_freq(results.h32)
        %% 3.2.1 Comparando com odeon
            results.h321 = merge(results.h32,med.odeon/20e-6); results.h321.comment = 'S2R2: Comparativo de HRTFs = Experimental & simulado' ;
            ita_plot_freq(results.h321);
    %% 3.3 TODAS AS HRTFs        
         %% 3.3.1 Lado esquerdo + intervalo de confian�a
        Hs.Waterfall.esq = merge( rir.H_esq11, rir.H_esq12,rir.H_esq13,rir.H_esq14,...
            rir.H_esq15, rir.H_esq21, rir.H_esq22, rir.H_esq23, rir.H_esq24,...
            rir.H_esq25, rir.H_esq31, rir.H_esq32, rir.H_esq33, rir.H_esq34, rir.H_esq35);
        Hs.Waterfall.esq.channelNames = {'S1R1','S1R2','S1R3','S1R4','S1R5','S2R1','S2R2',...
            'S2R3','S2R4','S2R5','S3R1','S3R2','S3R3','S3R4','S3R5'};
        Hs.Waterfall.esq.comment = 'Todas as HRTFs: Lado esquerdo';
            %% Incerteza por desvio padr�o da m�dia p/ distribui��o normal,
            % confian�a 95%
       results.plot331 = sopanoix(Hs.Waterfall.esq.freq);      
         %% 3.3.1 Lado direito + intervalo de confian�a
        Hs.Waterfall.dir = merge( rir.H_dir11, rir.H_dir12,rir.H_dir13,rir.H_dir14,...
            rir.H_dir15, rir.H_dir21, rir.H_dir22, rir.H_dir23, rir.H_dir24,...
            rir.H_dir25, rir.H_dir31, rir.H_dir32, rir.H_dir33, rir.H_dir34, rir.H_dir35);
        Hs.Waterfall.esq.channelNames = {'S1R1','S1R2','S1R3','S1R4','S1R5','S2R1','S2R2',...
            'S2R3','S2R4','S2R5','S3R1','S3R2','S3R3','S3R4','S3R5'};
        Hs.Waterfall.esq.comment = 'Todas as HRTFs: Lado esquerdo';
            %% Incerteza por desvio padr�o da m�dia p/ distribui��o normal,
            % confian�a 95%
       results.plot331 = sopanoix(Hs.Waterfall.dir.freq);
       %% 3.3. M�dia de todos os centros dos dodecaedros (para T60 e parametros seguindo ISO)
            results.h33 = (rir.H_cen11+rir.H_cen12+rir.H_cen13+rir.H_cen14+...
                rir.H_cen15+rir.H_cen21+rir.H_cen22+rir.H_cen23+rir.H_cen24+rir.H_cen25)/10;
            results.h33.comment = 'M�dia das respostas impulsivas para ISO';
            ita_plot_freq(results.h33)
    %% 3.4. Compara��o das fontes
        % Nomeando as fontes para legenda
        med.S1R4SW.cen.channelNames = {'S1'}; med.S2R4SW.cen.channelNames = {'S2'}; med.S3R4SW.cen.channelNames = {'S3'};
        % Resultado: juntando os itaAudio
        results.h34 = merge(med.S1R4SW.cen, med.S2R4SW.cen, med.S3R4SW.cen);
        % Titulo do resultado
        results.h34.comment='Comparativo da resposta da sala com diferentes fontes';
        ita_plot_freq(results.h34);
    %% 3.5. Limpando com Welch (comparando)
        % Mesmo sendo um sinal deterministico, h� referencias que dizem que
        % realizar esse processamento estatistico melhora a resposta 
        avgm = 8; % Num�ro de m�dias
        ovlap = 0.5; % Overlap
        NFFT = length(med.S2R2SW.cen.time);             % N�mero de amostras do sinal
        NJAN = NFFT*ovlap/avgm;               % N�mero de amostras da janela
        w = window(@hamming,NJAN);            % Janela hamming
        Hs.welch = tfestimate(ent.sweep.time,med.S2R2SW.cen.time,[],[],NFFT,Fs,'onesided');
        Hs.h35 = itaAudio; Hs.h35.freq = Hs.welch; Hs.h35.channelNames ={'Resposta da sala com processamento estat�stico'};
        results.h35 = merge(Hs.h35,rir.H_cen22);
        results.h35.comment = 'Compara��o da resposta com processamento estat�stico';
        ita_plot_freq(results.h35)
%% 4. Param�tros da sala (Pegar a m�dia dos pontos do S3)
    %%
    results.h4 = ita_roomacoustics(ita_merge(rir.H_cen11,rir.H_cen12,rir.H_cen13,rir.H_cen14,rir.H_cen15,rir.H_cen21,...
        rir.H_cen22,rir.H_cen23,rir.H_cen24,rir.H_cen25),'T20','C80','D50','EDT',...
        'Center_Time','freqRange',[125 8000],'bandsPerOctave',3);
    
    