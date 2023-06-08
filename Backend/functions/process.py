
# ## Importing modules
import numpy as np
from scipy import fft, ifft
from scipy.signal import resample
from scipy.stats import kurtosis, skew, entropy
import pandas as pd
# import matplotlib.pyplot as plt
import antropy as ent


def find_Spectral_Values(file):
    columns = ['seconds', 'mV']
    df = pd.read_csv(file, usecols=columns)
    # Resampling original data
    fs_orig = 100  # Hz
    # Define new sampling rate
    fs_new = 250  # Hz
    # Compute resampling factor
    resample_factor = fs_new / fs_orig
    n_samples_resampled = int(len(df) * resample_factor)
    df = resample(df, n_samples_resampled)
    ecg_data_dft = np.abs(np.fft.fft(np.array(df[:, 1])))
    ecg_data_dft = ecg_data_dft[:len(ecg_data_dft)//2]
    # Compute the mean
    mean = sum(ecg_data_dft) / len(ecg_data_dft)
    # Compute the variance
    variance = sum((x - mean) ** 2 for x in ecg_data_dft) / len(ecg_data_dft)
    # Compute the standard deviation
    stddev = variance ** 0.5
    # Compute the skewness
    skewness = sum((x - mean) ** 3 for x in ecg_data_dft) / \
        len(ecg_data_dft) / stddev ** 3
    # Compute the fourth moment
    fourth_moment = sum(
        (x - mean) ** 4 for x in ecg_data_dft) / len(ecg_data_dft)
    # Compute the kurtosis
    kurtosis = fourth_moment / stddev ** 4 - 3
    entropy = ent.spectral_entropy(df[:, 1], sf=250, method='fft')
    return [kurtosis,skewness,entropy]

