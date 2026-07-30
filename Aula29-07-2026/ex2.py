class Livro:
    def __init__(self):
        self.nome = None
        self.autor = None
        self.editora = None
        self.paginas = 0

    def inserirDados(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, editora):
        self.editora = editora
        print("O novo nome será:", editora)

    def lista_qtd_paginas(self):
        print(self.paginas)


livro = Livro()


nome = input("Insira o nome do livro: ")
autor = (input("Insira o nome do autor: "))
editora = input("Insira o nome da editora: ")
alterar = input("Deseja alterar nome da editora (S/N)?: ")
paginas = int(input("Insira a quantidade de páginas do livro: "))

livro.inserirDados(nome, autor, editora, paginas)

if alterar.lower() == "s":
    editora = input("Insira o nome da editora, corretamente: ")
    livro.alterar_editora(editora)

livro.lista_qtd_paginas()