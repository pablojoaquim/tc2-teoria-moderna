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
from analog import filters
from analog import bode
from scipy.signal import lsim
import matplotlib.pyplot as plt

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
        plotter = bode.FreqResponse()        

        fo = 1000
        wc = 2*np.pi*fo
        wci = 2*np.pi*500
        wcs = 2*np.pi*1500
        orders = [1,2,3,4]
    
        # # Filter definition by poles and zeroes
        # H = []
        # num = np.array([1,10])
        # den = np.polymul(np.array([1,1]), np.array([1,100]))
        # H.append([num, den, "func1"])
        # num = np.array([1,20])
        # den = np.polymul(np.array([1,1]), np.array([1,200]))
        # H.append([num, den, "func2"])
        # plotter.pzplot(H, 200, title="Pole-Zero")
        
        # # Butterworth - lowpass
        # H = []
        # for order in orders:
        #     num, den = filters.Butterworth.butter_lowpass(wc=wc, order=order)
        #     h = control.tf(num, den)
        #     print("H(s)=", h)
        #     H.append([num, den, "order = %d" % order])
        # plotter.plot(H, [fo,-3], "Butterworth - lowpass")
        # plotter.pzplot(H, wc, title="Butterworth - lowpass")

        # # Butterworth - highpass
        # H = []
        # for order in orders:
        #     num, den = filters.Butterworth.butter_highpass(wc=wc, order=order)
        #     h = control.tf(num, den)
        #     print("H(s)=", h)
        #     H.append([num, den, "order = %d" % order])
        # plotter.plot(H, [fo,-3], "Butterworth - highpass")
        # plotter.pzplot(H, wc, title="Butterworth - highpass")

        # # Butterworth - bandpass
        # H = []
        # for order in orders:
        #     num, den = filters.Butterworth.butter_bandpass(wci=wci, wcs=wcs, order=order)
        #     h = control.tf(num, den)
        #     print("H(s)=", h)
        #     H.append([num, den, "order = %d" % order])
        # plotter.plot(H, [fo,-3], "Butterworth - bandpass")
        # plotter.pzplot(H, wc, title="Butterworth - bandpass")        

        # # Butterworth - bandstop
        # H = []
        # for order in orders:
        #     num, den = filters.Butterworth.butter_bandstop(wci=wci, wcs=wcs, order=order)
        #     h = control.tf(num, den)
        #     print("H(s)=", h)
        #     H.append([num, den, "order = %d" % order])
        # plotter.plot(H, [fo,-3], "Butterworth - bandstop")
        # plotter.pzplot(H, wc, title="Butterworth - bandstop")        
        
        # The input signal is the sum of three sinusoidal curves, with frequencies 4 Hz, 40 Hz, and 80 Hz. 
        # The filter should mostly eliminate the 40 Hz and 80 Hz components, leaving just the 4 Hz signal.
        num, den = filters.Butterworth.butter_lowpass(wc=2*np.pi*12, order=5)
        t = np.linspace(0, 1.25, 500, endpoint=False)
        u = (np.cos(2*np.pi*4*t) + 0.6*np.sin(2*np.pi*40*t) + 0.5*np.cos(2*np.pi*80*t))
        
        # Simulate the filter with lsim.
        tout, yout, xout = lsim((num, den), U=u, T=t)
        plt.plot(t, u, 'r', alpha=0.5, linewidth=1, label='input')
        plt.plot(tout, yout, 'k', linewidth=1.5, label='output')
        plt.legend(loc='best', shadow=True, framealpha=1)
        plt.grid(alpha=0.3)
        plt.xlabel('t')
        plt.show()
        
        
        
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
