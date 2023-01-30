# Exercício 3: Escreva uma função que receba uma lista de números
# e um dicionário com informações de operação(operação, valor) e 
# retorne a lista de números com a operação realizada.
# Utilize * args e ** kwargs para passar a lista de números e as informações da operação, respectivamente.
lista=[2,4,6]
dicionario={'operacao':'multiplicacao','valor':2}

def operacao_na_lista(*args,**kwargs):
    operador=kwargs.get('operacao')
    valor=kwargs.get('valor')
    nova_lista=[]
    for arg in args:
        if operador=='multiplicacao':
            nova_lista.append(valor*arg)
        if operador=='adicao':
            nova_lista.append(valor+arg)
        if operador=='divisao':
            nova_lista.append(valor/arg)
        if operador=='subtraçao':
            nova_lista.append(valor-arg)
        
    return nova_lista

resultado=operacao_na_lista(*lista,**dicionario)
print(resultado)

