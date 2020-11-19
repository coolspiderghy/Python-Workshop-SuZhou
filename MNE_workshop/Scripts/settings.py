import os
import numpy as np
import pandas as pd
#%% ###### DIRECTORY STRUCTURE ###### 
def base_dir_init(): # Base directory for EEG analysis
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return base_dir

def script_path_init():
    script_path = base_dir_init() + '\Scripts'
    return script_path

def bids_root_path_init():
    bids_path = base_dir_init() + '\mne_bids'
    return bids_path

def subject_path_init(): # Subjects directory, for storing EEG data 
    subject_path = base_dir_init() + '\Raw_data'
    return subject_path

def marker_list_path_init():
    marker_path = base_dir_init() + "\Behaviorl"
    return marker_path

if __name__ == '__main__':
    base_dir = base_dir_init()
    print('====== Current directory ======')
    print(base_dir)


#%% remove the data that did not meet your criteria, you shoudl use the "sub-number" to represent the subjects no matter the filename of your data#

rm_sub_list=['sub-01','sub-02','sub-04','sub-05','sub-06','sub-12','sub-17','sub-19','sub-21','sub-25','sub-32','sub-37','sub-39']


#%% ###################First we need to convert our raw EEG data into a BIDS-compliant folder structure##############
#######################In this section we need define the following parameters for data description##################


task='ForcedChioce'

session='3'


project_name='Sleep_learning_Forced_chioce_task'

authors='Tao Xia, Xiaoqing Hu'

acknowledgements='The authors would like to thank the subjects for their participantion' 

funding_support='GRF1004'

#################let's define the dict object of events_ids for MNE analysis############
#marker_lists=pd.read_csv('Behavioral/all_raw_marker.csv')['trigger'].to_list() # to do: events operation 

low_filter=30
high_filter=0.1

epochs_tmin=-0.2
epochs_tmax=1


  
# %%
