import time
from imp import load_source

DRV2605 = load_source('DRV2605', '/home/pi/Documents/HearingLoss/Adafruit_DRV2605_Library-master/DRV2605.py')


def main():
    hptc = DRV2605.DRV2605()
    hptc.set_library(1)
    hptc.set_mode(0x00)

    while True:
        hptc.set_waveform(0, 51)
        hptc.set_waveform(1, 75)  # object coming from the right
        hptc.set_waveform(1, 0)  # object dead ahead
        hptc.set_waveform(1, 87)  # object coming from the left
        hptc.go()
        time.sleep(0.5)
        hptc.stop()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
