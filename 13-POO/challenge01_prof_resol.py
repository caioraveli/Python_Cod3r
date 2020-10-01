class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        # so para encurtar o nome das variaveis
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self,delta=5):
        #primeiro faço o calculo
        nova = self.velocidade_atual - delta
        # aqui amarro sempre a velocidade no minimo 0
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))
    
    for _ in range(10):
        print(c1.frear(delta=20))
    