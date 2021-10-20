
# calculo

import math

x = input("Qual a função de x? ")
a = input("Qual o intervalo A da função? ")
b = input("Qual o intervalo B da função? ")
e = input("Qual o valor de E? ")

def f(x):
    return x
	
if f(a)*f(b) < 0:
   while (math.fabs(b-a)>2 > e):
        x1 = (a+b)/2
        if f(x1) == 0:
           print(f" a raiz é {x1}")
           break
         else:
         if f(a)*f(b) <0:
            b = x1
         else:
         a = x1
         print(f" a raiz é {x1}")
		 break
		 return

else:
    print("Não existe raiz no intervalo declarado!")
	
    print("Sua função foi f(x) com intervalo de f(a)")

    print("Intervalo é de (a) e raiz de (x1)")
 	
		 
