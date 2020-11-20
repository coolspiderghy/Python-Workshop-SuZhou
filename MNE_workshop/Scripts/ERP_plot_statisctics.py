


import mne
import pandas as pd 
import os
import settings


#%%
os.chdir(settings.base_dir_init())

epoch_fname=('Raw_data/epochs/')

epochs_list=os.listdir(epoch_fname)
condition_marker_file=os.listdir('Behavioral/condition_marker/')
condition_marker=pd.read_csv('Behavioral/condition_marker/' + condition_marker_file[0])
conditions=condition_marker.columns.values
#%%
evoked_list1=[]
evoked_list2=[]
evoked_list3=[]

condition_list=[evoked_list1,evoked_list2,evoked_list3]

for i in range(0,len(epochs_list))[0:7]:
    epochs=mne.read_epochs(epoch_fname+epochs_list[i],preload=True)
    epochs.apply_baseline(baseline=(None,0))
    for j in conditions:
        q=j + '_evoked'
        globals()[q]=epochs[j].average()
    
    for k,j in zip(condition_list,conditions):
        k.append(globals()[j+'_evoked'])


picks=[epochs.ch_names.index(ch)for ch in ['Oz','POz','O1','O2']]
condition_index={'Positive':evoked_list1,'Control':evoked_list2,'Cue_only':evoked_list3}
mne.viz.plot_compare_evokeds(condition_index,picks=picks,ci=None,combine='mean',show_sensors='upper right')




