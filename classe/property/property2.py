# Crie uma classe Celsius com o atributo temperatura. Adicione um método de propriedade chamado fahrenheit que retorne a temperatura em Fahrenheit

class Celsius:
    def __init__(self,temperatura) :
        self.temperatura=temperatura

    @property
    def fahrenheit(self):
        self.temperatura=self.temperatura*1.8+32
        return self.temperatura

t1=Celsius(10)
print(t1.fahrenheit)