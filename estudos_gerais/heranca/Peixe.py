from Animal import Animal

class Peixe(Animal):
    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def pularAgua(forca):
        if super.fadiga > 70:
            print("O animal está muito cansado para pular para fora d'água.")
        else:
            super.fadiga += 30 + super.peso/10 + forca/10
            print("O animal acaba de pular para fora da água e gastou bastante energia")
            print("A fadiga total do animal está em {:.2f}".format(super.fadiga))

