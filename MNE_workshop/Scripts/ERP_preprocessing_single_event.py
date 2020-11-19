# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:51:24 2020

@author: Xia Tao
"""
#%% import the module that will be used
#%matplotlib qt
import mne
import os
from mne.preprocessing import (ICA, create_eog_epochs)
from mne_bids import read_raw_bids, BIDSPath
from autoreject import Ransac  # 
from autoreject.utils import interpolate_bads  # 
from pyprep.find_noisy_channels import NoisyChannels
import pandas as pd
import numpy as np
import settings
import event_test
#%% define the data path##


subjetc_file=settings.bids_root_path_init()
marker_file=settings.marker_list_path_init()

os.chdir(settings.base_dir_init())

os.makedirs('Raw_data/raw_ica/',exist_ok=True)
os.makedirs('Raw_data/epochs/',exist_ok=True)
#%% read the subject list from mne-bids path and remove the participants that predefined
raw_files=os.listdir(subjetc_file)
raw_file_list=[]
for raw_file in raw_files:
    if raw_file.split('-')[0]=='sub':
        raw_file_list.append(raw_file)

for i in settings.rm_sub_list:
    raw_file_list.remove(i)

#%%
marker_lists=pd.read_csv('Behavioral/all_raw_marker.csv')['trigger'].to_list()

raw_events_id=event_test.raw_marker_create(marker_list=marker_lists)

condition_marker_file=os.listdir('Behavioral/condition_marker/')

#%%
for q in range(0,len(raw_file_list)):
    subject_id=raw_file_list[q].split('-')[1]
    bids_path = BIDSPath(subject=subject_id, task=settings.task, root=settings.bids_root_path_init(),session=settings.session,datatype='eeg',suffix='eeg')
    raw=read_raw_bids(bids_path=bids_path,extra_params=dict(preload=True))
    raw.info['bads']=['FT7','FT8','T7','T8','TP7','TP8','AF7','AF8','M1','M2','BIP1','BIP2','BIP3','BIP4','BIP5','BIP6','BIP7','BIP8','BIP9','BIP10','BIP11','BIP12','BIP13','BIP14',
                      'BIP15','BIP16','BIP17','BIP18','BIP19','BIP20','BIP21','BIP22','BIP23','BIP24']
    raw.drop_channels(ch_names=raw.info['bads'])
    montage=mne.channels.make_standard_montage('standard_1020')
    raw.set_montage(montage)
    filt_raw=raw.copy()
    filt_raw.drop_channels('EOG')
    nd=NoisyChannels(filt_raw)
    nd.find_bad_by_ransac(n_samples=50,channel_wise=True)
    raw.info['bads']=nd.bad_by_ransac
    raw.notch_filter(np.arange(50,250,50))
    filt_raw.notch_filter(np.arange(50,250,50))
    raw.filter(l_freq=settings.high_filter,h_freq=settings.low_filter,fir_design='firwin')
    filt_raw.filter(l_freq=1, h_freq=settings.low_filter)
    filt_raw.info['bads']=raw.info['bads']
    raw.interpolate_bads(reset_bads=True,mode='accurate')
    filt_raw.interpolate_bads(reset_bads=True,mode='accurate')
    raw.resample(200,npad='auto')
    filt_raw.resample(200,npad='auto')
    raw.set_eeg_reference('average')
    filt_raw.set_eeg_reference('average')
    eog_evoked = create_eog_epochs(raw).average()
    raw.plot(block=True,n_channels=31,duration=30)
    ica=ICA(n_components=53,method='picard').fit(filt_raw, reject_by_annotation=True)
    eog_indices, eog_scores=ica.find_bads_eog(raw,threshold=0.2,measure='correlation')
    ica.exclude = eog_indices
    ica.plot_scores(eog_scores,exclude=ica.exclude,axhline=[-0.2,0.2],labels='eog')
    ica.plot_properties(raw, picks=eog_indices)
    ica.plot_sources(raw,block=True) 
    ica.plot_sources(eog_evoked) 
    ica.plot_sources(raw,block=True)                                    
    ica.plot_overlay(raw,picks='eeg')
    ica.apply(raw)
    raw.save('Raw_data/raw_ica/'+raw_file_list[q]+'_raw.fif',overwrite=True)
    events,events_id=mne.events_from_annotations(raw,event_id=raw_events_id)
    condition_marker=pd.read_csv('Behavioral/condition_marker/' + condition_marker_file[q])
    conditions=condition_marker.columns.values
    new_events,new_marker_list=event_test.event_operation(events,conditions_name=conditions,condition_marker=condition_marker)
    new_marker_list=list(set(new_marker_list))
    new_events_id=dict(zip(conditions.tolist(),new_marker_list))
    epochs=mne.Epochs(raw,events=new_events,event_id=new_events_id,baseline=None,preload=True,
                                                tmin=settings.epochs_tmin,tmax=settings.epochs_tmax,reject=dict(eeg=300e-6),flat=dict(eeg=1e-6))
    epochs.plot(block=True)
    epochs.save('Raw_data/epochs/' + raw_file_list[q] +'-epo.fif',overwrite=True)

    

