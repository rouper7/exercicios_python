# Crie uma classe "Livro" que possui os atributos "título", "autor" e "ano_publicacao". Adicione um método "info" que imprime as informações do livro (título, autor e ano de publicação). Depois, crie uma instância da classe e chame o método "info" para exibir as informações do livro.

class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo 
        self.autor=autor 
        self.ano_publicacao=ano_publicacao 


info=Livro("harry potter",'.K. Rowling.',' 1997')

print(info.titulo)
print(info.autor)
print(info.ano_publicacao)