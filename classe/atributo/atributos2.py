# Crie uma classe "Veiculo" que possua atributos "marca" e "ano_fabricacao", e um método "verificar_garantia" que retorne se o veículo ainda está na garantia baseado no ano atual (atributo estático) e no ano de fabricação (atributo de instância).

class Veiculo:
    ano_atual=2023
    garantia=5

    def __init__(self,marca,ano_fabricacao):
        self.marca=marca
        self.ano_fabricacao=ano_fabricacao

    def verificar_garantia(self):
        if self.ano_fabricacao<(Veiculo.ano_atual -Veiculo.garantia):
            print('nao tem garantia pois ja passou do limite')
        else:
            print(f'seu veiculo {self.marca} esta na garantia ')



c1=Veiculo('ford',2020)
print(c1.verificar_garantia())