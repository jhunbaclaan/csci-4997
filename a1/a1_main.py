## IMPORTANT: RUN FROM ROOT DIRECTORY!!! (csci-4997/) 
# for some god forsaken reason this just wont run if you try running from ../a1

# refuses to run in vsc, so use console
# please please PLEASE run with THIS ---> python -m a1.a1_main

# tester file for all a1 methods

import os
import sys
sys.path.insert(0, os.path.abspath('a1/4997-tools-v4/software/models'))
from a1.A1Part1 import readAudio
from a1.A1Part2 import minMaxAudio

print("part 1:",readAudio('piano.wav'))
print("part 2:", minMaxAudio('oboe-A4.wav'))  # test part 2