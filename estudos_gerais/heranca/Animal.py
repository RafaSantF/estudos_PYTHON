class Animal():
    __velocidade = 0   
    __fadiga = 0

    # Quando atributos são encapsulados a sintaxe "__" deve ser utilziada sempre que eles forem inseridos no código da própria classe, e encapsulado fora dela (getter, setter)

    def __init__(self, peso, especie, aceleracao):
        self.__peso = peso
        self.__especie = especie
        self.__aceleracao = aceleracao

    def movimentoLento(self, intensidadeAcelerada):
        if intensidadeAcelerada > 50:
            print("Para acelerar mais que 50%, favor CORRER.")
        elif self.__fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.__velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.__velocidade))
            self.__fadiga += (10 * self.__velocidade/10) + self.peso/10
            print("A fadiga total do animal está em {:.2f}".format(self.__fadiga))

    def MovimentoRapido(self, intensidadeAcelerada):
        if intensidadeAcelerada < 50:
            print("Para acelerar menos que 50%, favor ANDAR")
        elif self.__fadiga > 90:
            print("O animal está muito cansado, favor DESCANSAR")
        else:
            self.__velocidade += intensidadeAcelerada/100 * self.aceleracao
            print("O animal está a {:.2f} m/s".format(self.__velocidade))
            self.__fadiga += (20 * self.__velocidade/10) + self.peso/10
            print("A fadiga total do animal está em {:.2f}".format(self.__fadiga))
    
    def descansar(self, tempo):
        if self.__fadiga - tempo <= 0:
            print("O animal já está denscansado.")
        else:    
            self.__fadiga -= tempo
            print("Desanso realizado. A fadiga total do animal está em {:.2f}".format(self.__fadiga))

    # ENCAPSULAMENTO
    def getFadiga(self):
        return self.__fadiga
    
    def setFadiga(self, fadiga):
        self.__fadiga = fadiga

    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso