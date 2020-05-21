#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:55:52 2020

@author: wexu
"""

import os 

study_path='/nashome1/wexu/MNE_data/AVLearn2'
group_name='AL'

MRI_data_path = os.path.join(study_path, 'subjects')
MEG_data_path = os.path.join(study_path, 'MEG')

os.environ["SUBJECTS_DIR"] = MRI_data_path

Ids=[1,2,3,4,5,6,7,8,9,10]

delay=25 #ms