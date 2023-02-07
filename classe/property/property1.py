# Crie uma classe Pessoa com os atributos nome e idade_anos. Adicione um método de propriedade chamado idade  que retorne a idade em anos.


class Pessoa:
    def __init__(self,nome,idade_anos):
        self.nome=nome
        self.idade_anos=idade_anos

    @property
    def idade(self):
        return self.idade_anos


p1=Pessoa('guilherme',35)
print(p1.idade)
