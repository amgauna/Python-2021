# nota

a = float(input("digite sua primeira nota: "))
nota1 = int(a)
print ("/n")

b = float(input("digite sua segunda nota: "))
nota2 = int(b)
print ("/n")

media = (nota1 + nota2)/2

print("Sua média é ", media, "/n")
      
if (nota1 + nota2) / 2 >= 7.0:
   print("Com essa nota ",media,", você foi APROVADO!")
   print ("/n")
   
elif (nota1 + nota2) /2 >= 5 && (nota1 + nota2) / 2 <= 6.9:
    print("Com essa nota ",media,", você está em RECUPERAÇÃO!") 
    print ("/n")

elif (nota1 + nota2) / 2 < 5.0:
    print("Com essa nota ",media, ", você foi REPROVADO!")
    print ("/n")
   
print("Continue estudando!")
