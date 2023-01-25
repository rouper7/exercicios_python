#converta esse codigo para lambda

# def multiply_by_two(x):
#     return x*2

# numbers = [1,2,3,4,5]
# result = map(multiply_by_two, numbers)
resultado=[]
numbers=[1,2,3,4,5]

multiplica_por_dois=map(lambda x:x*2,numbers)
for numero in multiplica_por_dois:
    print(numero)
# ou
# print(list(multiplica_por_dois))

#made by rouper7