class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
    def __str__(self):
        return f'Nome do artista: {self.artista} - Titulo da Música: {self.titulo}'

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def add_musica(self, musica):
        self.musicas.append(musica)

    def mostrar_playlist(self):
        print(f'----{self.nome}---')
        for musica in self.musicas:
            print(musica)

m1 = Musica('Toma conta de mim',  ' Limão com mel')
m2 = Musica('Inventor dos Amores', 'Gustavo Lima')
m3 = Musica('Não era pra ser', 'Luan Santana')

sofrencia = Playlist('Sofrencia')

sofrencia.add_musica(m1)
sofrencia.add_musica(m2)
sofrencia.add_musica(m3)

sofrencia. mostrar_playlist()

print(m1.__str__())


