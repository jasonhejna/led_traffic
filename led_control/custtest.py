#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import Image
from dotstar import Adafruit_DotStar

numpixels = 180 # Number of LEDs in strip

# Load image in RGB format and get dimensions:
filename  = "../yomap.png" # Image file to load
img       = Image.open(filename).convert("RGB")
imgpixels    = img.load()

# Here's how to control the strip from any two GPIO pins:
datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

# Calculate gamma correction table, makes mid-range colors look 'right':
gamma = bytearray(256)
for i in range(256):
	gamma[i] = int(pow(float(i) / 255.0, 2.7) * 255.0 + 0.5)

# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

#color = 0xFF0000        # 'On' color (starts red)
x = 495
y = 231

pixels = [  #x, y
    [970, 459],
    [949, 470],
    [939, 477],
    [928, 488],
    [902, 507],
    [899, 519],
    [904, 538],
    [906, 568]
]

# For each pixel
for i in range(0, numpixels):
    if i < 6:
        value = imgpixels[i][0, 1]   # Read pixel in image
        print value
        print gamma[value[0]], gamma[value[1]], gamma[value[2]]
        strip.setPixelColor(i, # Set pixel in strip
          gamma[value[1]],     # Gamma-corrected green
          gamma[value[0]],     # Gamma-corrected red
          gamma[value[2]])     # Gamma-corrected blue
    else:
	    strip.setPixelColor(i, 0)

strip.show()                     # Refresh strip
