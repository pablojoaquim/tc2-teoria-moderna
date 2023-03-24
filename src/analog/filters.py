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
from scipy import signal as filters

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
    def butter_lowpass(fc, order=5):
        return filters.butter(order, fc, btype='lowpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_highpass(fc, order=5):
        return filters.butter(order, fc, btype='highpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_bandpass(fci, fcs, order=5):
        return filters.butter(order, [fci, fcs], btype='bandpass', analog=True)

    # ******************************************************************************
    # * @brief Obtain a butterworth coefficients according to the parameters definition
    # ******************************************************************************
    def butter_bandstop(fci, fcs, order=5):
        return filters.butter(order, [fci, fcs], btype='bandstop', analog=True)


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
