class Cpu:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    def __str__(self):
        return f'Modelo{self.modelo}, Velocidade {self.velocidade}'

class Ram:
    def __init__(self, capacidade):
        self.capacidade = capacidade

    def __str__(self):
        return f'Capacidade {self.capacidade}'

class Computador:
    def __init__(self, marca, modelo, velocidade, capacidade):
        self.marca = marca
        self.cpu = Cpu(modelo, velocidade)
        self.ram = Ram(capacidade)
    def mostrar_especificacoes(self):
        print(self.marca)
        print(self.cpu)
        print(self.ram)

computador1 = Computador('ACER', "NITRO 5", 10000, 10)
computador1.mostrar_especificacoes()


