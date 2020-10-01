class Carro:
    global vel_max
    vel_max = 180
    global vel_min
    vel_min = 0
    def __init__(self, delta=5,vel_atual = 0):
        self.delta = delta
        self.vel_atual = vel_atual
    

    def acelerar(self):
        if ((self.vel_atual <= vel_max) and ((vel_max - self.vel_atual) >= self.delta)):
            self.vel_atual = self.vel_atual + self.delta
        elif ((self.vel_atual <= vel_max) and ((vel_max - self.vel_atual) < self.delta)):
            self.vel_atual = vel_max
        if (self.vel_atual >= 180):
            #print(f'Velocidade maxima!!!!')
            return f'Velocidade maxima!!!!'

    def frear(self):
        if ((self.vel_atual >= vel_min) and ((self.vel_atual - self.delta) >= vel_min)):
            self.vel_atual = self.vel_atual - self.delta
        if ((self.vel_atual <= vel_max) and ((self.vel_atual - self.delta) < vel_min )):
            self.vel_atual = vel_min
        if (self.vel_atual <= 0):
            print("Carro está parado!!")


if __name__ == "__main__":
    c1 = Carro(delta=33)
    """
    for _ in range(50):
        if ( (vel_max - c1.vel_atual) <= c1.delta):
            break
        else: 
            c1.acelerar()
            print(c1.vel_atual)
            """

    c1.acelerar()
    c1.acelerar()
    c1.acelerar()
    c1.acelerar()
    print(c1.vel_atual)
    c1.frear()
    c1.frear()
    c1.frear()
    c1.frear()
    c1.frear()
    print(c1.vel_atual)

        
        