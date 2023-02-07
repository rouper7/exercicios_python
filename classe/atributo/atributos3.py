# Crie uma classe "Imovel" que possua atributos "endereco" e "ano_construcao", e um método "verificar_antiguidade" que retorne a antiguidade do imóvel baseado no ano atual (atributo estático) e no ano de construção (atributo de instância).

class Imovel:
    ano_atual=2023

    def __init__(self,endereco,ano_construcao):
        self.endereco=endereco
        self.ano_construcao=ano_construcao

    def verificar_antiguidade(self):
        total=Imovel.ano_atual -self.ano_construcao

        return total

im1=Imovel('rua uruguai',1970)

print(f'o imovel do endereço:{im1.endereco} tem {im1.verificar_antiguidade()} anos de construcao')
