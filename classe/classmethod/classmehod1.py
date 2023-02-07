# O uso do @classmethod em Python é importante porque permite que você acesse informações da classe sem precisar criar uma instância da classe. Isso significa que você pode acessar atributos estáticos e chamar outros métodos da classe diretamente, sem precisar criar uma instância. Isso é útil quando você quer fazer algo que não depende de informações específicas de uma instância da classe, como configurar a classe ou modificar informações compartilhadas por todas as instâncias da classe. A diferença entre o @classmethod e o método convencional é que o @classmethod aceita a classe como primeiro argumento, em vez da instância da classe


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @classmethod
    def quadrado(cls,lado):
        return cls(lado,lado)


q1=Retangulo.quadrado(20)
print(q1.largura)
print(q1.altura)


