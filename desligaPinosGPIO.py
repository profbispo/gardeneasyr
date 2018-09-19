# coding=utf-8
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

ADDA = 11
ADDB = 13
ADDC = 15
ALE = 12
OE = 16
CLK = 23

GPIO.setwarnings(False)
GPIO.setup(ADDA, GPIO.OUT)
GPIO.setup(ADDB, GPIO.OUT)
GPIO.setup(ADDC, GPIO.OUT)
GPIO.setup(ALE, GPIO.OUT)
GPIO.setup(OE, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)

GPIO.output(ADDA, 0)
GPIO.output(ADDB, 0)
GPIO.output(ADDC, 0)
GPIO.output(OE, 0)
GPIO.output(ALE, 0)
GPIO.output(OE, 0)
GPIO.output(CLK, 0)
