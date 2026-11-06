eeglab;

    EEG=readbdfdata({'data.bdf','evt.bdf'},'F:\PhD_project\stroke_experiment\data\rawdata\S002-wujianyou\');

    EEG=pop_chanedit(EEG, 'lookup','D:\\research\\matlab2018\\toolbox\\eeglab\\plugins\\dipfit\\standard_BEM\\elec\\standard_1005.elc');
    EEG = pop_select( EEG, 'nochannel',{'ECG','HEOR','HEOL','VEOU','VEOL'});
    EEG = pop_reref( EEG, 43);
    EEG = pop_eegfiltnew(EEG, 'locutoff',0.5,'hicutoff',40,'plotfreqz',1);
    EEG = pop_eegfiltnew(EEG, 'locutoff',49,'hicutoff',51,'revfilt',1,'plotfreqz',1);
    EEG = pop_rmbase( EEG, [],[]);
    EEG = pop_epoch( EEG, {  '1'  '2' '3' '4' }, [0  4], 'newname', 'BDF file epochs', 'epochinfo', 'yes');
    EEG = pop_rmbase( EEG, [],[]);
    EEG = pop_resample( EEG, 250);
    EEG = pop_saveset( EEG, 'filename','S2.set','filepath','F:\\PhD_project\\stroke_experiment\\data\\preprocesseddata\\set\\2\\');
    lbs=[EEG.event.type];
   
    labels=[];
    for i =1:length(lbs)        
        labels=[labels,str2num(lbs(i))] ;
    end

    data=EEG.data;
    %save(strcat('F:\PhD_project\stroke_experiment\data\preprocesseddata\2\','data','.mat'),'data','labels');