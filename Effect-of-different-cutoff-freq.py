import pandas as pd
import numpy as np
import scipy as sp
from scipy import signal
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

sfreq = 1000
high_band = 20
low_band = 450
low_pass = 10

# Normalize cut-off freq to sfreq
high_band = high_band/(sfreq/2)
low_band = low_band/(sfreq/2)

# Create bandpass filter for EMG
b1, a1 = sp.signal.butter(4, [high_band, low_band], btype = 'bandpass')

## Process EMG signal: filter EMG
emg_filtered = sp.signal.filtfilt(b1, a1, emg_correctmean, axis = 0)

# Process EMG signal: rectify
emg_rectified = abs(emg_filtered)
	
# Create low-pass filter & apply to rect signal; EMG envelope
low_pass = low_pass/sfreq
b2, a2 = sp.signal.butter(4, low_pass, btype = 'lowpass')
emg_envelope = sp.signal.filtfilt(b2, a2, emg_rectified, axis = 0)

# Plot subplot graphs
fig = plt.figure(1)
base = fig.add_subplot(1, 4, 1)
base.set_title('Unfiltered,' + '\n' + 'unrectified EMG')
plt.plot(time, emg_correctmean)
plt.locator_params(axis = 'x', nbins = 4)
plt.locator_params(axis = 'y', nbins = 4)
plt.ylim(-0.01, 0.01)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

filtrect = fig.add_subplot(1, 4, 2)
filtrect.set_title('Filtered,' + '\n' + 'rectified EMG:' + str(int(low_band * sfreq)) + 'Hz')
plt.plot(time, emg_rectified)
plt.locator_params(axis = 'x', nbins = 4)
plt.locator_params(axis = 'y', nbins = 4)
plt.ylim(-0.01, 0.01)
plt.plot([0.9, 1.0], [1.0, 1.0], 'r-', lw = 5)
plt.xlabel('Time (sec)')

env = fig.add_subplot(1, 4, 3)
env.set_title('Filtered, rectified ' + '\n' + 'EMG envelope: ' + str(int(low_pass * sfreq)) + 'Hz')
plt.plot(time, emg_envelope)
plt.locator_params (axis = 'x', nbins = 4)
plt.locator_params (axis = 'y', nbins = 4)
plt.ylim(-0.01, 0.01)
plt.plot([0.9, 1.0], [1.0, 1.0], 'r-', lw = 5)
plt.xlabel('Time (sec)')

focused = fig.add_subplot(1, 4, 4)
focused.set_title('Focused region')
plt.plot(time[int(0.9 * 1000): int(1.0 * 1000)], emg_envelope[int(0.9 * 1000): int(1.0 * 1000)])
plt.xlim(0.9, 1.0)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
fig_name = 'fig_' + str(int(low_pass * sfreq)) + '.png'
fig.set_size_inches(w = 11, h = 7)
fig.savefig(fig_name)


# Try out different cut-off values to see what happens to the 1) unfiltered, unrectified signal, 2) filtered, rectified signal, 
# 3) rectified signal w/ low-pass filter for EMG envelope, and 4) zoomed-in section of signal from 3) over a certain time period
