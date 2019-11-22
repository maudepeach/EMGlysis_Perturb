#Function of this program is to import, analyze, and plot .csv EMG data

#importing libraries and importing file for analysis
import matplotlib.pyplot as plt

import pandas as pd

#importing data and setting variables
raw_import = pd.read_csv('D:\BRaIN Lab\EMGAnalysis_Perturb\emg_data\PS08\CSV\PS08_perturb1_Rep_1.5.csv') # Replace pathfile with local
col_names = raw_import.columns

#make sure the x-axis for plot is the first column
time = raw_import['X[s]'] 

#peruse columns for those that have "EMG"
EMG_subs = 'EMG'
#print(EMG_col)
EMG_col = [i for i in col_names if EMG_subs in i]

#slice out columns that have EMG as their column header
RI_EMG = raw_import.loc[raw_import.index, EMG_col]
#print(RI_EMG)

#plot and save raw EMG signal
fig = plt.figure()
plt.plot(time, RI_EMG)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
fig_name = 'PS08p1-raw.png' # Replace plot name
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)


#Do low-pass, high-pass, and rectified filters on raw data from biosppy

#initial filter
from biosppy import emg

out = bs.signals.emg.emg(signal=RI_EMG, sampling_rate=1000.0, show=True)

#high-pass
highpass = bs.signals.emg.solnik_onset_detector(signal=RI_EMG, sampling_rate=20.0,threshold=None, active_state_duration=None)

#rectified (absolute value)

#low-pass

#Plot the other graphs
