# Crie uma classe "Empregado" que possua atributos "nome", "salario" e "ano_admissao", e um método "calcular_tempo_servico" que retorne o número de anos de serviço do empregado baseado no ano atual (atributo estático) e no ano de admissão (atributo de instância).

class Empregado:
    ano_atual=2023
    
    def __init__(self,nome,salario,ano_admissao):
        self.nome=nome
        self.salario=salario
        self.ano_admissao=ano_admissao

    def ano_servico(self):
        total= Empregado.ano_atual-self.ano_admissao
        return print(f' o número de anos de serviço do empregado é {total}')


p1=Empregado('taquinho',3500,1970)
print(p1.nome)
print(p1.salario)
print(p1.ano_servico())

