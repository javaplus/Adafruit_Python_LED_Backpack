#!/usr/bin/python

import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

print "Press CTRL+Z to exit"

# Continually update the time on a 4 char, 7-segment display
counter = 9999
while(counter>8999):
  
  hour = int(counter/100)
  minute = int(counter % 100)


  segment.clear()
  # Set hours
  segment.set_digit(0, int(hour / 10))     # Tens
  segment.set_digit(1, hour % 10)          # Ones
  # Set minutes
  segment.set_digit(2, int(minute / 10))   # Tens
  segment.set_digit(3, minute % 10)        # Ones
  # Toggle colon
  #segment.set_colon(counter % 2)              # Toggle colon at 1Hz

  # Write the display buffer to the hardware.  This must be called to
  # update the actual display LEDs.
  segment.write_display()

  # Wait a quarter second (less than 1 second to prevent colon blinking getting$
  time.sleep(0.25)
  counter=counter-1
segment.clear()

