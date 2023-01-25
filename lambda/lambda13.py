# Crie uma lista chamada "numbers" com números inteiros qualquer.
# Crie uma nova lista com o resultado da aplicação de uma função lambda em cada elemento da lista "numbers", elevando cada número ao quadrado.
# Use a função sum() para somar os valores da nova lista.
# Armazene o resultado em uma variável chamada "result" e imprima o resultado.


numbers=[3, 17, 11, 20, 6]

new_numbers=map(lambda x:x**2,numbers)
soma=sum(new_numbers)
print(soma)