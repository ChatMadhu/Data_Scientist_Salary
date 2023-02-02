# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 05:44:57 2023

@author: User
"""

import pandas as pd
df =  pd.read_csv('glassdoor_jobs.csv')

#salary parsing

df = df[df['Salary Estimate']!='-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('$','').replace('K',''))
#Company text name only
#age of company
#preparinng of job description(python, etc..)
