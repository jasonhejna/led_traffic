#!/usr/bin/python

# Import image, and sample colors in various locations
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

import Image
from dotstar import Adafruit_DotStar
from pixel_coord_data import main_strand

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

pixels = main_strand()

# For each LED pixel
for i in range(numpixels):
    if i < 66:
        value = imgpixels[pixels[i][0], pixels[i][1]]   # Read pixel in image
        print value
        print gamma[value[0]], gamma[value[1]], gamma[value[2]]
        strip.setPixelColor(i, # Set pixel in strip
          gamma[value[1]],     # Gamma-corrected green
          gamma[value[0]],     # Gamma-corrected red
          gamma[value[2]])     # Gamma-corrected blue
    else:
	    strip.setPixelColor(i, 0)

strip.show()                     # Refresh strip
