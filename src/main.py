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

import scipy as sp
from analog import filters
from analog import bode
import control

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
        
        pi = 3.14
        fo = 1000
        wc = 2*pi*fo
        wci = 2*pi*500
        wcs = 2*pi*1500
        
        orders = [1,2,3,4]
        plotter = bode.FreqResponse()        
        
        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_lowpass(wc=wc, order=order)
            print("H(s)=", control.tf(num, den))
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - lowpass")

        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_highpass(wc=wc, order=order)
            print("H(s)=", control.tf(num, den))
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - highpass")

        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_bandpass(wci=wci, wcs=wcs, order=order)
            print("H(s)=", control.tf(num, den))
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - bandpass")

        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_bandstop(wci=wci, wcs=wcs, order=order)
            print("H(s)=", control.tf(num, den))
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - bandstop")

        
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
        
        # plt.show()
        
    except RuntimeError:
        print("Finishing...", flush=True)
