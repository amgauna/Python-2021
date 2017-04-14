>>> # Utilizando Python Como Uma Calculadora
>>> # Vamos tentar alguns comandos simples em Python. 
>>> # Inicie o interpretador e aguarde o prompt primário, ">>> ". (Não deve demorar muito.)

>>> # 3.1.1 Números
>>> # O interpretador atua como uma calculadora bem simples: você pode digitar uma expressão e o valor resultando será
>>> # apresentado após a avaliação da expressão. A sintaxe da expressão é a usual: operadores +, -, * e / funcionam da
>>> # mesma forma que em outras linguagens tradicionais (por exemplo, Pascal ou C); parênteses podem ser usados para 
>>> # definir agrupamentos. 

>>> # Por exemplo:

>>> 2+2
4
>>> # Isso é um comentário
... 2+2
4
>>> 2+2  # e um comentário na mesma linha de um comando
4
>>> (50-5*6)/4
5
>>> # Divisão inteira retorna com aredondamento para base
... 7/3
2
>>> 7/-3
-3

>>> # O sinal de igual ("=") é utilizado para atribuição de um valor a uma variável. 
>>> # Nenhum resultado é exibido até o próximo prompt interativo:

>>> width = 20
>>> height = 5*9
>>> width * height
900

>>> # Um valor pode ser atribuído a diversas variáveis simultaneamente:

>>> x = y = z = 0  # Zero x, y e z
>>> x
0
>>> y
0
>>> z
0

>>> # Há total suporte para ponto-flutuante; operadores com operandos de diferentes tipos convertem o inteiro para ponto-flutuante:

>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5

>>> # Números complexos também são suportados; números imaginários são escritos com o sufixo "j" ou "J". 
>>> # Números complexos com parte real não nula são escritos como "(real+imagj)", ou podem ser criados 
>>> # pela chamada de função "complex(real, imag)".

>>> 1j * 1J
(-1+0j)
>>> 1j * complex(0,1)
(-1+0j)
>>> 3+1j*3
(3+3j)
>>> (3+1j)*3
(9+3j)
>>> (1+2j)/(1+1j)
(1.5+0.5j)

>>> # Números complexos são sempre representados por dois números ponto-flutuante, a parte real e a parte imaginária. 
>>> # Para extrair as partes de um número z, utilize z.real e z.imag.

>>> a=1.5+0.5j
>>> a.real
1.5
>>> a.imag
0.5

>>> # As funções de conversão para ponto-flutuante e inteiro (float(), int() e long()) não funcionam para números complexos 
>>> # -- não existe maneira correta de converter um número complexo para um número real. 
>>> # Utilize abs(z) para obter sua magnitude (como ponto-flutuante) ou z.real para obter sua parte real.

>>> a=3.0+4.0j
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: can't convert complex to float; use abs(z)
>>> a.real
3.0
>>> a.imag
4.0
>>> abs(a)
5.0

>>> # No modo interativo, a última expressão a ser impressa é atribuída a variável _.  Isso significa que ao utilizar
>>> # Python como uma calculadora, é muitas vezes mais fácil prosseguir com os cálculos da seguinte forma:

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> # Essa variável especial deve ser tratada somente para leitura pelo usuário. Nunca lhe atribua explicitamente um valor 
>>> # - do contrário, estaria se criando uma outra variável (homônima) independente, que mascararia o comportamento mágico 
>>> # da variável especial.
