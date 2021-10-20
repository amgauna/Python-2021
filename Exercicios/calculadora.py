# calculadora aritmética

print ("Digite a operação desejada de acordo com a explicação abaixo:")
print ("Digite + para adição")
print ("Digite - para subtração")
print ("Digite * para multiplicação")
print ("Digite / para divisão")

operacao = (input("Operação desejada: "))

n1 = int(input("Agora digite o primeiro número: "))

n2 = int(input("Agora digite o segundo número: "))

if operacao == "+":
      print(f"operacao: {n1} {operacao} {n2} = {n1 + n2}")
   
   elif operacao == "-":
      print(f"operacao: {n1} {operacao} {n2} = {n1 - n2}")
   
   elif operacao == "*":
   print(f"operacao: {n1} {operacao} {n2} = {n1 * n2}")
   
   elif operacao == "/":
      print(f"operacao: {n1} {operacao} {n2} = {n1 / n2}")
   
   else:
      print("Ops! Operação inválida, tente novamente!")
break

s = n1 + n2
print("A soma entre {n1} e {n2} é igual a {s}.".format(n1,n2,s))
