import snowboydecoder
import sys
import signal
import time
from imp import load_source

# Demo code for listening two hotwords at the same time

interrupted = False
DRV2605 = load_source('DRV2605', '/home/pi/Documents/HearingLoss/Adafruit_DRV2605_Library-master/DRV2605.py')

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def vibrate():
    hptc = DRV2605.DRV2605()
    hptc.set_library(1)
    hptc.set_mode(0x00)

    hptc.set_waveform(0, 52)
    hptc.go()
    time.sleep(1)
    hptc.set_waveform(0, 29)
    hptc.go()
    hptc.stop()

def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=vibrate,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
