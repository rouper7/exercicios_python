# Crie uma classe Círculo com o atributo raio. Crie um método de classe chamado from_diameter que crie um círculo a partir do diâmetro de um círculo.

class Circulo:
    
    def __init__(self,raio):
        self.raio=raio


    @classmethod
    def from_diameter(cls,raio):
        d=raio*2 
        return 3.14*(d/2)**2


c1=Circulo(2)
print(c1.from_diameter(c1.raio))

