from ex1 import * # "*" --> importa TUDO

playlist = {}
musicas = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar música")
    print("2 - Listar músicas cadastradas")
    print("3 - Criar playlist")
    print("4 - Adicionar música à playlist")
    print("5 - Remover música da playlist")
    print("6 - Exibir playlist")
    print("7 - Buscar por nome")
    print("0 - Sair")

    op = int(input("Escolha uma opção: "))

    if op == 1:
       

        while True:
            try:
                nome = (input("Nome:  "))
                artista = (input("Artista: "))
                album_nome = (input("Nome do álbum: "))
                duracao = int(input("Insira a duração da música em minutos: "))
                musics = Musica(nome, artista, album_nome, duracao)
                musicas.append(musics)
                
                print("Música adicionada com sucesso!")
                break
            except ValueError:
                print("Valor inválido!")
    elif op == 2:

        print("\nMusicas:")
        for i, p in enumerate(musicas):
            print(f"{i} - {p.nome}")


    elif op == 3:
        if playlist:
            for i, c in enumerate(playlist.keys()):
                print(f"{i} - {c}")
        while True:    
            try:
                nome_play = (input("Escolha o nome pra playlist: "))
                break
            except ValueError:
                print("\nDigite um valor correto!")

        playlist[nome_play] = Playlist()
        print(f"Playlist '{nome_play}' criada!")

        

    elif op == 4:
        if not playlist:
            print("Nenhuma playlist cadastrada.")
            continue

        nome_das_play = list(playlist.keys())
        
        print("\nPlaylist:")
        for i, c in enumerate(nome_das_play):
            print(f"{i} - {c}")

        while True:    
            try:
                cliente = int(input("Escolha a playlist: "))
                if 0 <= cliente < len(nome_das_play):
                    break
                print("\nNumero inválido")
            except ValueError:
                print("\nDigite um valor correto!")


        if not musicas:
            print("Nenhuma músicam cadastrada!")
            continue
        
        print("\nMusicas que deseja adicionar:")
        for i, p in enumerate(musicas):
            print(f"{i} - {p.nome}")
        while True:
            try:
                indice = int(input("Escolha a música para adicionar: "))
                if 0 <= indice < len(musicas):
                    break
                print("Número inválido")
            except ValueError:
                print("\nDigite um valor correto!")

        
        nome_escolhido = nome_das_play[cliente]

        playlist_atual : Playlist = playlist[nome_escolhido]

        musica_escolhida = musicas[indice]

        playlist_atual.adicionar_musica(musica_escolhida)

    elif op == 6:

        if not playlist:
            print("\nNenhuma playlist cadastrada")
            continue

        nome_das_play = list(playlist.keys())
        print("\nPlaylist:")
        for i, c in enumerate(nome_das_play):
            print(f"{i} - {c}")

        while True:    
            try:
                escolha_play = int(input("Escolha a playlist: "))
                if 0 <= escolha_play < len(nome_das_play):
                    break
                print("\nNumero inválido")
            except ValueError:
                print("\nDigite um valor correto!")    

        nome_escolhido = nome_das_play[escolha_play]
        playlist_atual : Playlist = playlist[nome_escolhido]

        playlist_atual.listar_musicas()
        
