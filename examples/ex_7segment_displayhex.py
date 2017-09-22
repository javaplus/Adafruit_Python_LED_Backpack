import sys
import time
from Adafruit_LED_Backpack import SevenSegment


segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

inputHex = sys.argv[1]
position = sys.argv[2] #get the position on the display to put this.

print "value of argument=" + inputHex
print "value of position=" + position
hexValue = int(inputHex, 16)

print "Hex value=" + hex(hexValue)
print "Will display value for 5 seconds"
segment.clear()
segment.set_digit_raw(position, hexValue)
segment.write_display()
time.sleep(5.0)



