# coding=utf-8
import spidev
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

spi = spidev.SpiDev()

spi.open(0, 0)



ADDA = 11
ADDB = 13
ADDC = 15
ALE = 12
OE = 16
CLK = 23

GPIO.setwarnings(False)
print(ADDA, " TOMAAAA ")
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

# liga o Clock
GPIO.output(CLK, 1)

# seta canal de entrada
GPIO.output(ALE, 1)
time.sleep(2)
GPIO.output(ALE, 0)

# ativa saida
GPIO.output(OE, 1)




