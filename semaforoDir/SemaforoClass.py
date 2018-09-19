# coding=utf-8
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
__p1 = 0
__p2 = 0
__p3 = 0
__rua = 0


class Semaforo:
    def __init__(self, p1, p2, p3, rua):
        print(p1, "|", p2, "|", p3)
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__rua = rua

        #exit()
        GPIO.setup(p1, GPIO.OUT)
        GPIO.setup(p2, GPIO.OUT)
        GPIO.setup(p3, GPIO.OUT)
        GPIO.setwarnings(False)

        Red   = GPIO.output(p1, 1)
        Yelow = GPIO.output(p2, 1)
        Green = GPIO.output(p3, 1)

        self.teste()

    def abre(self):
        print("Abre: ", self.__rua)
        self.Green = GPIO.output(self.__p3, 0)
        self.Red   = GPIO.output(self.__p1, 1)

    def atencao(self):
        print("Atencao: ", self.__rua)
        self.Green = GPIO.output(self.__p3, 1)
        self.Yelow = GPIO.output(self.__p2, 0)


    def fecha(self):
        print("Fecha: ", self.__rua)
        self.Yelow = GPIO.output(self.__p2, 1)
        self.Red   = GPIO.output(self.__p1, 0)


    def alerta(self):
        return "alerta"

    def teste(self):
        self.Red = GPIO.output(self.__p1, 0)
        self.Yelow = GPIO.output(self.__p2, 0)
        self.Green = GPIO.output(self.__p3, 0)
        time.sleep(3)
        self.Red = GPIO.output(self.__p1, 1)
        self.Yelow = GPIO.output(self.__p2, 1)
        self.Green = GPIO.output(self.__p3, 1)
        time.sleep(2)
        self.Red = GPIO.output(self.__p1, 0)
        time.sleep(1)
        self.Yelow = GPIO.output(self.__p2, 0)
        time.sleep(1)
        self.Green = GPIO.output(self.__p3, 0)
        time.sleep(1)
        self.Red = GPIO.output(self.__p1, 1)
        time.sleep(1)
        self.Yelow = GPIO.output(self.__p2, 1)
        time.sleep(1)
        self.Green = GPIO.output(self.__p3, 1)
        time.sleep(2)
