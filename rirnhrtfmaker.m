%% RIR E HRTFS
function [rir hrtf] = rirnhrtfmaker(med,ent)
%% RESPOSTAs IMPULSIVA
    %% centro de cabeça
        % Fonte S1;
            rir.H_cen11 = itaAudio; rir.H_cen11.freq = med.S1R1SW.cen.freq./ent.sweep.freq;
            rir.H_cen11.channelNames = {'S1R1'};
            rir.H_cen12 = itaAudio; rir.H_cen12.freq = med.S1R2SW.cen.freq./ent.sweep.freq;
            rir.H_cen12.channelNames = {'S1R2'};
            rir.H_cen13 = itaAudio; rir.H_cen13.freq = med.S1R3SW.cen.freq./ent.sweep.freq;
            rir.H_cen13.channelNames = {'S1R3'};
            rir.H_cen14 = itaAudio; rir.H_cen14.freq = med.S1R4SW.cen.freq./ent.sweep.freq;
            rir.H_cen14.channelNames = {'S1R4'};
            rir.H_cen15 = itaAudio; rir.H_cen15.freq = med.S1R5SW.cen.freq./ent.sweep.freq;
            rir.H_cen15.channelNames = {'S1R5'};
        % Fonte S2
            rir.H_cen21 = itaAudio; rir.H_cen21.freq = med.S2R1SW.cen.freq./ent.sweep.freq;
            rir.H_cen21.channelNames = {'S2R1'};
            rir.H_cen22 = itaAudio; rir.H_cen22.freq = med.S2R2SW.cen.freq./ent.sweep.freq;
            rir.H_cen22.channelNames = {'S2R2'};
            rir.H_cen23 = itaAudio; rir.H_cen23.freq = med.S2R3SW.cen.freq./ent.sweep.freq;
            rir.H_cen23.channelNames = {'S2R3'};
            rir.H_cen24 = itaAudio; rir.H_cen24.freq = med.S2R4SW.cen.freq./ent.sweep.freq;
            rir.H_cen24.channelNames = {'S2R4'};
            rir.H_cen25 = itaAudio; rir.H_cen25.freq = med.S2R5SW.cen.freq./ent.sweep.freq;
            rir.H_cen25.channelNames = {'S2R5'};
        % Fonte S3
            rir.H_cen31 = itaAudio; rir.H_cen31.freq = med.S3R1SW.cen.freq./ent.sweep.freq;
            rir.H_cen31.channelNames = {'S3R1'};
            rir.H_cen32 = itaAudio; rir.H_cen32.freq = med.S3R2SW.cen.freq./ent.sweep.freq;
            rir.H_cen32.channelNames = {'S3R2'};
            rir.H_cen33 = itaAudio; rir.H_cen33.freq = med.S3R3SW.cen.freq./ent.sweep.freq;
            rir.H_cen33.channelNames = {'S3R3'};
            rir.H_cen34 = itaAudio; rir.H_cen34.freq = med.S3R4SW.cen.freq./ent.sweep.freq;
            rir.H_cen34.channelNames = {'S3R4'};        
            rir.H_cen35 = itaAudio; rir.H_cen35.freq = med.S3R5SW.cen.freq./ent.sweep.freq;
            rir.H_cen35.channelNames = {'S3R5'};
        %% Lado esquerdo
            % Fonte S1;
            rir.H_esq11 = itaAudio; rir.H_esq11.freq = med.S1R1SW.esq.freq./ent.sweep.freq;
            rir.H_esq11.channelNames = {'S1R1: Lado esquerdo'};
            rir.H_esq12 = itaAudio; rir.H_esq12.freq = med.S1R2SW.esq.freq./ent.sweep.freq;
            rir.H_esq12.channelNames = {'S1R2: Lado esquerdo'};
            rir.H_esq13 = itaAudio; rir.H_esq13.freq = med.S1R3SW.esq.freq./ent.sweep.freq;
            rir.H_esq13.channelNames = {'S1R3: Lado esquerdo'};
            rir.H_esq14 = itaAudio; rir.H_esq14.freq = med.S1R4SW.esq.freq./ent.sweep.freq;
            rir.H_esq14.channelNames = {'S1R4: Lado esquerdo'};
            rir.H_esq15 = itaAudio; rir.H_esq15.freq = med.S1R5SW.esq.freq./ent.sweep.freq;
            rir.H_esq15.channelNames = {'S1R5: Lado esquerdo'};
            % Fonte S2
            rir.H_esq21 = itaAudio; rir.H_esq21.freq = med.S2R1SW.esq.freq./ent.sweep.freq;
            rir.H_esq21.channelNames = {'S2R1: Lado esquerdo'};
            rir.H_esq22 = itaAudio; rir.H_esq22.freq = med.S2R2SW.esq.freq./ent.sweep.freq;
            rir.H_esq22.channelNames = {'S2R2: Lado esquerdo'};
            rir.H_esq23 = itaAudio; rir.H_esq23.freq = med.S2R3SW.esq.freq./ent.sweep.freq;
            rir.H_esq23.channelNames = {'S2R3: Lado esquerdo'};
            rir.H_esq24 = itaAudio; rir.H_esq24.freq = med.S2R4SW.esq.freq./ent.sweep.freq;
            rir.H_esq24.channelNames = {'S2R4: Lado esquerdo'};
            rir.H_esq25 = itaAudio; rir.H_esq25.freq = med.S2R5SW.esq.freq./ent.sweep.freq;
            rir.H_esq25.channelNames = {'S2R5: Lado esquerdo'};
            % Fonte S3
            rir.H_esq31 = itaAudio; rir.H_esq31.freq = med.S3R1SW.esq.freq./ent.sweep.freq;
            rir.H_esq31.channelNames = {'S3R1: Lado esquerdo'};
            rir.H_esq32 = itaAudio; rir.H_esq32.freq = med.S3R2SW.esq.freq./ent.sweep.freq;
            rir.H_esq32.channelNames = {'S3R2: Lado esquerdo'};
            rir.H_esq33 = itaAudio; rir.H_esq33.freq = med.S3R3SW.esq.freq./ent.sweep.freq;
            rir.H_esq33.channelNames = {'S3R3: Lado esquerdo'};
            rir.H_esq34 = itaAudio; rir.H_esq34.freq = med.S3R4SW.esq.freq./ent.sweep.freq;
            rir.H_esq34.channelNames = {'S3R4: Lado esquerdo'};        
            rir.H_esq35 = itaAudio; rir.H_esq35.freq = med.S3R5SW.esq.freq./ent.sweep.freq;
            rir.H_esq35.channelNames = {'S3R5: Lado esquerdo'};
        %% Lado direito
                % Fonte S1;
            rir.H_dir11 = itaAudio; rir.H_dir11.freq = med.S1R1SW.dir.freq./ent.sweep.freq;
            rir.H_dir11.channelNames = {'S1R1: Lado direito'};
            rir.H_dir12 = itaAudio; rir.H_dir12.freq = med.S1R2SW.dir.freq./ent.sweep.freq;
            rir.H_dir12.channelNames = {'S1R2: Lado direito'};
            rir.H_dir13 = itaAudio; rir.H_dir13.freq = med.S1R3SW.dir.freq./ent.sweep.freq;
            rir.H_dir13.channelNames = {'S1R3: Lado direito'};
            rir.H_dir14 = itaAudio; rir.H_dir14.freq = med.S1R4SW.dir.freq./ent.sweep.freq;
            rir.H_dir14.channelNames = {'S1R4: Lado direito'};
            rir.H_dir15 = itaAudio; rir.H_dir15.freq = med.S1R5SW.dir.freq./ent.sweep.freq;
            rir.H_dir15.channelNames = {'S1R5: Lado direito'};
            % Fonte S2
            rir.H_dir21 = itaAudio; rir.H_dir21.freq = med.S2R1SW.dir.freq./ent.sweep.freq;
            rir.H_dir21.channelNames = {'S2R1: Lado direito'};
            rir.H_dir22 = itaAudio; rir.H_dir22.freq = med.S2R2SW.dir.freq./ent.sweep.freq;
            rir.H_dir22.channelNames = {'S2R2: Lado direito'};
            rir.H_dir23 = itaAudio; rir.H_dir23.freq = med.S2R3SW.dir.freq./ent.sweep.freq;
            rir.H_dir23.channelNames = {'S2R3: Lado direito'};
            rir.H_dir24 = itaAudio; rir.H_dir24.freq = med.S2R4SW.dir.freq./ent.sweep.freq;
            rir.H_dir24.channelNames = {'S2R4: Lado direito'};
            rir.H_dir25 = itaAudio; rir.H_dir25.freq = med.S2R5SW.dir.freq./ent.sweep.freq;
            rir.H_dir25.channelNames = {'S2R5: Lado direito'};
            % Fonte S3
            rir.H_dir31 = itaAudio; rir.H_dir31.freq = med.S3R1SW.dir.freq./ent.sweep.freq;
            rir.H_dir31.channelNames = {'S3R1: Lado direito'};
            rir.H_dir32 = itaAudio; rir.H_dir32.freq = med.S3R2SW.dir.freq./ent.sweep.freq;
            rir.H_dir32.channelNames = {'S3R2: Lado direito'};
            rir.H_dir33 = itaAudio; rir.H_dir33.freq = med.S3R3SW.dir.freq./ent.sweep.freq;
            rir.H_dir33.channelNames = {'S3R3: Lado direito'};
            rir.H_dir34 = itaAudio; rir.H_dir34.freq = med.S3R4SW.dir.freq./ent.sweep.freq;
            rir.H_dir34.channelNames = {'S3R4: Lado direito'};        
            rir.H_dir35 = itaAudio; rir.H_dir35.freq = med.S3R5SW.dir.freq./ent.sweep.freq;
            rir.H_dir35.channelNames = {'S3R5: Lado direito'};
%% HRTFs
    hrtf.s1r1 = ita_merge(rir.H_esq11, rir.H_dir11);
    hrtf.s1r2 = ita_merge(rir.H_esq12, rir.H_dir12);
    hrtf.s1r3 = ita_merge(rir.H_esq13, rir.H_dir13);
    hrtf.s1r4 = ita_merge(rir.H_esq14, rir.H_dir14);
    hrtf.s1r5 = ita_merge(rir.H_esq15, rir.H_dir15);
    hrtf.s1r1 = ita_merge(rir.H_esq11, rir.H_dir21);
    hrtf.s2r2 = ita_merge(rir.H_esq22, rir.H_dir22);
    hrtf.s2r3 = ita_merge(rir.H_esq23, rir.H_dir23);
    hrtf.s2r4 = ita_merge(rir.H_esq24, rir.H_dir24);
    hrtf.s2r5 = ita_merge(rir.H_esq25, rir.H_dir25);
    hrtf.s3r1 = ita_merge(rir.H_esq31, rir.H_dir31);
    hrtf.s3r2 = ita_merge(rir.H_esq32, rir.H_dir32);
    hrtf.s3r3 = ita_merge(rir.H_esq33, rir.H_dir33);
    hrtf.s3r4 = ita_merge(rir.H_esq34, rir.H_dir34);
    hrtf.s3r5 = ita_merge(rir.H_esq35, rir.H_dir35);
end
        