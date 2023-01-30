# Escreva uma função que receba uma lista de números e retorne a soma de todos os números. Utilize *args para passar a lista de números.

lista=[7, 3, 10]
def soma(*args):
    count=0
    for arg in args: 
        count+=arg
    return count

print(soma(*lista))