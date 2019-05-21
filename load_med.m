function [Data,MeasurementSetup] = load_med(medName)
    load('Data_empty_structure.mat'); % Carrega estrutura de dados vazia
    Data = rmfield(Data,'status');
    Data = rmfield(Data,'MS');
    medmatpath = strcat(medName,'_mat/'); % Caminho dos takes em .mat
    
    load(strcat(medmatpath,medName,'_MS.mat')); % Carregando MeasurementSetup
    myfiless = ls(strcat(medmatpath,'*take*.mat'));
    myfiles = split(myfiless); % Lista com nomes dos arquivos dos takes
    
    for i=1:length(myfiles)-1 % loop para adicionar itens de cada take no struct medStruct
        file = char(myfiles(i)); % nome do arquivo da vez
        fprintf([file,'\n'])
        loadedStruct = load(file); % dados do take
        fn1 = fieldnames(loadedStruct); % listando fields. Níveis posívels: 'measuredData' ou 'Status'

        for k1=1:numel(fn1) % iterando nos fields de Data
            key1 = cell2mat(fn1(k1)); % field da vez
            
            if strcmp(key1,'measuredData')
                fn2 = fieldnames(eval(['loadedStruct.' key1])); % listando fields. Níveis posívels: 'SxRx', 'noisefloor' ou 'calibration'
                
                for k2=1:numel(fn2) % iterando nos fields de Data.measuredData
                    key2 = cell2mat(fn2(k2)); % field da vez
                    
                    if strcmp(key2,'calibration')
                        fn3 = fieldnames(eval(['loadedStruct.' key1 '.' key2])); %listando fields. Níveis possíveis: 'T0', 'T1, 'T2' ...
                        for k3=1:numel(fn3)
                            key3 = cell2mat(fn3(k3)); % field da vez
                            check = 'T0';
                            if eval(['isfield(Data.measuredData.calibration.' key3 ',check)']) % verifica se T0 já existe em Data
                                fn4 = fieldnames(eval(['Data.' key1 '.' key2 '.' key3]));
                                lastTakenum = str2num(strrep(fn4{end},'T',''));
                                newTakeCode = ['T' num2str(lastTakenum+1)];
                                eval(['Data.' key1 '.' key2 '.' key3 '.' newTakeCode '= loadedStruct.' key1 '.' key2 '.' key3 ';'])
                            else
                                eval(['Data.measuredData.calibration.' key3 '.' check ' = loadedStruct.' key1 '.' key2 '.' key3 ';'])
                            end
                        end
                        
                    elseif strcmp(key2,'noisefloor')
                            check = 'T0';
                            if eval(['isfield(Data.measuredData.noisefloor,check)'])
                                fn4 = fieldnames(eval(['Data.' key1 '.' key2]));
                                lastTakenum = str2num(strrep(fn4{end},'T',''));
                                newTakeCode = ['T' num2str(lastTakenum+1)];
                                eval(['Data.' key1 '.' key2 '.' newTakeCode '= loadedStruct.' key1 '.' key2 ';'])
                            else
                                eval(['Data.measuredData.noisefloor.' check ' = loadedStruct.' key1 '.' key2 ';'])
                            end
                    else
                        fn3 = fieldnames(eval(['loadedStruct.' key1 '.' key2])); % listando fields. Níveis posívels: 'varredura', 'musica' ou 'fala'
                        for k3=1:numel(fn3)
                            key3 = cell2mat(fn3(k3)); % field da vez
                            fn4 = fieldnames(eval(['loadedStruct.' key1 '.' key2 '.' key3]));  % listando fields. Níveis posívels: 'binaural' ou 'hc'
                            for k4=1:numel(fn4)
                                key4 = cell2mat(fn4(k4)); % field da vez
                                eval(['Data.' key1 '.' key2 '.' key3 '.' key4 '=loadedStruct.' key1 '.' key2 '.' key3 '.' key4 ';'])
                            end
                        end   
                    end
                end 
            elseif strcmp(key1,'status')
                
            end
        end
    end
end