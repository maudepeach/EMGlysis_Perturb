#Function of this program is to import, analyze, and plot .csv EMG data

#importing libraries and importing file for analysis
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd

raw_import = pd.read_csv('file:///E:/BRaIN Lab/Perturbation_2019/Older_Stepper/emg_data/PS08/CSV/PS08_perturb1_Rep_1.5.csv') # Replace pathfile with local

time = np.array([i/1000 for i in range(0, len(raw_import), 1)]) # sampling rate 1000 Hz

#plot and save EMG signal
fig = plt.figure()
plt.plot(time, raw_import)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
fig_name = 'PSO8p1-test.png' # Replace plot name
fig.set_size_inches(w=11,h=7)
fig.savefig(fig_name)
