#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
from dotstar import Adafruit_DotStar

numpixels = 180 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.
# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

# Calculate gamma correction table, makes mid-range colors look 'right':
gamma = bytearray(256)
for i in range(256):
	gamma[i] = int(pow(float(i) / 255.0, 2.7) * 255.0 + 0.5)

# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

#color = 0xFF0000        # 'On' color (starts red)
color = 0xC7DFB7

# For each pixel
for i in range(0, numpixels):
    if i > 90:
	    strip.setPixelColor(i, 199, 223, 183)    # Red, Green, Blue
    else:
	    strip.setPixelColor(i, 0)

strip.show()                     # Refresh strip
