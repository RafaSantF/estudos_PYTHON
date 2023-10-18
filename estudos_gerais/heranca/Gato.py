from Animal import Animal

class Gato(Animal):
    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def subirMuro(self):
        if super.fadiga > 70:
            print("O animal está muito cansado para subir um muro.")
        else:
            super.fadiga += 30 + super.peso/10
            print("O animal está em cima de um muro. Muito cuidado ao descer!")
            print("A fadiga total do animal está em {:.2f}".format(super.fadiga))