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
import scipy as sp
import matplotlib.pyplot as plt
# from scipy.signal import butter, lfilter, freqz
# from scipy import signal as filters

from analog import filters
    
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
# * @brief Format Bode plots
# ******************************************************************************
def format_plots(ax, filter_name):
    for column in range(2):
        ax[0].set_title(f'{filter_name} filter')
        ax[0].set_xlabel('Frequency [Hz]')
        ax[0].set_ylabel('|H(jw)| [dB]')
        ax[0].margins(0, 0.1)
        ax[0].grid(b=True, which='both', axis='both')
        ax[0].legend()
        ax[1].set_xlabel('Frequency [Hz]')
        ax[1].set_ylabel('Phase [degrees]')
        ax[1].margins(0, 0.1)
        ax[1].grid(b=True, which='both', axis='both')
        ax[1].legend()
        
# # ******************************************************************************
# # * @brief Obtain a butterworth coefficients according to the parameters definition
# # ******************************************************************************
# def butter_bandpass(lowcut, highcut, fs, order=5, analog = False):
#     return filters.butter(order, [lowcut, highcut], fs=fs, btype='band', analog=analog)

# # ******************************************************************************
# # * @brief Obtain a butterworth coefficients according to the parameters definition
# # ******************************************************************************
# def butter_lowpass(fc, fs=0, order=5, analog = False):
#     if (analog):
#         return filters.butter(order, fc, btype='low', analog=True)
#     else:
#         return filters.butter(order, fc, fs=fs, btype='low', analog=False)

# # ******************************************************************************
# # * @brief Obtain a lowpass filter and apply it to the input signal defined in data
# # ******************************************************************************
# def butter_lowpass_filter(data, cutoff, fs, order=5):
#     b, a = butter_lowpass(cutoff, fs, order)
#     y = filters.lfilter(b, a, data)
#     return y

# # ******************************************************************************
# # * @brief Obtain a bandpass filter and apply it to the input signal defined in data
# # ******************************************************************************
# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandpass(lowcut, highcut, fs, order)
#     y = filters.lfilter(b, a, data)
#     return y
                        
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
        
        fig, ax = plt.subplots(2, 1)

        fc = 1000
        orders = [1,2,3,4]
        for order in orders:
            num, den = filters.Butterworth.butter_lowpass(fc=fc, order=order)
            # num,den = butter_lowpass(fc=fc, order=order, analog = True)
            # b, a = signal.butter(2*(order+1), fc, analog=True)
            w, h = sp.signal.freqs(num, den)
            ax[0].semilogx(w, 20 * np.log10(abs(h)), label="order = %d" % order)
            ax[0].axvline(fc, color='green', linestyle='--')
            ax[0].axhline(-3, color='green', linestyle='--')
            ax[1].semilogx(w, np.unwrap(np.angle(h))*180/np.pi, label="order = %d" % order)
            ax[1].axvline(fc, color='green', linestyle='--')
            
        format_plots(ax,"Butterworth")

        # b1, a1 = filters.butter(1, 1, 'high', analog=True)
        # print("analog filter: ", [b1, a1])

        # # Sample rate and desired cutoff frequencies (in Hz).
        # fs = 5000.0
        # lowcut = 500.0
        # highcut = 1250.0

        # # Plot the frequency response for a few different orders.
        # plt.figure(1)
        # plt.clf()
        
        # orders = [3, 6, 9]
        # for order in orders:
        #     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        #     w, h = filters.freqz(b, a, fs=fs, worN=2000)
        #     plt.plot(w, abs(h), label="order = %d" % order)

        # plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
        #         '--', label='sqrt(0.5)')
        # plt.xlabel('Frequency (Hz)')
        # plt.ylabel('Gain')
        # plt.grid(True)
        # plt.legend(loc='best')

        # orders = [3, 6, 9]
        # for order in orders:
        #     b, a = butter_lowpass(lowcut, fs, order=order)
        #     w, h = filters.freqz(b, a, fs=fs, worN=2000)
        #     plt.plot(w, abs(h), label="order = %d" % order)

        # plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
        #         '--', label='sqrt(0.5)')
        # plt.xlabel('Frequency (Hz)')
        # plt.ylabel('Gain')
        # plt.grid(True)
        # plt.legend(loc='best')

        # # Filter a noisy signal.
        # T = 1
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

        # y = butter_lowpass_filter(x, lowcut, fs, order=6)
        # plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
        # plt.xlabel('time (seconds)')
        # plt.hlines([-a, a], 0, T, linestyles='--')
        # plt.grid(True)
        # plt.axis('tight')
        # plt.legend(loc='upper left')
        
        plt.show()
        
    except RuntimeError:
        print("Finishing...", flush=True)
