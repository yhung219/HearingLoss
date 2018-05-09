# Copyright (c) 2016 Dave Clarke Design 
# Author: Dave Clarke
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from __future__ import division
import time
import math


# Registers/etc:
DRV2605_ADDR            =0x5A

DRV2605_REG_STATUS      =0x00
DRV2605_REG_MODE        =0x01
DRV2605_MODE_INTTRIG    =0x00
DRV2605_MODE_EXTTRIGEDGE =0x01
DRV2605_MODE_EXTTRIGLVL  =0x02
DRV2605_MODE_PWMANALOG  =0x03
DRV2605_MODE_AUDIOVIBE  =0x04
DRV2605_MODE_REALTIME   =0x05
DRV2605_MODE_DIAGNOS    =0x06
DRV2605_MODE_AUTOCAL    =0x07


DRV2605_REG_RTPIN       =0x02
DRV2605_REG_LIBRARY     =0x03
DRV2605_REG_WAVESEQ1    =0x04
DRV2605_REG_WAVESEQ2    =0x05
DRV2605_REG_WAVESEQ3    =0x06
DRV2605_REG_WAVESEQ4    =0x07
DRV2605_REG_WAVESEQ5    =0x08
DRV2605_REG_WAVESEQ6    =0x09
DRV2605_REG_WAVESEQ7    =0x0A
DRV2605_REG_WAVESEQ8    =0x0B

DRV2605_REG_GO          =0x0C
DRV2605_REG_OVERDRIVE   =0x0D
DRV2605_REG_SUSTAINPOS  =0x0E
DRV2605_REG_SUSTAINNEG  =0x0F
DRV2605_REG_BREAK       =0x10
DRV2605_REG_AUDIOCTRL   =0x11
DRV2605_REG_AUDIOLVL    =0x12
DRV2605_REG_AUDIOMAX    =0x13
DRV2605_REG_RATEDV      =0x16
DRV2605_REG_CLAMPV      =0x17
DRV2605_REG_AUTOCALCOMP =0x18
DRV2605_REG_AUTOCALEMP  =0x19
DRV2605_REG_FEEDBACK    =0x1A
DRV2605_REG_CONTROL1    =0x1B
DRV2605_REG_CONTROL2    =0x1C
DRV2605_REG_CONTROL3    =0x1D
DRV2605_REG_CONTROL4    =0x1E
DRV2605_REG_VBAT        =0x21
DRV2605_REG_LRARESON    =0x22

class DRV2605(object):
    """DRV2605 Haptic / Vibration controller."""

    def __init__(self, address=DRV2605_ADDR, i2c=None, **kwargs):
        """Initialize the DRV2605."""
        # Setup I2C interface for the device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)

        self._device.write8(DRV2605_REG_MODE, 0x00) #out of standby
    
        self._device.write8(DRV2605_REG_RTPIN, 0x00) # no real-time-playback
  
        self._device.write8(DRV2605_REG_WAVESEQ1, 1) # strong click
        self._device.write8(DRV2605_REG_WAVESEQ2, 0)
  
        self._device.write8(DRV2605_REG_OVERDRIVE, 0) # no overdrive
  
        self._device.write8(DRV2605_REG_SUSTAINPOS, 0)
        self._device.write8(DRV2605_REG_SUSTAINNEG, 0)
        self._device.write8(DRV2605_REG_BREAK, 0)
        self._device.write8(DRV2605_REG_AUDIOMAX, 0x64)

        # ERM open loop
  
        # turn off N_ERM_LRA
        n_erm_lra = self._device.readU8(DRV2605_REG_FEEDBACK)
        n_erm_lra = n_erm_lra & 0x7F
        self._device.write8(DRV2605_REG_FEEDBACK, n_erm_lra)
        
        # turn on ERM_OPEN_LOOP
        erm_open_loop = self._device.readU8(DRV2605_REG_CONTROL3)
        erm_open_loop = erm_open_loop | 0x20
        self._device.write8(DRV2605_REG_CONTROL3, erm_open_loop)        
 

    def set_waveform(self, slot, w):
        self._device.write8(DRV2605_REG_WAVESEQ1+slot, w)

    def set_library(self, lib):
        self._device.write8(DRV2605_REG_LIBRARY, lib)

    def go(self):
        self._device.write8(DRV2605_REG_GO, 1)        

    def stop(self):
        self._device.write8(DRV2605_REG_GO, 0) 

    def set_mode(self, mode):
        self._device.write8(DRV2605_REG_MODE, mode)
       
    def set_realtime_value(self, rtp):
        self._device.write8(DRV2605_REG_RTPIN, rtp)

    def use_erm(self):
        use_erm = self._device.readU8(DRV2605_REG_FEEDBACK)
        use_erm = use_erm & 0x7F
        self._device.write8(DRV2605_REG_FEEDBACK, use_erm)       

        
    def use_lra(self):
        use_lra = self._device.readU8(DRV2605_REG_FEEDBACK)
        use_lra = use_lra | 0x80
        self._device.write8(DRV2605_REG_FEEDBACK, use_lra)
