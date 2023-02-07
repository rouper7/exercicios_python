# Crie uma classe "ContaBancaria" que possui os atributos "nome_titular" e "saldo". Adicione um método "depositar" que permite depositar dinheiro na conta e um método "sacar" que permite sacar dinheiro da conta. Depois, crie uma instância da classe e faça alguns depósitos e saques para testar os métodos.

class ContaBancaria:
    def __init__(self,nome_titular,saldo):
        self.nome=nome_titular
        self.saldo=saldo

    def depositar(self):
        print(f'voce({self.nome}) depositou {self.saldo}')
    
    def sacar(self):
        print(f'voce({self.nome}) sacou {self.saldo}')

pessoa1=ContaBancaria('joao pedro',2500)
pessoa1.sacar()
pessoa1.depositar()