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

pixels = [[1323,346],[1323,342],[1323,338],[1324,331],[1325,326],[1326,321],[1326,316],[1326,307],[1324,299],[1323,295],[1322,290],[1321,284],[1320,277],[1319,270],[1318,263],[1317,257],[1317,252],[1317,248],[1317,245],[1316,224],[1316,222],[1315,217],[1314,212],[1314,209],[1311,204],[1309,201],[1306,198],[1302,194],[1298,190],[1294,185],[1289,182],[1284,178],[1280,174],[1275,170],[1271,165],[1267,161],[1263,157],[1259,153],[1255,149],[1250,147],[1246,143],[1241,139],[1236,136],[1235,134],[1231,132],[1228,129],[1226,125],[1209,106],[1206,102],[1203,99],[1199,95],[1196,92],[1192,88],[1185,85],[1180,84],[1175,83],[1170,82],[1164,82],[1158,82],[1153,82],[1144,83],[1137,82],[1128,82],[1121,82],[1108,82],[1099,82],[1091,82],[1084,83],[1076,85]]

# For each pixel
for i in range(numpixels):
    if i < 40:
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
