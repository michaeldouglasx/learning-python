class Pedido:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.itens = []

    def add_item(self, nome_produto, qtd, valor_unitario):
        self.itens.append(Item(nome_produto, qtd, valor_unitario))

    def calcula_total(self):
        total = 0
        for item in self.itens:
            total += item.get_subtotal()
        return total

    def recibo(self):
        print(f'--------{self.nome_cliente}---------')
        for item in self.itens:
            print(item)
        total_do_pedido = self.calcula_total()
        print(f'------Valor Total------\n R$ {total_do_pedido}')

class Item():
    def __init__(self, nome_produto, qtd, valor_unitario):
        self.nome_produto = nome_produto
        self.qtd = qtd
        self.valor_unitario = valor_unitario
    def __str__(self):
        return f'-Produto: {self.nome_produto}\n-Quantidade: {self.qtd}\n-Valor unitário: R$ {self.valor_unitario}'

    def get_subtotal(self):
        return self.valor_unitario * self.qtd


pedido1 = Pedido('Michael')
pedido1.add_item('Hamburguer', 3, 30)
pedido1.recibo()


