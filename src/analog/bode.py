# ******************************************************************************
# * @file filters.py
# * @author Pablo Joaquim
# * @brief Several convenient functions to plot the filters frequecy response
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************
class FreqResponse():
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
    # * @brief Format the Bode plots
    # ******************************************************************************
    def __format_plots(self, ax, title):
      for column in range(2):
          ax[0].set_title(f'{title}')
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
        
    # ******************************************************************************
    # * @brief Plot the frequecy response of each transfer.
    # * H is a list of as many transfer functions you want to plot in the form [num, den, order]
    # ******************************************************************************
    def plot(self, H, marker=[0,0], title = ""):
      fig, ax = plt.subplots(2, 1)
      
      for h in H:
        num = h[0]
        den = h[1]
        order = h[2]
        w, h = sp.signal.freqs(num, den)

        # Plot the module of the transfer
        ax[0].semilogx(w, 20 * np.log10(abs(h)), label="order = %d" % order)
        if (marker[0] != 0):
          fc = marker[0]
          ax[0].axvline(fc, color='green', linestyle='--')
        if (marker[1] != 0):
          mod = marker[1]
          ax[0].axhline(mod, color='green', linestyle='--')

        # Plot the phase of the transfer
        ax[1].semilogx(w, np.unwrap(np.angle(h))*180/np.pi, label="order = %d" % order)
        if (marker[0] != 0):
          fc = marker[0]
          ax[1].axvline(fc, color='green', linestyle='--')

      # Format the Bode plots
      self.__format_plots(ax, title)
      
      # Finally show the plots
      plt.show()

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

