def checkType(spectral_values):
    kurtosis = spectral_values[0]
    skewness = spectral_values[1]
    entropy = spectral_values[2]

    # Define threshold ranges for each signal type and feature
    ecg_threshold_entropy = [3.5, 7.5]
    pcg_threshold_entropy = [7.51, 8.98]
    resp_threshold_entropy = [0.5, 3]
    ppg_threshold_kurtosis = [1100, 1300]
    ecg_threshold_kurtosis = [7, 55]
    pcg_threshold_kurtosis = [2, 30]

    # Classify the signal based on its feature values
    if entropy > ecg_threshold_entropy[0] and entropy < ecg_threshold_entropy[1]:
        if kurtosis < 60:
            return("ECG")  # ECG
        else:
            return("PPG")  # PPG

    elif entropy > pcg_threshold_entropy[0] and entropy < pcg_threshold_entropy[1]:
        if kurtosis < 60:
            return("PCG")  # PCG
        else:
            return("PPG")  # PPG

    elif entropy > resp_threshold_entropy[0] and entropy < resp_threshold_entropy[1]:
        if 1250 > kurtosis > 1100:
            return("PPG")  # PPG
        else:
            return("RESP")  # RESP

    else:
        return("PPG")  # PPG
