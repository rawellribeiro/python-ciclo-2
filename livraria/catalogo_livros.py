def exibir_catalogo(lista_livros):
    print("=== CATÁLOGO DE LIVROS ===")

    for livro in lista_livros:
        print("----------------------------")
        print("ID:", livro["id"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Descrição:", livro["descricao"])
        print("Preço: R$", livro["preco"])
    print("----------------------------")


catalogo_padrao = [
    {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "descricao": "Uma aventura na Terra média.", "preco": 49.90},
    {"id": 2, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "descricao": "Um clássico da literatura brasileira.", "preco": 39.90},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "descricao": "Uma história sobre um governo totalitário.", "preco": 59.90},
    {"id": 4, "titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "descricao": "A história de uma menina na guerra.", "preco": 44.90},
    {"id": 5, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "descricao": "Um conto filosófico.", "preco": 29.90}
]
