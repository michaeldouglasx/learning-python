class Endereco:
    def __init__(self, rua_end, num_end, cidade_end):
        self.rua_end = rua_end
        self.num_end = num_end
        self.cidade_end = cidade_end
    def __str__(self):
        return f'{self.rua_end} - {self.num_end} - {self.cidade_end}'

class Pessoa:
    def __init__(self, nome, rua_end, num_end, cidade_end):
        self.nome = nome
        self.endereco = Endereco(rua_end, num_end, cidade_end)
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(self.endereco)

p1 = Pessoa('Michael', 'Rua Santo Antônio',22,'Brasília')
p1.mostrar_dados()