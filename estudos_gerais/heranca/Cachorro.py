from Animal import Animal

class Peixe(Animal):
    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def brincarBola(tempo):
        if super.fadiga > 70:
            print("O animal está muito cansado para brincar com uma bola.")
        else:
            super.fadiga += 30 + super.peso/10 + tempo/10
            print(f"O animal brincou com uma bola por {tempo} minutos")
            print("A fadiga total do animal está em {:.2f}".format(super.fadiga))


