import RPi.GPIO as GPIO
import time

# Use GPIO names
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup GPIO #26 and #19 as outputs
# with initially low position
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

# Loop 10 times
for i in range(10):
    # Set #26 to high and #19 to low
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    # Wait 1 second
    time.sleep(1)
    # Set #26 to low and #19 to high
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    # Wait 1 second
    time.sleep(1)
# Reset #26 and #19
GPIO.output(26, GPIO.LOW)
GPIO.output(19, GPIO.LOW)