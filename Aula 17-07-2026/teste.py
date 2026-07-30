class Cachorro:

    def __init__(self, nome, raca, cor, idade):
    
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade

    def descricao(self):
        print("Nome: ", self.nome, "Raça: ", self.raca, "Cor: ", self.cor, "Idade: ", self.idade)



# bidu = Cachorro("Bidu", "Dobberman", "Preto", 2) # bilu e bidu sao objts da classe cachorro
# bilu = Cachorro("Bilu", "Pastor", "branco", 3)

cachorro = Cachorro("Bidu", "Dobberman", "Preto", 2) # bilu e bidu sao objts da classe cachorro



cachorro.descricao()
print(cachorro.raca)