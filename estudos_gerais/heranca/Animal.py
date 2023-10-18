class Animal():
    velocidade = 0   
    fadiga = 0

    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def movimentoLento(self, intensidadeAcelerada):
        if intensidadeAcelerada > 50:
            print("Para acelerar mais que 50%, favor CORRER.")
        elif self.fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.velocidade))
            self.fadiga += 10 + self.peso/10
            print("A fadiga total do animal está em {:.2f}".format(self.fadiga))

    def MovimentoRapido(self, intensidadeAcelerada):
        if intensidadeAcelerada < 50:
            print("Para acelerar menos que 50%, favor ANDAR")
        elif self.fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.velocidade))
            self.fadiga += 20 + self.peso/10
            print("A fadiga total do animal está em {:.2f}".format(self.fadiga))
    
    def descansar(self, tempo):
        if self.fadiga - tempo <= 0:
            print("O animal já está denscansado.")
        else:    
            self.fadiga -= tempo
            print("A fadiga total do animal está em {:.2f}".format(self.fadiga))