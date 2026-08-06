from ex1 import * # "*" --> importa TUDO

produtos = []
clientes = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar produto")
    print("2 - Cadastrar cliente")
    print("3 - Adicionar produto ao carrinho")
    print("4 - Remover produto do carrinho")
    print("5 - Finalizar compra")
    print("6 - Listar produtos")
    print("0 - Sair")

    op = int(input("Escolha uma opção: "))

    if op == 1:
        nome = input("Nome do produto: ")

        while True:
            try:
                preco = float(input("Preço: R$ "))
                produto = Produto(nome, preco)
                produtos.append(produto)
                print("Produto cadastrado com sucesso!")
                break
            except ValueError:
                print("Preço inválido!")

    elif op == 2:
            nome = input("Nome do cliente: ")
            email = input("E-mail: ")

            cliente = Cliente(nome, email)
            clientes.append(cliente)

            print("Cliente cadastrado com sucesso!")

    elif op == 3:
        if not clientes:
            print("Nenhum cliente cadastrado.")
            continue

        if not produtos:
            print("Nenhum produto cadastrado.")
            continue

        print("\nClientes:")
        for i, c in enumerate(clientes):
            print(f"{i} - {c.nome}")
        while True:    
            try:
                cliente = clientes[int(input("Escolha o cliente: "))]
                break
            except ValueError:
                print("\nDigite um valor correto!")

        print("\nProdutos:")
        for i, p in enumerate(produtos):
            print(f"{i} - {p.nome} - R$ {p.preco}")
        while True:
            try:
                produto = produtos[int(input("Escolha o produto: "))]
                break
            except ValueError:
                print("\nDigite um valor correto!")

        cliente.carrinho.adicionar_produto(produto)

    elif op == 4:
        if not clientes:
            print("Nenhum cliente cadastrado.")
            continue

        print("\nClientes:")
        for i, c in enumerate(clientes):
            print(f"{i} - {c.nome}")

        while True:    
            try:
                cliente = clientes[int(input("Escolha o cliente: "))]
                break
            except ValueError:
                print("\nDigite um valor correto!")

        if not cliente.carrinho.produtos:
            print("Carrinho vazio.")
            continue

        print("\nProdutos no carrinho:")
        for i, p in enumerate(cliente.carrinho.produtos):
            print(f"{i} - {p.nome} - R$ {p.preco}")
        while True:
            try:
                indice = int(input("Escolha o produto para remover: "))
                break
            except ValueError:
                print("\nDigite um valor correto!")
        cliente.carrinho.remover_produto(indice)

    elif op == 5:
        if not clientes:
            print("Nenhum cliente cadastrado.")
            continue

        print("\nClientes:")
        for i, c in enumerate(clientes):
            print(f"{i} - {c.nome}")

        while True:    
            try:
                cliente = clientes[int(input("Escolha o cliente: "))]
                break
            except ValueError:
                print("\nDigite um valor correto!")
        cliente.finalizar_pedido()

    elif op == 6:
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(f"{p.nome} - R$ {p.preco}")

    elif op == 0:
        print("FIm do programa")
        break


    else:
        print("Opcao invalida")
