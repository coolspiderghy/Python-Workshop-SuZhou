# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:40:12 2020

@author: Tao XIA
"""

def event_operation(raw_events,conditions_name,condition_marker):
    j=0
    new_marker_list=[]
    new_events=[]
    while j < len(conditions_name):
        for i in range(0,len(raw_events)):
            print(i)
            if raw_events[i][2] in condition_marker[conditions_name[j]].to_list():
                raw_events[i][2]=j+200 
                new_marker_list.append(j+200)
                new_events.append(raw_events[i])
        j=j+1
    return new_events,new_marker_list

def raw_marker_create(marker_list):
    key_list=[]
    for j in marker_list:
        b='Stimulus/s'+str(j)
        key_list.append(b)

    event_ids=dict(zip(key_list,marker_list))
    return event_ids
