#fazer uma calculadora com o sys
import sys
def eh_numero(valor) :
    if valor.isdigit():
        return True
    else:
       return False
    



if len(sys.argv)!=4 :
    print(f'apenas utilize dois argumentos: operador numero1 numero2')
    sys.exit()
if  not eh_numero(sys.argv[2]) or not eh_numero(sys.argv[3]) :
    print("digite um numero")
    sys.exit()


numero1=float(sys.argv[2])
numero2=float(sys.argv[3])



if sys.argv[1]=='-':
    calculo=numero1-numero2
    print(f"o resultado da subtração é {calculo}")
if sys.argv[1]=='+':
    calculo=numero1+numero2
    print(f"o resultado da adição é {calculo}")
if sys.argv[1]=='/':
    if numero2==0:
         print("Erro: Divisão por zero não é permitida.")
    else:
        calculo=numero1/numero2
        print(f"o resultado da divisão é {calculo}")
if sys.argv[1]=='*':
    calculo=numero1*numero2
    print(f"o resultado da multiplicação é {calculo}")






