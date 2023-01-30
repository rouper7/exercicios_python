# Crie uma função chamada "imprime_valores" que recebe uma lista,
# um dicionário, e valores adicionais. A função deve imprimir todos
# os valores passados para ela, independentemente da forma como foram
# passados(seja como argumentos posicionais, como argumentos nomeados
# ou ambos). Use * args para desempacotar a lista e ** kwargs para 
# desempacotar o dicionário.

lista=[1,2,3,4]
dicionario={'nome':'joao','idade':20}
def imprime_valores(*args,**kwargs):
    for i in args:
        print(i)
    
    for key,value in kwargs.items():
        print(key,value)


imprime_valores(*lista,**dicionario)
