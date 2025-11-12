class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - R${self.salario:.2f}"


class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.membros = []

    def adicionar_membro(self, funcionario):
        self.membros.append(funcionario)

    def remover_membro(self, funcionario):
        if funcionario in self.membros:
            self.membros.remove(funcionario)

    def listar_membros(self):
        if not self.membros:
            print("Nenhum membro no projeto.")
        for membro in self.membros:
            print(membro)

    def custo_total(self):
        return sum([membro.salario for membro in self.membros])


func1 = Funcionario("João", "Desenvolvedor", 5000)
func2 = Funcionario("Maria", "Gerente", 8000)
func3 = Funcionario("Carlos", "Analista", 4000)

projeto = Projeto("Projeto X", "Desenvolvimento de sistema para cliente")

projeto.adicionar_membro(func1)
projeto.adicionar_membro(func2)
projeto.adicionar_membro(func3)

print("Membros do projeto:")
projeto.listar_membros()

print(f"\nCusto total do projeto: R${projeto.custo_total():.2f}")

projeto.remover_membro(func3)

print("\nMembros do projeto após remoção:")
projeto.listar_membros()

print(f"\nCusto total do projeto após remoção: R${projeto.custo_total():.2f}")
