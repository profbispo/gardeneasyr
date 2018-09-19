# coding=utf-8

from semaforoDir import SemaforoClass

import time

rua1 = SemaforoClass.Semaforo(16, 18, 22, "rua1")
rua2 = SemaforoClass.Semaforo(29, 31, 33, "rua2")

tes = None

while (tes != 0) and (tes != 1):
    tes = input("O Teste foi ok? (0/1)")
    print("olha o valor: ", tes)

if tes == 1:
    while True:
        rua1.abre()
        rua2.fecha()
        time.sleep(10)
        rua1.atencao()
        time.sleep(3)
        rua1.fecha()
        rua2.abre()
        time.sleep(10)
        rua2.atencao()
        time.sleep(3)
else:
    print("Teste Falhou, não será executado")
