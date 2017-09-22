#!/usr/bin/python

import time

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

print "Press CTRL+Z to exit"

def clearDisplay():
    segment.clear()
    # Set hours
    segment.set_digit(0, " ")
    segment.set_digit(1, " ")
    # Set minutes
    segment.set_digit(2, " ")
    segment.set_digit(3, " ")
    segment.write_display()


# Continually update the time on a 4 char, 7-segment display
counter = 99.99
while(counter>9.99):
    segment.clear()
    segment.print_number_str(str(counter))
   
    # Toggle colon
    #segment.set_colon(counter % 2)              # Toggle colon at 1Hz

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(0.05)
    counter=counter-0.01

clearDisplay()

