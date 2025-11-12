class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado!\n")
        else:
            print(f"O livro '{self.titulo}' já está emprestado!\n")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido!\n")
        else:
            print(f"O livro '{self.titulo}' já está disponível!\n")

    def exibir_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Disponível: {self.disponivel}")


livros = [
    Livro("A invenção de Hugo Cabret", "Brian Selznick", 2012),
    Livro("Senhora", "José de Alencar", 1875),
    Livro("Capitães da Areia", "Jorge Amado", 1937)
]

while True:
    print("\nBiblioteca")
    print("1 - Verificar livros disponíveis")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nLivros disponíveis:")
        tem_disponivel = False
        for i, livro in enumerate(livros):
            if livro.disponivel:
                print(f"{i + 1}. {livro.titulo}")
                tem_disponivel = True
        if not tem_disponivel:
            print("Nenhum livro disponível no momento.")

    elif opcao == "2":
        print("\nEscolha um livro para emprestar:")
        for i, livro in enumerate(livros):
            if livro.disponivel:
                print(f"{i + 1}. {livro.titulo}")
        escolha = int(input("Número do livro: ")) - 1
        if 0 <= escolha < len(livros):
            livros[escolha].emprestar()
        else:
            print("Opção inválida.")

    elif opcao == "3":
        print("\nEscolha um livro para devolver:")
        for i, livro in enumerate(livros):
            if not livro.disponivel:
                print(f"{i + 1}. {livro.titulo}")
        escolha = int(input("Número do livro: ")) - 1
        if 0 <= escolha < len(livros):
            livros[escolha].devolver()
        else:
            print("Opção inválida.")

    elif opcao == "4":
        print("Saindo da biblioteca.")
        break

    else:
        print("Opção inválida. Tente novamente.")
