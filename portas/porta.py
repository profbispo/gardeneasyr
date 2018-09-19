#coding: utf-8
#Modulo portas apenas para teste de POO
class Porta:

    nome =""
    material=""
    cor=""
    largura=0
    altura=0
    espessura=0

    # metodo construtor, só roda uma vez, quando um aporta é instanciada (Criada)
    def __init__(self, nome, material ):
        self.nome=nome
        self.material=material
        print("Rodei uma vez para a porta: ",nome)



    def getNome(self):
        return self.nome

    def getMaterial(self):
        return self.material

    def setCor(self, cor):
        self.cor=cor

    def setDimenssoes(self, largura, altura, espessura):
        self.largura=largura
        self.altura=altura
        self.espessura=espessura
        print("Foi setadoos valores: Largura= ",largura,", altura= ",altura," e espessura= ",espessura)

    def getDimenssoes(self):
        return self.largura,self.altura,self.espessura
