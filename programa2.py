import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setwarnings(False)

r = GPIO.output(16, 1)
g = GPIO.output(18, 1)
b = GPIO.output(22, 1)


try:
    while(True) :
        decimal = input("entre com valor de 0 a 7")

        if decimal==0:
            intVermelho=0
            intAmarelo=0
            intVerde=0
        elif decimal==1:
            intVermelho=1
            intAmarelo=0
            intVerde=0
        elif decimal==2:
            intVermelho=0
            intAmarelo=1
            intVerde=0
        elif decimal==3:
            intVermelho=1
            intAmarelo=1
            intVerde=0
        elif decimal==4:
            intVermelho=0
            intAmarelo=0
            intVerde=1
        elif decimal==5:
            intVermelho=1
            intAmarelo=0
            intVerde=1
        elif decimal==6:
            intVermelho=0
            intAmarelo=1
            intVerde=1
        elif decimal==7:
            intVermelho=1
            intAmarelo=1
            intVerde=1
        elif decimal<0 or decimal>7:
            decimal = input("somente entre com valores maiores que 0 e menor igual a 7")

#        intVermelho = input("Liga vermelho? 1 ou 0: ")


#        intVerde = input("Liga Verde?: ")


#        intAmarelo = input("Liga Azul?: ")




        if intVermelho==0:
            r = GPIO.output(16, 1)
        else:
            print("Ligou Vermelho")
            r = GPIO.output(16, 0)

        if intVerde==0:
            g = GPIO.output(22, 1)
        else:
            print("Ligou Verde")
            g = GPIO.output(22, 0)

        if intAmarelo==0:
            b = GPIO.output(18, 1)
        else:
            print("Ligou Amarelo")
            b = GPIO.output(18, 0)
            


except KeyboardInterrupt:
    pass

    r.stop
    g.stop
    b.stop