#  o operador * desempacota os elementos da estrutura iterável e os passa como argumentos posicionais. Por exemplo:
def funcao_desempacotar(*args):
    print(args)


lista=[1,2,3,4,5]
print(*lista)

# Já o operador ** desempacota os elementos de um dicionário
# e os passa como argumentos nomeados, ou seja, cada chave e
# valor do dicionário vira um argumento da função. Por exemplo:

def funcao_exemplo(nome, idade):
    print(nome, idade)

dicionario_exemplo = {"nome": "Lucas", "idade": 25}
funcao_exemplo(**dicionario_exemplo)