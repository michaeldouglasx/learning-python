

class Capitulo:
    def __init__(self, titulo, numero):
        self.titulo = titulo
        self.numero = numero
    def __str__(self):
        return f'{self.titulo} - {self.numero}'

class Livro:
    def __init__(self, titulo_livro, autor):
        self.titulo_livro = titulo_livro
        self.autor = autor
        self.capitulos = []

    def add_capitulo(self,numero_capitulo,titulo_capitulo):
        new_capitulo = Capitulo(titulo_capitulo, numero_capitulo)
        self.capitulos.append(new_capitulo)

    def getSumario(self):
        for capitulo in self.capitulos:
            print(capitulo)


meu_livro = Livro("O Senhor dos Anéis", "Tolkien")

meu_livro.add_capitulo(1, "Uma Festa Inesperada")

meu_livro.getSumario()
