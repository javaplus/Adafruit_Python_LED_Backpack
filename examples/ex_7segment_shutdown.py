import time
from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

print "Turning off display"

def clearDisplay():
    segment.clear()
    # Set hours
    segment.set_digit(0, " ")
    segment.set_digit(1, " ")
    # Set minutes
    segment.set_digit(2, " ")
    segment.set_digit(3, " ")
    segment.write_display()


# Display "BYE" then shutdown
segment.clear()
segment.print_number_str("BYE")
segment.write_display()

# Wait a 1 second 
time.sleep(1.00)

clearDisplay()
