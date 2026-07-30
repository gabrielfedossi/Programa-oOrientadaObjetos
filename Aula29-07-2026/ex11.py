class NotaFiscal:
    def __init__(self):
        self.numero = None
        self.tipo = None
        self.serie = None
        self.cnpj = None
        self.razao_social = None
        self.data = None
        self.valor_produtos = 0
        self.icms = 0
        self.frete = 0
        self.ipi = 0
        self.valor_total = 0
 
    def inserirDados(self, numero, tipo, serie, cnpj, razao_social, data,
                      valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
 
    def obter_numero(self):
        print("Número da nota:", self.numero)
 
    def obter_data_emissao(self):
        print("Data de emissão:", self.data)
 
    def alterar_razao_social(self, nova_razao_social):
        self.razao_social = nova_razao_social
        print("Nova razão social:", self.razao_social)
 
    def calcular_valor_total(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        print("Valor total da nota:", self.valor_total)
 
 
nf = NotaFiscal()
numero = input("Insira o número da nota: ")
tipo = input("Insira o tipo (Entrada/Saída): ")
serie = input("Insira a série (1, 2 ou 3): ")
cnpj = input("Insira o CNPJ: ")
razao_social = input("Insira a razão social: ")
data = input("Insira a data de emissão: ")
valor_produtos = float(input("Insira o valor dos produtos: "))
icms = float(input("Insira o valor do ICMS: "))
frete = float(input("Insira o valor do frete: "))
ipi = float(input("Insira o valor do IPI: "))
nf.inserirDados(numero, tipo, serie, cnpj, razao_social, data,
                valor_produtos, icms, frete, ipi)
 
nf.obter_numero()
nf.obter_data_emissao()
 
alterar = input("Deseja alterar a razão social (S/N)?: ")
if alterar.lower() == "s":
    nova_razao = input("Insira a nova razão social: ")
    nf.alterar_razao_social(nova_razao)
 
nf.calcular_valor_total()