# ******************************************************************************
# * @file filters.py
# * @author Pablo Joaquim
# * @brief Several convenient functions to work with Analog filters
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import numpy as np
from scipy import signal as filters
from scipy.signal import lsim

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************
class Butterworth():
    # ******************************************************************************
    # * @brief The __init__() function is called automatically every time the class
    # * is being used to create a new object.
    # ******************************************************************************
    def __init__(self):
        # The self parameter is a reference to the current instance of the class,
        # and is used to access variables that belong to the class.
        pass

    # ******************************************************************************
    # * @brief Returns a string as a representation of the object.
    # ******************************************************************************
    def __repr__(self):
        return '<Metadata(name={self.id!r})>'.format(self=self)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_lowpass(wc, order=5):
        return filters.butter(order, wc, btype='lowpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_highpass(wc, order=5):
        return filters.butter(order, wc, btype='highpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_bandpass(wci, wcs, order=5):
        return filters.butter(order, [wci, wcs], btype='bandpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_bandstop(wci, wcs, order=5):
        return filters.butter(order, [wci, wcs], btype='bandstop', analog=True)

class SignalGenerator():
    # ******************************************************************************
    # * @brief The __init__() function is called automatically every time the class
    # * is being used to create a new object.
    # ******************************************************************************
    def __init__(self):
        # The self parameter is a reference to the current instance of the class,
        # and is used to access variables that belong to the class.
        pass

    # ******************************************************************************
    # * @brief Returns a string as a representation of the object.
    # ******************************************************************************
    def __repr__(self):
        return '<Metadata(name={self.id!r})>'.format(self=self)
    
    # ******************************************************************************
    # * @brief Create a signal based in the time data and the several fourier components 
    # * defined in the signals input in the form [[A,w,phi]]
    # ******************************************************************************    
    def signal(signals, step, tmin, tmax):
        t = np.linspace(tmin, step, tmax, endpoint=False)
        u = 0
        for signal in signals:
            A=signal[0]
            w=signal[1]
            phi=signal[2]
            u = u + A*np.sin(2*np.pi*w*t)
            
        return u,t

class ApplyFilter():
    # ******************************************************************************
    # * @brief The __init__() function is called automatically every time the class
    # * is being used to create a new object.
    # ******************************************************************************
    def __init__(self):
        # The self parameter is a reference to the current instance of the class,
        # and is used to access variables that belong to the class.
        pass

    # ******************************************************************************
    # * @brief Returns a string as a representation of the object.
    # ******************************************************************************
    def __repr__(self):
        return '<Metadata(name={self.id!r})>'.format(self=self)
    
    # ******************************************************************************
    # * @brief Create a signal based in the time data and the several fourier components 
    # * defined in the signals input in the form [[A,w,phi]]
    # ******************************************************************************    
    def eval(h, input, t):
        num = h[0]
        den = h[1]
        tout, output, xout = lsim((num, den), U=input, T=t)
        return output

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************

# ******************************************************************************
# * Function Definitions
# ******************************************************************************


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
