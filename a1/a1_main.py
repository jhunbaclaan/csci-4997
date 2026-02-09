## IMPORTANT: RUN FROM ROOT DIRECTORY!!! (csci-4997/) 
# for some god forsaken reason this just wont run if you try running from ../a1
# this MIGHT just be a macos only issue. run it from ../csci-4997 and you'll be fine

# refuses to run in vsc, so use console
# note to self: please please PLEASE run with THIS ---> python3 -m a1.a1_main
# this wont be relevant to you if your regular python installation was installed to PATH correctly but... yeah dont ask

# tester file for all a1 methods

import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath('a1/4997-tools-v4/software/models'))
from a1.A1Part1 import readAudio
from a1.A1Part2 import minMaxAudio
from a1.A1Part3 import hopSamples

print("part 1:",readAudio('piano.wav'))
print("part 2:", minMaxAudio('oboe-A4.wav'))  # test part 2
print("part 3:", hopSamples(np.arange(10), 2))  # test part 3