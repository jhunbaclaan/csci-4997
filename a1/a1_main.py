## IMPORTANT: RUN FROM ROOT DIRECTORY!!! (csci-4997/) 
# for some god forsaken reason this just wont run if you try running from ../a1
# i'll label each part with how you should run them

# tester file for all a1 methods

import os
import sys
sys.path.insert(0, os.path.abspath('a1/4997-tools-v4/software/models'))
from a1.A1Part1 import readAudio

# part 1 -- run with python -m a1.a1_main
print(readAudio('piano.wav'))  # test the function