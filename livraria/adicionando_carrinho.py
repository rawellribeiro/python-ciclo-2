def adicionar_livro(carrinho):
    print("=== ADICIONAR LIVROS AO CARRINHO ===")
    print("Digite o nome do livro ou 'sair' para parar.")

    while True:
        nome = input("Livro: ")

        if nome.lower() == "sair":
            break

        carrinho.append(nome)
        print(f'Livro "{nome}" adicionado ao carrinho!\n')

    print("\n=== LIVROS NO CARRINHO ===")
    for item in carrinho:
        print("-", item)
