class Carro:
    def __init__(self, cor, marca, modelo, nivelCombustivel, farol):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.nivelCombustivel = nivelCombustivel
        self.farol = farol

    def andar(self):
        print("O carro está andando!")
        self.nivelCombustivel -= 2
        if self.nivelCombustivel <= 20 and self.nivelCombustivel > 0:
            print("O nível de combustível chegou na reserva!")
        elif self.nivelCombustivel == 0:
            print("O combustível do carro acabou!")

    def buzinar(self):
        print("O carro está buzinando!")

    def ligarFarol(self):
        self.farol = True
        print("O farol está ligado!")

meu_carro = Carro(cor="Branco", marca="Renault", modelo="Kwid", nivelCombustivel=30, farol=False)

while(True):
    print("Menu de opções: \n")
    print("1 - Verificar modelo")
    print("2 - Verificar cor")
    print("3 - Verificar marca")
    print("4 - Ligar o carro")
    print("5 - Buzinar o carro")
    print("6 - Ligar farol")
    print("0 - Exibir carro")
    opcao = int(input())
    if opcao == 1:
        print("\nModelo: ", meu_carro.modelo)
    elif opcao == 2:
        print("Cor: ", meu_carro.cor)
    elif opcao == 3:
        print("Marca: ", meu_carro.marca)
    elif opcao == 4:
        meu_carro.andar()
    elif opcao == 5:
        meu_carro.buzinar()
    elif opcao == 6:
        meu_carro.ligarFarol()
    elif opcao == 0:
        print("Informações:")
        print("Modelo: ", meu_carro.modelo)
        print("Cor: ", meu_carro.cor)
        print("Marca: ", meu_carro.marca)
        print("Nível de combustível: ", meu_carro.nivelCombustivel)
        if meu_carro.farol:
            print("Farol: ligado")
        else:
            print("Farol: desligado")
    else:
        break



