# Crie uma classe Produto com os atributos nome e preco. Crie um método de classe chamado desconto que aplique um desconto de 20% ao preço de um produto.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @classmethod
    def desconto(cls, preco):
        return preco * 0.8

produto = Produto("Notebook", 2000)
print(produto.nome) # Notebook
print(produto.desconto(produto.preco))