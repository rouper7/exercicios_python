# Exercício 2: Escreva uma função que receba um dicionário com informações 
# de pessoa(nome, idade, endereço) e retorne uma string formatada com as 
# informações da pessoa. Utilize ** kwargs para passar as informações do dicionário

dicionario={'nome':'fenix','idade':20,'endereço':'rua diamente'}

def desempacotamento(**kwargs):
    for key,value in kwargs.items():
        print(key,':',value)
        


desempacotamento(**dicionario)
