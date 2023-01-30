# Exercício: Escreva uma função que receba uma lista de números
# e um dicionário com informações de operação (operação, valor)
# e retorne uma nova lista com a operação realizada apenas nos 
# números pares da lista original. Utilize *args e **kwargs para
# passar a lista de números e as informações da operação, 
# respectivamente.

lista=[18, 5, 12, 15]
dicionario={'operacao':'adicao','valor':3}

def operacao(*args,**kwargs):
    operacao=kwargs.get('operacao')
    valor=kwargs.get('valor')
    nova_lista=[]
    for arg in args:
        if arg%2!=0:
            continue
        else:
            if operacao=='adicao':
                nova_lista.append(arg+valor)
            if operacao=='multicao':
                nova_lista.append(arg*valor)
            if operacao=='subtracao':
                nova_lista.append(arg-valor)
            if operacao=='divicao':
                nova_lista.append(arg/valor)
    return nova_lista

soma_3=operacao(*lista,**dicionario)
print(soma_3)



        
        

