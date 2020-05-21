#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:58:20 2020

@author: wexu
"""

import mne
import os.path as op

from config_GP_Learn_Body_Rhythms import Ids, group_name, MEG_data_path

for subject_id in Ids:
    
    subject = group_name+"%d" % subject_id
    print("processing subject: %s" % subject)
    
    tasks=['av2','av2']
    days=[1,2]   
    
    for task,day in zip(tasks,days):
        
        fname=op.join(MEG_data_path,subject,task+'_%d'%day+'_%02d'%subject_id+'.fif')
        
        bio=mne.io.read_raw_fif(fname,preload=True).pick_types(meg=False,eog=False, eeg=False, ecg=True, bio=True)
        
        df=bio.to_data_frame(index='time')
        
        df.to_csv(subject+'_%d'%day)
        
        x