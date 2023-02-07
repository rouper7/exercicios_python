# O exercício pede para que você crie uma classe chamada "Retangulo", com atributos comprimento e largura. Depois, é pedido para que você crie um método de classe chamado "from_square", que será responsável por criar um retângulo a partir do comprimento de um quadrado.

class Retangulo:
    def __init__(self,comprimento,largura):
        self.comprimento=comprimento
        self.largura=largura

    @classmethod
    def from_square(cls,lado):
        return cls(lado,lado)


c1=Retangulo(50,80)
c1=c1.from_square(30)
print(c1.comprimento)
print(c1.largura)
