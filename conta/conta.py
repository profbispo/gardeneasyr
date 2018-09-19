#coding: utf-8

class Conta:
    tipo = ''
    conta = ""
    __saldo = 100
    __saldoAnterior = 0

    def __init__(self, conta, tipo ):
        self.conta=conta
        self.tipo=tipo

    def deposita(self, valor):
        self.__saldoAnterior = self.__saldo
        self.__saldo=self.__saldoAnterior+valor
        print("Depositou: ", valor)

    def saca(self, valor):
        self.__saldoAnterior = self.__saldo
        self.__saldo=self.__saldoAnterior-valor
        print("Sacou: ",valor)

    def getSaldo(self):
        return self.__saldo

    def getDados(self):
        return "Conta: ",self.conta," |, Tipo: ",self.tipo