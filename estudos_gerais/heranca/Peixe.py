from Animal import Animal

class Peixe(Animal):
    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def pularAgua(self, forca):
        if self.getFadiga() > 70:
            print("O animal está muito cansado para pular para fora d'água.")
        else:
            self.setFadiga(self.getFadiga() + 30 + self.peso/10 + forca/10) 
            print("O animal acaba de pular para fora da água e gastou bastante energia")
            print("A fadiga total do animal está em {:.2f}".format(self.getFadiga()))

    #TESTANDO MÉTODO SOBRESCRITO --> deve-se apenas criar o método com o mesmo nome da classe mãe.
    def descansar(self, tempo):
        if self.getFadiga() - tempo <= 0:
            print("O animal já está denscansado.")
        else:    
            self.setFadiga(self.getFadiga() - tempo)
            print("O PEIXE parou de nadar. A fadiga total do animal está em {:.2f}".format(self.getFadiga())) 