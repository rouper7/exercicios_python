# #def verifica_maior(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(verifica_maior(5, 10)) # imprime 10
# Você deve melhorar esse código utilizando 
# a função lambda e deixa-lo mais conciso e fácil de ler.


verifica_maior=lambda a,b:a if a>b else b

print(verifica_maior(5,9))
#made by rouper7