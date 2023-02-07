# Exercício 1: Crie uma classe "Cozinheiro" e uma classe "FerramentaDeCozinha". A classe "Cozinheiro" deve ter um atributo "nome" e uma propriedade "ferramenta", e a classe "FerramentaDeCozinha" deve ter um atributo "nome" e um método "cozinhar". Instancie um objeto "cozinheiro" da classe "Cozinheiro" e um objeto "fogão" da classe "FerramentaDeCozinha". Atribua a propriedade "ferramenta" do cozinheiro com o fogão e chame o método "cozinhar" da ferramenta.


class Cozinheiro:
    def __init__(self,nome):
        self.nome=nome
        self._ferramenta=None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta=ferramenta

class FerramentaDeCozinha:
    def __init__(self,nome):
        self.nome=nome

    def cozinhar(self):
        return f'{self.nome} esta cozinhando'

cozinheiro=Cozinheiro('luiz')
fogao=FerramentaDeCozinha('fogao')
cozinheiro.ferramenta=fogao
print(cozinheiro.ferramenta.cozinhar())



