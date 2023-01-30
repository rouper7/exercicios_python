# Neste exemplo, a lista "lista_exemplo" é desempacotada
# usando o operador * e passada como argumentos posicionais
# para a função "minha_funcao". O dicionário "dicionario_exemplo"
# é desempacotado usando o operador ** e passado como argumentos 
# nomeados para a função "minha_funcao". A função imprime cada elemento 
# da lista e cada chave e valor do dicionário.
# def minha_funcao(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key, value)

# lista_exemplo = [1, 2, 3]
# dicionario_exemplo = {"nome": "Lucas", "idade": 25}

# minha_funcao( **dicionario_exemplo)

# Desempacotando dicionário em chamada de função
def funcao_exemplo(nome, idade):
    print(nome, idade)

dicionario = {"nome": "Lucas", "idade": 25}
funcao_exemplo(**dicionario) # imprime "Lucas 25