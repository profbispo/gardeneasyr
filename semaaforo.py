import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setwarnings(False)

r = GPIO.output(16, 1)
g = GPIO.output(18, 1)
b = GPIO.output(22, 1)


while(True):
    g = GPIO.output(22, 1)
    time.sleep(3)
    g = GPIO.output(22, 1)
    b = GPIO.output(18, 0)
    time.sleep(3)
    b = GPIO.output(18, 1)
    r = GPIO.output(16, 0)
    time.sleep(15)
    r = GPIO.output(16, 1)

