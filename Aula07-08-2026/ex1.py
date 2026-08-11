class Musica:
    def __init__(self, nome, artista, album, duracao : int):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.duracao = duracao

class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica : Musica):
        self.musicas.append(musica)
        print(f"Musica {musica.nome} adicionado!\n")

    


    def remover_musica(self, indice):
        if 0 <= indice < len(self.musicas):
            musica = self.musicas.pop(indice)
            print(f"Musica {musica.nome} removido!")
        else:
            print("Índice inválido.")


    def listar_musicas(self):
        if not self.musicas:
            print("Está playlist está vazia")
            return


        print("\nMúsicas da playlist")

        for i, m in enumerate(self.musicas):
            print(f"{i} - {m.nome}  | Artista: {m.artista} | Álbum: {m.album} | Duração: {m.duracao} min" )


