class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def verificar_estoque(self):
        return self.estoque > 0


class Carrinho:
    def __init__(self):
        self.produtos = []
        self.total = 0

    def adicionar(self, produto, quantidade):
        if produto.verificar_estoque() and produto.estoque >= quantidade:
            produto.estoque -= quantidade
            self.produtos.append({"produto": produto, "quantidade": quantidade})
            self.total += produto.preco * quantidade
            print(f"O produto '{produto.nome}' foi adicionado ao carrinho. Quantidade: {quantidade}\n")
        else:
            print(f"O produto '{produto.nome}' não está disponível em quantidade suficiente!\n")

    def remover(self, produto):
        for item in self.produtos:
            if item["produto"] == produto:
                self.produtos.remove(item)
                produto.estoque += item["quantidade"]
                self.total -= produto.preco * item["quantidade"]
                print(f"O produto '{produto.nome}' foi removido do carrinho!\n")
                return
        print(f"O produto '{produto.nome}' não está no carrinho!\n")

    def finalizar_compra(self):
        if not self.produtos:
            print("O carrinho está vazio! Não é possível finalizar a compra.\n")
            return

        print("Resumo da compra:")
        for item in self.produtos:
            produto = item["produto"]
            quantidade = item["quantidade"]
            print(
                f"Produto: {produto.nome}, Quantidade: {quantidade}, Preço unitário: {produto.preco}, Subtotal: {produto.preco * quantidade}")

        print(f"Total da compra: R${self.total:.2f}\n")
        self.produtos.clear()
        self.total = 0


produto1 = Produto("Camiseta", 50.00, 10)
produto2 = Produto("Calça Jeans", 120.00, 5)

carrinho = Carrinho()
carrinho.adicionar(produto1, 2)
carrinho.adicionar(produto2, 1)
carrinho.remover(produto1)
carrinho.finalizar_compra()
