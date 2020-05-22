# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:12:44 2020
@author: Farid Khafizov
"""

import os
import pandas as pd

wd = "C:\\Users\\Farid Khafizov\\conda\\kgu\\"
logdir = "log_dir\\"
output_file = 'results.csv'

logfiles = os.listdir(wd+logdir)

PREFIX = "BOM_4NOtBu"
goodfiles=[]
energy = []
for fn in logfiles: 
    if fn.find(PREFIX)==0:
        goodfiles.append(fn.split('.')[0])
        enVal = -1
        with open(wd+logdir+fn) as f:
            content = f.readlines()
            for ss in content: 
                pos = ss.find("HF=")
                if pos>=0:
                    enVal = ss[pos:].split('\\')[0].split('=')[1]
        energy.append(enVal)
        
df=pd.DataFrame({'filename':goodfiles, 'energy':energy})

df.to_csv(wd+output_file)
