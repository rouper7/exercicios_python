# : Crie uma classe "Artista" e uma classe "FerramentaDeArte". A classe "Artista" deve ter um atributo "nome" e uma propriedade "ferramenta", e a classe "FerramentaDeArte" deve ter um atributo "nome" e um método "criar". Instancie um objeto "artista" da classe "Artista" e um objeto "pincel" da classe "FerramentaDeArte". Atribua a propriedade "ferramenta" do artista com o pincel e chame o método "criar" da ferramenta.


class Artista:
    def __init__(self,nome):
        self.nome=nome
        self._ferramenta=None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeArte:
    def __init__(self,nome):
        self.nome=nome

    def criar(self):
        return f'o artista esta pintando com {self.nome} ' 

artista=Artista('marcos')
pincel=FerramentaDeArte('pincel')
artista.ferramenta=pincel

print(artista.ferramenta.criar())


        