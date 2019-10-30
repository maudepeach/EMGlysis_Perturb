import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

##Import .csv data using Pandas


## Process EMG signal: remove mean
emg_correctmean = emg - np.mean(emg)		#emg variable = raw data import of EMG_flagged items. See EMGlysis.py; to be continued

def filteremg(time, emg, low_pass = 10, sfreq = 1000, high_band = 20, low_band = 450):
	"""
	time: Time data
	emg : EMG data
	high: high-pass cut off frequency
	low: low-pass cut off frequency
	sfreq: sampling frequency
	"""

	# Normalize cut-off freq to sfreq
	high_band = high_band/(sfreq/2)
	low_band = low_band/(sfreq/2)

	# Create bandpass filter for EMG
	b1, a1 = sp.signal.butter(4, [high_band,low_band, btype = 'bandpass'])

	# Process EMG signal: filter EMG
	emg_filtered = sp.signal.filtfilt(b1, a1, emg_correctmean)

	# Process EMG signal: rectify
	emg_rectified = abs(emg_filtered)

	# Create low-pass filter & apply to rect signal; EMG envelope
	low_pass = low_pass/sfreq
	b2, a2 = sp.signal.butter(4, low_pass, btype = 'lowpass')
	emg_envelope = sp.signal.filtfilt(b2, a2, emg_rectified)

	# Plot subplot graphs
	fig = plt.figure()
	plt.subplot(1, 4, 1)
	plt.subplot(1, 4, 1).set_title('Unfiltered,' + '\n' + 'unrectified EMG')
	plt.plot(time, emg_correctmean)
	plt.locator_params(axis = 'x', nbins = 4)
	plt.locator_params(axis = 'y', nbins = 4)
	plt.ylim(-1.5, 1.5)
	plt.xlabel('Time (sec)')
	plt.ylabel('EMG (a.u.)')

	plt.subplot(1, 4, 2)
	plt.subplot(1, 4, 2).set_title('Filtered,' + '\n' + 'rectified EMG:' + str(int(low_band * sfreq)) + 'Hz')
	plt.plot(time, emg_rectified)
	plt.locator_params(axis = 'x', nbins = 4)
	plt.locator_params(axis = 'y', nbins = 4)
	plt.ylim(-1.5, 1.5)
	plt.plot([0.9, 1.0], [1.0, 1.0], 'r-', lw = 5)
	plt.xlabel('Time (sec)')

	plt.subplot(1, 4, 3)
	plt.subplot(1, 4, 3).set_title('Filtered, rectified ' + '\n' + 'EMG envelope: ' + str(int(low_pass * sfreq)) + 'Hz')
	plt.plot(time, emg_envelope)
	plt.locator_params (axis = 'x', nbins = 4)
	plt.locator_params (axis = 'y', nbins = 4)
	plt.ylim(-1.5, 1.5)
	plt.plot([0.9, 1.0], [1.0, 1.0], 'r-', lw = 5)
	plt.xlabel('Time (sec)')

	plt.subplot(1, 4, 4)
	plt.subplot(1, 4, 4).set_title('Focused region')
	plt.plot(time[int(0.9 * 1000): int(1.0 * 1000)], emg_envelope[int(0.9 * 1000): int(1.0 * 1000)])
	plt.xlim(0.9, 1.0)
	plt.ylim(-1.5, 1.5)
	plt.xlabel('Time (sec)')

	fig_name = 'fig_' + str(int(low_pass * sfreq)) + '.png'
	fig.set_size_inches(w = 11, h = 7)
	fig.savefig(fig_name)


# Try out different cut-off values to see what happens to the 1) unfiltered, unrectified signal, 2) filtered, rectified signal, 
# 3) rectified signal w/ low-pass filter for EMG envelope, and 4) zoomed-in section of signal from 3) over a certain time period
for i in [3, 10, 40]:
	filteremg(time, emg_correctmean, low_pass = i)
