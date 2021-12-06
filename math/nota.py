# nota

nota1 = float(input("digite sua primeira nota: "))

nota2 = float(input("digite sua segunda nota: "))

if (nota1 + nota2) / 2 >= 7.0:
   print("Você foi APROVADO!")
   
elif (nota1 + nota2) /2 >= 5 && (nota1 + nota2) / 2 <= 6.9:
    print("Você está de RECUPERAÇÃO!")  

elif (nota1 + nota2) / 2 < 5.0:
    print("Você foi REPROVADO!")

print("Continue estudando!")
