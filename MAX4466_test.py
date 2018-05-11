#!/usr/bin/python
# python program to communicate with an MCP3008

# Import our SpiDe wrapper and out sleep function

import spidev
from light import Light

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

    # If adcOut is greater than 700 send a text via email through terminal
    if (adcOut > 700):
        led.blink(16)


while True:
    getAdc(0)
