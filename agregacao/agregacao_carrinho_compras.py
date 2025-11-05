class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def add_produto(self, produto):
        self.itens.append(produto)

    def listar_produtos(self):
        for produto in self.itens:
            print(produto)

    def valor_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco
        return total


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f'Produto: {self.nome} | Preço :R$ {self.preco}'


p2 = Produto('Arroz', 30)
p1 = Produto('Chocolate', 7)
p3 = Produto('Batata Frita', 26)

carrinho1 = CarrinhoCompras()

carrinho1.add_produto(p1)
carrinho1.add_produto(p2)
carrinho1.add_produto(p3)

print(carrinho1.valor_total())

