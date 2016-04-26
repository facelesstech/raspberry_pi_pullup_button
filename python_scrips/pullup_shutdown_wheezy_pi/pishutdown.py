#import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
import os

# Define a function to keep script running
def loop():
    raw_input()

# Define a function to run when an interrupt is called
def shutdown(pin):
    GPIO.setup(16, GPIO.OUT) # Set up pin 16 as an output
    GPIO.output(16, True) # Turn on pin 16 (LED)
    os.system("sudo shutdown -h now") # Shutdown command

GPIO.setmode(GPIO.BOARD) # Set pin numbering to board numbering
#gpio.setup(15, gpio.IN) # Set up pin 15 as an input
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(15, GPIO.RISING, callback=shutdown, bouncetime=200) #Set up an interrupt to look for button presses
 
loop() # Run the loop function to keep script running
