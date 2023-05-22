class Carrinho:

    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:

    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

sacola = Carrinho()
p1, p2 = Produto('Pão', 5.60), Produto('Cartela de Ovos', 15)
sacola.inserir_produtos(p1, p2)
sacola.listar_produtos()
print(sacola.total())