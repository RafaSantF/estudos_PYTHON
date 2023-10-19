from Animal import Animal

class Cachorro(Animal):
    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def brincarBola(self, tempo):
        if self.fadiga > 70:
            print("O animal está muito cansado para brincar com uma bola.")
        else:
            self.fadiga += 30 + self.peso/10 + tempo/10
            print(f"O animal brincou com uma bola por {tempo} minutos")
            print("A fadiga total do animal está em {:.2f}".format(self.fadiga))


