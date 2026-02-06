import numpy as np
import sys, os
from scipy.io.wavfile import write, read
import subprocess
import matplotlib.pyplot as plt

INT16_FAC = (2 ** 15) - 1  # 2^(B-1) - 1, where B = number of bits, e.g. bit rate of 16 
INT32_FAC = (2 ** 31) - 1
INT64_FAC = (2 ** 63) - 1
norm_fact = {'int16': INT16_FAC, 'int32': INT32_FAC, 'int64': INT64_FAC, 'float32': 1.0, 'float64': 1.0}

def wavread(filename):
    """
	Read a sound file and convert it to a normalized floating point array
	filename: name of file to read
	returns fs: sampling rate of file, x: floating point array
    """

    if (os.path.isfile(filename) == False):  # raise error if wrong input file
        raise ValueError("Input file is wrong")

    fs, x = read(filename) # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html

    if (len(x.shape) != 1):  # raise error if wrong sample rate
        raise ValueError("Sample rate should be 44.1kHz")

    if (fs != 44100):  # raise error if more than one channel
        raise ValueError("Sampling rate of input sound should be 44100")

    # scale down and convert audio into floating point number in range of -1 to 1

    """
    print("x before scaling")    
    print("dtype:")
    print(x.dtype.name)  
    plt.plot(x)
    plt.title('x before scaling')
    plt.xlabel('time')
    plt.ylabel('amplitude')    
    plt.show()    
    """
    
    x = np.float32(x) / norm_fact[x.dtype.name] 

    """
    print("x after scaling")    
    print("dtype:")
    print(x.dtype.name) 
    plt.title('x after scaling')
    plt.xlabel('time')
    plt.ylabel('amplitude')    

    plt.plot(x)
    plt.show()    
    """
    
    return fs, x


def wavplay(filename):

    # Play a wav audio file from system using OS calls
    # filename: name of file to read

    if (os.path.isfile(filename) == False):  # raise error if wrong input file
        print("Input file does not exist for wavplay in utilFunctions.py")
    else: 
        if sys.platform == "darwin":   # OS X
            subprocess.call(["afplay", filename])

        elif sys.platform == "linux" or sys.platform == "linux2":   # linux
            subprocess.call(["aplay", filename])
            
        else:
            print("Platform not recognized")
"""
      elif sys.platform == "win32":
            if winsound_imported:
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:
                print("Cannot play sound, winsound could not be imported")
"""
