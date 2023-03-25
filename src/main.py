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

import control
import numpy as np
from analog import filters
from analog import bode
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
    
        # Filter definition by poles and zeroes
        H = []
        num = np.array([1,10])
        den = np.polymul(np.array([1,1]), np.array([1,100]))
        H.append([num, den, "func1"])
        num = np.array([1,20])
        den = np.polymul(np.array([1,1]), np.array([1,200]))
        H.append([num, den, "func2"])
        plotter.pzplot(H, 200, title="Pole-Zero")
        h = control.tf(num, den)
        plotter.bode(h)
        
        # Butterworth - lowpass
        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_lowpass(wc=wc, order=order)
            h = control.tf(num, den)
            print("H(s)=", h)
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - lowpass")
        plotter.pzplot(H, wc, title="Butterworth - lowpass")

        # Butterworth - highpass
        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_highpass(wc=wc, order=order)
            h = control.tf(num, den)
            print("H(s)=", h)
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - highpass")
        plotter.pzplot(H, wc, title="Butterworth - highpass")

        # Butterworth - bandpass
        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_bandpass(wci=wci, wcs=wcs, order=order)
            h = control.tf(num, den)
            print("H(s)=", h)
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - bandpass")
        plotter.pzplot(H, wc, title="Butterworth - bandpass")        

        # Butterworth - bandstop
        H = []
        for order in orders:
            num, den = filters.Butterworth.butter_bandstop(wci=wci, wcs=wcs, order=order)
            h = control.tf(num, den)
            print("H(s)=", h)
            H.append([num, den, "order = %d" % order])
        plotter.plot(H, [fo,-3], "Butterworth - bandstop")
        plotter.pzplot(H, wc, title="Butterworth - bandstop")        
        
        # Test a filter time response
        # The input signal is the sum of three sinusoidal curves, with frequencies 4 Hz, 40 Hz, and 80 Hz. 
        # The filter should mostly eliminate the 40 Hz and 80 Hz components, leaving just the 4 Hz signal.
        num, den = filters.Butterworth.butter_lowpass(wc=2*np.pi*12, order=5)
        h = [num, den]
        inputSignal,t = filters.SignalGenerator.signal([[1,4,np.pi/2], [0.6,40,0], [0.5,80,np.pi/2]], 1.25, 0, 500)
        outputSignal = filters.ApplyFilter.eval(h, inputSignal, t)
        plt.plot(t, inputSignal, 'r', alpha=0.5, linewidth=1, label='input')
        plt.plot(t, outputSignal, 'k', linewidth=1.5, label='output')
        plt.legend(loc='best', shadow=True, framealpha=1)
        plt.grid(alpha=0.3)
        plt.xlabel('t')
        plt.show()
        
    except RuntimeError:
        print("Finishing...", flush=True)
