#sounddevice
#scipy

import sounddevice
from scipy.io.wavfile import write

second = int(input("How many second you need to record: "))
print("Recording Started..")
recording = sounddevice.rec((second*44100), channels=2) #framerate 44100
sounddevice.wait()
filename = input("Enter file name you want to save: ")
write(filename, 44100, recording)
print('Record Done.')