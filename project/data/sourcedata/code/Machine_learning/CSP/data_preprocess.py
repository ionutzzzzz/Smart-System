import numpy as np
from os.path import join
import scipy.io as sio
import random
import mne



ch_names = ["Fpz","Fp1","Fp2","AF3","AF4","AF7","AF8","Fz","F1","F2","F3","F4","F5",
              "F6","F7","F8","FCz","FC1","FC2","FC3","FC4","FC5","FC6","FT7","FT8","Cz",
              "C1","C2","C3","C4","C5","C6","T7","T8","CP1","CP2","CP3","CP4","CP5","CP6",
              "TP7","TP8","P3","P4","P5","P6","P7","P8","POz","PO3","PO4","PO5",
              "PO6","PO7","PO8","Oz","O1","O2"]


event_id = {'left': 1,'right':2}

def get_data(subj,data_path):
    da=sio.loadmat(join(data_path,'S'+str(subj).zfill(3)+'.mat'))
    data=da['data']
    labels=np.ravel(da['labels'])
    return data,labels


def create_raw(data,labels,freq=250):

    si,sj,sk=data.shape
    da=data.transpose(1,0,2)
    da=da.reshape(sj,si*sk)
    llen=data.shape[0]

    # Initialize the event array (timestamp and event type)
    event=np.zeros((llen,3))
    info = mne.create_info(
        ch_names=ch_names,
        ch_types="eeg",  # channel type
        sfreq=freq  # frequency
    )

    # Create the raw object
    raw = mne.io.RawArray(da, info)  # create raw

    # Populate events
    for i in range(llen):
        event[i,0]=i*sk
        event[i,2]=labels[i]

    event=event.astype(int)
    raw.info['events']=event

    # Assign events using MNE's set_annotations method (instead of direct assignment to raw.info['events'])
    #annotations = mne.Annotations(onset=event[:, 0] / float(freq),  # convert to seconds
    #                              duration=np.ones(len(event)),  # assume 1 second for each event duration
    #                              description=[str(e) for e in event[:, 2]])  # event labels
    #raw.set_annotations(annotations)

    return raw

def mnebandFilter(data,labels,lowfreq,highfreq):
    data = create_raw(data,labels)
    data.filter(lowfreq, highfreq, fir_design='firwin')

    event = data.info['events']

    train_epoches = mne.Epochs(data, event, event_id, 0, 4 - 0.004,
                               baseline=None, preload=True)
    train_data = train_epoches.get_data()
    return train_data
