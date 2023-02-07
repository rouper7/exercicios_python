class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

def calcular_valor_total_estoque(lista_produtos):
    valor_total = 0
    for produto in lista_produtos:
        valor_total += produto.preco * produto.quantidade
    return valor_total

produto1 = Produto('Televisão', 2000, 10)
produto2 = Produto('Notebook', 1500, 5)
produto3 = Produto('Smartphone', 800, 20)

lista_produtos = [produto1, produto2, produto3]
valor_total_estoque = calcular_valor_total_estoque(lista_produtos)
print(valor_total_estoque)