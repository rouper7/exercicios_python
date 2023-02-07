# Crie uma classe "Pessoa" que possui os atributos "nome" e "idade". Adicione um método "cumprimentar" que imprime "Olá, meu nome é [nome] e tenho [idade] anos". Depois, crie uma instância da classe e chame o método "cumprimentar" para exibir o cumprimento da pessoa.

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def comprimentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')

maria=Pessoa('maria',15)
print(maria.nome)
print(maria.idade)