# ******************************************************************************
# * @file main.py
# * @author Pablo Joaquim
# * @brief The entry point
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
    
# ******************************************************************************
# * Objects Declarations
# ******************************************************************************
    
# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

# ******************************************************************************
# * Function Definitions
# ******************************************************************************
# ******************************************************************************
# * @brief Obtain a butterworth coefficients according to the parameters definition
# ******************************************************************************
def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

# ******************************************************************************
# * @brief Obtain a filter and apply it to the input signal defined in data
# ******************************************************************************
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
                        
# ******************************************************************************
# * @brief The handler for the termination signal handler
# ******************************************************************************
def sigintHandler(signum, frame):
    global running
    running = False
    print('Signal handler called with signal', signum)
    raise RuntimeError("Terminating...")

# ******************************************************************************
# * @brief The main entry point
# ******************************************************************************
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigintHandler)

    try:
        print("Initializing...", flush=True)

        # Sample rate and desired cutoff frequencies (in Hz).
        fs = 5000.0
        lowcut = 500.0
        highcut = 1250.0

        # Plot the frequency response for a few different orders.
        plt.figure(1)
        plt.clf()
        
        orders = [3, 6, 9]
        for order in orders:
            b, a = butter_bandpass(lowcut, highcut, fs, order=order)
            w, h = freqz(b, a, fs=fs, worN=2000)
            plt.plot(w, abs(h), label="order = %d" % order)

        plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
                '--', label='sqrt(0.5)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')

        # # Filter a noisy signal.
        # T = 0.05
        # nsamples = T * fs
        # t = np.arange(0, nsamples) / fs
        # a = 0.02
        # f0 = 600.0
        # x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
        # x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
        # x += a * np.cos(2 * np.pi * f0 * t + .11)
        # x += 0.03 * np.cos(2 * np.pi * 2000 * t)
        # plt.figure(2)
        # plt.clf()
        # plt.plot(t, x, label='Noisy signal')

        # y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
        # plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
        # plt.xlabel('time (seconds)')
        # plt.hlines([-a, a], 0, T, linestyles='--')
        # plt.grid(True)
        # plt.axis('tight')
        # plt.legend(loc='upper left')

        plt.show()
        
    except RuntimeError:
        print("Finishing...", flush=True)
