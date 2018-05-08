#!/usr/bin/python

# python program to communicate with an MCP3008

# Import our SpiDe wrapper and out sleep function

import spidev
import os

# Establish SPI device on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0, 0)


def getAdc(channel):
    # check for valid channel
    if ((channel > 7) or (channel < 0)):
        return -1

    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8 + channel) << 4, 0])

    # Filter data bits from returned bits
    adcOut = ((r[1] & 3) << 8) + r[2]

    # Print out 0 - 1023 value and percentage
    if (adcOut > 700):
        os.system("echo 'WOOF! WOOF!' | mail 2537320033@messaging.sprintpcs.com")


while True:
    getAdc(0)