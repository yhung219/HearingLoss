from __future__ import print_function
from sys import platform
from os import system
import time
import RPi.GPIO as GPIO
#import DRV2605
#haptic = DRV2605.DRV2605()
effect = 1 
#import DRV2605 module from location
from imp import load_source
DRV2605 = load_source('DRV2605', '/home/pi/Adafruit_DRV2605_Library/DRV2605.py')
haptic = DRV2605.DRV2605()
 
def haptic_setup():
    haptic.set_library(5)
  
    # I2C trigger by sending 'go' command 
    # default, internal trigger when sending GO command
    haptic.set_mode(0x00) 



def main():
    global effect    
    # set the effect to play
    haptic.set_waveform(0, effect)  # play effect 
    haptic.set_waveform(1, 0)       # end waveform

    # play the effect!
    haptic.go();

    # wait a bit
    time.sleep(0.5)

    effect += 1
    
    if (effect > 117):
        effect = 1

    print(effect)    


if __name__ == '__main__':
  
    haptic_setup()
    effect = 1    
    while True:
        main()
        
