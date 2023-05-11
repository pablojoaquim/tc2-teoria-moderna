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
# import control.matlab as ml
import control

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
      for column in range(3):
          ax[0].set_title(f'{title}')
          ax[0].set_xlabel('Frequency [Hz]')
          ax[0].set_ylabel('|H(jw)| [dB]')
          ax[0].margins(0, 0.1)
          ax[0].grid(b=True, which='both', axis='both')
          ax[0].legend([""])
          ax[1].set_xlabel('Frequency [Hz]')
          ax[1].set_ylabel('Phase [degrees]')
          ax[1].margins(0, 0.1)
          ax[1].grid(b=True, which='both', axis='both')
          ax[1].legend([""])
          ax[2].set_xlabel('Frequency [Hz]')
          ax[2].set_ylabel('GroupDelay [seconds]')
          ax[2].margins(0, 0.1)
          ax[2].grid(b=True, which='both', axis='both')
          ax[2].legend([""])
        
    # ******************************************************************************
    # * @brief Plot the frequecy response of each transfer.
    # * H is a list of as many transfer functions you want to plot in the form [num, den, label]
    # ******************************************************************************
    def plot(self, H, marker=[0,0], title = ""):
      fig, ax = plt.subplots(3, 1)
      
      for h in H:
        num = h[0]
        den = h[1]
        label = ""
        if (len(h)>=2):
          label = h[2]

        # Calc the mod and phase
        w, mag, phase = sp.signal.bode((num,den))

        # Calc the group delay
        grpdelay = []
        for i in (range(len(w)-1)):
            grpdelay.append(-1*(phase[i]-phase[i+1])/(w[i]-w[i+1]))
        grpdelay = grpdelay + grpdelay[-1:] # Repeat the last elements to have an array of the same dimmension as w[]

        # Plot the module of the transfer
        ax[0].semilogx(w/(2*np.pi), mag, label=label)    # Bode magnitude plot
        if (marker[0] != 0):
          fc = marker[0]
          ax[0].axvline(fc, color='green', linestyle='--')
        if (marker[1] != 0):
          mod = marker[1]
          ax[0].axhline(mod, color='green', linestyle='--')

        # Plot the phase of the transfer
        ax[1].semilogx(w/(2*np.pi), phase)  # Bode phase plot
        if (marker[0] != 0):
          fc = marker[0]
          ax[1].axvline(fc, color='green', linestyle='--')

        # Plot the group delay of the transfer
        ax[2].semilogx(w/(2*np.pi), grpdelay)  # Bode phase plot
        if (marker[0] != 0):
          fc = marker[0]
          ax[2].axvline(fc, color='green', linestyle='--')
          
      # Format the Bode plots
      self.__format_plots(ax, title)
      
      # Finally show the plots
      plt.show()

    # ******************************************************************************
    # * @brief Plot the zero-pole diagram
    # * H is a list of as many transfer functions you want to plot in the form [num, den, label]
    # ******************************************************************************
    def pzplot(self, H, wo=0, title = ""):
      fig, ax = plt.subplots(1, 1)
           
      for h in H:
        num = h[0]
        den = h[1]
        label = ""
        if (len(h)>=2):
          label = h[2]
        (zeros,poles,gain) = sp.signal.tf2zpk(num, den)
        
        # Plot the poles and set marker properties
        p = plt.plot(poles.real, poles.imag, 'x', markersize=9, alpha=1, label=label)
    
        # Plot the zeros and set marker properties
        z = plt.plot(zeros.real, zeros.imag,  'o', markersize=9, 
             color='none', alpha=1,
             markeredgecolor=p[0].get_color(), # same color as poles
             label=label)
        
      if (wo != 0):
        circle = plt.Circle((0, 0), radius=wo, fill = False, color='black', ls='solid', alpha=0.3)
        ax.add_patch(circle)
      
      plt.axis('square')
      plt.xlabel('Real')
      plt.ylabel('Imag')
      plt.title(f'{title}')
      plt.grid(b=True, which='both', axis='both')
      plt.legend()
      plt.show()
  
    # ******************************************************************************
    # * @brief Plot the bode diagram of each transfer.
    # ******************************************************************************
    def bode(self, H):
      control.bode_plot(H, grid=True)
      plt.show()      
      
    # ******************************************************************************
    # * @brief Plot the pole-zero diagram of the system H
    # ******************************************************************************
    def pzmap(self, H):
      control.pzmap(H)
      plt.show()

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

