#!/usr/bin/python
# python program to communicate with an MCP3008

# Import our SpiDe wrapper and out sleep function

from time import sleep
import spidev
from gpiozero import LED
from gpiozero import MCP3008

# Establish SPI device on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0, 0)

# LED pin
led = LED(16)

#Define Variables
delay = 0.5
chan = MCP3008(channel=0)


def getAdc(chan):
    # check for valid channel
    if chan > 7 or chan < 0:
        return -1
        print(chan)

    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8 + chan) << 4, 0])
    print (r)

    # Filter data bits from returned bits
    adcOut = ((r[1] & 3) << 8) + r[2]
    print(adcOut)

    # If adcOut is greater than 700 send a text via email through terminal
    if (adcOut > 400):
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)
        print('heard')

while True:
    getAdc(0)

