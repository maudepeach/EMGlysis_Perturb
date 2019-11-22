import scipy as sp
from scipy import signal
import numpy as np
import pandas as pd
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

# create bandpass filter for EMG
high = 20/(1000/2)
low = 450/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass')

# process EMG signal: filter EMG
emg_filtered = sp.signal.filtfilt(b, a, emg_correctmean, axis = 0)

# plot comparison of unfiltered vs filtered mean-corrected EMG
fig = plt.figure(1)
unfilt = fig.add_subplot(1, 2, 1)
unfilt.set_title('Unfiltered EMG')
plt.plot(time, emg_correctmean)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-0.01, 0.01)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

filt = fig.add_subplot(1, 2, 2)
filt.set_title('Filtered EMG')
plt.plot(time, emg_filtered)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-0.01, 0.01)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

fig.tight_layout()
fig_name = 'fig3.png'
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)