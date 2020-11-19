#%%
#%matplotlib qt
import mne
import os
from mne_bids import write_raw_bids, BIDSPath,make_dataset_description
import re
import settings
import event_test
import pandas as pd
#%% 
subjetc_file=settings.subject_path_init()
os.chdir(settings.base_dir_init())
#%%

raw_files=os.listdir(subjetc_file)
raw_file_list=[]
marker_lists=pd.read_csv('Behavioral/all_raw_marker.csv')['trigger'].to_list() 
event_ids=event_test.raw_marker_create(marker_lists)

for raw_file in raw_files:
    if os.path.splitext(raw_file)[1]=='.vhdr':
        raw_file_list.append(raw_file)
#%%
for q in range(0,len(raw_file_list)):

    raw=mne.io.read_raw_brainvision(os.path.join(subjetc_file,raw_file_list[q]),preload=False)
    # if len(raw.info['ch_names'])>60:
    #     raw.info['bads']=['BIP1','BIP2','BIP3','BIP4','BIP5','BIP6','BIP7','BIP8','BIP9','BIP10','BIP11','BIP12','BIP13','BIP14',
    #                  'BIP15','BIP16','BIP17','BIP18','BIP19','BIP20','BIP21','BIP22','BIP23','BIP24']
    # raw.drop_channels(ch_names=raw.info['bads'])
    raw.info['line_freq'] = 50
    raw.set_channel_types(mapping={'EOG':'eog'})
    # montage=mne.channels.make_standard_montage('standard_1020')
    # raw.set_montage(montage)
    subject_id=re.findall('(\d+)',raw_file_list[q])[0]
    bids_path = BIDSPath(subject=subject_id, task=settings.task, root=settings.bids_root_path_init(),session=settings.session,datatype='eeg',suffix='eeg')
    #events,events_id=mne.events_from_annotations(raw,event_id=event_ids)       
    write_raw_bids(raw, bids_path,overwrite=True)

make_dataset_description(path=settings.bids_root_path_init(),name=settings.project_name,authors=settings.authors,
acknowledgements=settings.acknowledgements,funding=settings.funding_support,overwrite=True)

