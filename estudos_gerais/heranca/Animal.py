class Animal():
    velocidade = 0   
    fadiga = 0

    def __init__(self, peso, especie, aceleracao):
        self.peso = peso
        self.especie = especie
        self.aceleracao = aceleracao

    def andar(self, intensidadeAcelerada):
        if intensidadeAcelerada > 50:
            print("Para acelerar mais que 50%, favor CORRER.")
        elif self.fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.velocidade))
            self.fadiga += 20

    def correr(self, intensidadeAcelerada):
        if intensidadeAcelerada < 50:
            print("Para acelerar menos que 50%, favor ANDAR")
        elif self.fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.velocidade))
            self.fadiga += 50
    
    def descansar(self, tempo):
        #MODELAR DESCANSO PARA FADIGA NÃO FICAR NEGATIVO <------------------------------------------------
        #FADIGA DEVE LEVAR EM CONSIDERAÇÃO O PESO E IDADE DO ANIMAL <------------------------------------------------
        self.fadiga -= tempo
        if self.fadiga < 50:
            print("O animal está com metade de disposição e já consegue voltar às atividades.")