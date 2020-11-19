# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:58:33 2020

@author: Psychology
"""

import os
import pandas as pd
import numpy as np
import settings
import re


os.chdir(settings.base_dir_init())
marker_fname=('behavioral_data/data/lists/')

marker_files=os.listdir(marker_fname)
marker_file_list=[]
for marker_file in marker_files:
    if os.path.splitext(marker_file)[1]=='.csv':
        marker_file_list.append(marker_file)

positive_list=[]
control_list=[]
cue_only_list=[]
for positive in marker_file_list:
    if positive.find('positive')==7 or positive.find('positive')==6:
        positive_list.append(positive)
for control in marker_file_list:
    if control.find('control')==7 or control.find('control')==6:
        control_list.append(control)
for cue in marker_file_list:
    if cue.find('cue')==7 or cue.find('cue')==6:
        cue_only_list.append(cue)
        
for i in range(0,len(positive_list)):
    all_conditions=pd.DataFrame(columns=['Positive','Control','Cue_only'])
    all_conditions['Positive']=pd.read_csv(marker_fname + positive_list[i])['cue_trigger']
    all_conditions['Control']=pd.read_csv(marker_fname + control_list[i])['cue_trigger']
    all_conditions['Cue_only']=pd.read_csv(marker_fname + cue_only_list[i])['trigger_learn']
    subject_id=re.findall('(\d+)',positive_list[i])[0]
    all_conditions.to_csv('Behavioral/condition_marker/'+ subject_id +'_marker_lists.csv',index=False)