import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

## Import .csv data using Pandas

raw_import = pd.read_csv('D:\\BRaIN Lab\EMGAnalysis_Perturb\emg_data\PS29\PS29_Perturb_1_Rep_1.10.csv') # Replace pathfile with local
col_names = raw_import.columns

time = raw_import['X[s]']

## Select columns with EMG in column name, then splice respective columns out into separate array

find_EMG = 'EMG'

col_EMG = [i for i in col_names if find_EMG in i]

emg = raw_import.loc[raw_import.index, col_EMG]


## Process EMG signal: remove mean
emg_correctmean = emg - np.mean(emg)	

## Plot comparison of EMG with offset vs mean-corrected values

fig = plt.figure(1)
mean_off = fig.add_subplot(1, 2, 1)
mean_off.set_title('Mean offset present')
plt.plot(time, emg)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-0.01, 0.01)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

mean_corr = fig.add_subplot(1, 2, 2)
mean_corr.set_title('Mean-corrected values')
plt.plot(time, emg_correctmean)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-0.01, 0.01)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

fig.tight_layout()
fig_name = 'fig2.png'
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)