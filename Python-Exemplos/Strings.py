# Strings
# Além de números, Python também pode manipular strings, que podem ser expressas de diversas formas. 
# Elas podem ser delimitadas pos aspas simples ou duplas:

'spam eggs'

"doesn't"

'"Yes," he said.'

'"Isn\'t," she said.'

# Strings que contém mais de uma linha podem ser construídas de diversas maneiras. 
# Terminadores de linha podem ser embutidos na string com barras invertidas, 
# Exemplo.:

oi = "Esta eh uma string longa contendo\n\
diversas linhas de texto assim como voce faria em C.\n\
    Observe que os espaços em branco no inicio da linha são \
 significativos."
print oi

# Observe que terminadores de linha ainda precisam ser embutidos na string usando \n; a quebra de linha
# após a última barra de escape seria ignorada. Este exemplo produziria o seguinte resultado:

Esta eh uma string longa contendo
diversas linhas de texto assim como voce faria em C.
    Observe que os espaços em branco no inicio da linha são significativos.

# No entanto, se a tornarmos uma string ``crua'' (raw), as sequências de \n não são convertidas para quebras de linha. 
# Tanto a barra invertida quanto a quebra de linha no código-fonte são incluídos na string como dados. Portanto, o exemplo:

oi = r"Esta eh uma string longa contendo\n\
diversas linhas de texto assim como voce faria em C.\n\
    Observe que os espaços em branco no inicio da linha são \
 significativos."
print oi

# teria como resultado:

Esta eh uma string longa contendo\n\
diversas linhas de texto assim como voce faria em C.\n\
    Observe que os espaços em branco no inicio da linha são \
 significativos

# Ou, strings podem ser delimitadas por pares de aspas tríplices: " ou '''. Neste caso não é necessário embutir
# terminadores de linha, pois o texto da string será tratado verbatim.

print """
Usage: thingy [OPTIONS] 
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
# produz a seguinte saída:

Usage: thingy [OPTIONS] 
     -h                        Display this usage message
     -H hostname               Hostname to connect to

# O interpretador imprime o resultado de operações sobre strings da mesma forma que as strings são formatadas
# na digitação: dentro de aspas, e com caracteres especiais embutidos em escape sequences, para mostar seu valor
# com precisão. A string será delimitada por aspas duplas se ela contém um único caracter de aspas simples e nenhum
# de aspas duplas, caso contrário a string será delimitada por aspas simples. ( O comando print, descrito posteriormente,
# pode ser utilizado para escrever strings sem aspas ou escape sequences.)

# Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *:

word = 'Help' + 'A'
word 'HelpA'
'<' + word*5 + '>'
'<HelpAHelpAHelpAHelpAHelpA>'

# Duas strings literais justapostas são automaticamente concatenadas; a primeira linha do exemplo anterior poderia
# ter sido escrita como "word = 'Help''A'"; isso funciona somente com strings literais, não com expressões arbitrárias:

'str' 'ing'                #  <-  This is ok
'string'

str.strip('str') + 'ing'   #  <-  This is ok
'string'

str.strip('str') 'ing'     #  <-  This is invalid
  File "<stdin>", line 1
    str.strip('str') 'ing'
                            ^
SyntaxError: invalid syntax

# Strings podem ser indexadas; como em C, o primeiro índice da string é o 0. Não existe um tipo separado para caracteres; 
# um caracter é simplesmente uma string unitária. Assim como na linguagem Icon, substrings podem ser especificadas através
# da notação slice (N.d.T: fatiar): dois índices separados por dois pontos.

word[4]
'A'

word[0:2]
'He'

word[2:4]
'lp'

# Índices de fatias slice seguem uma padronização útil; a omissão do primeiro índice equivale a zero, a omissão do segundo
# índice equivale ao tamanho da string sendo fatiada.

word[:2]    # Os dois primeiros caracteres
'He'

word[2:]    # Tudo exceto os dois primeiros caracteres
'lpA'

# Diferentemente de C, strings não podem ser alteradas em Python. Atribuir para uma posição (índice) dentro de uma string
# resultará em erro:

word[0] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object doesn't support item assignment
    
word[:1] = 'Splat'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object doesn't support slice assignment

# Entretanto, criar uma nova string com o conteúdo combinado é fácil e eficiente:

'x' + word[1:]
'xelpA'

'Splat' + word[4]
'SplatA'

# Aqui está um invariante interessante relacionado a operações de slice: s[:i] + s[i:] equals s.

word[:2] + word[2:]
'HelpA'

word[:3] + word[3:]
'HelpA'

# Índices de slice degenerados são tratados ``graciosamente'' (N.d.T: este termo indica robustez no tratamento de erros): 
# um índice muito maior que o comprimento é trocado pelo comprimento, um limitante superior que seja menor que o limitante 
# inferior produz uma string vazia como resultado.

word[1:100]
'elpA'

word[10:]
''

word[2:1]
''
# Índices podem ser números negativos, para iniciar a contagem a partir da direita ao invés da esquerda. 
# Por exemplo:

word[-1]     # O útlimo caracter
'A'
word[-2]     # O penúltimo caracter
'p'
word[-2:]    # Os dois últimos caracteres 
'pA'
word[:-2]    # Tudo exceto os dois últimos caracteres
'Hel'

# Observe que -0 é o mesmo que 0, logo neste caso não se conta a partir da direita!

word[-0]     # ( -0 ==  0)
'H'

# Intervalos fora dos limites da string são truncados, mas não tente isso em indexações com um único índice 
# (que não seja um slice):

word[-100:]
'HelpA'
word[-10]    # error
Traceback (most recent call last):
  File "<stdin>", line 1
IndexError: string index out of range

# A melhor maneira de lembrar como slices funcionam é pensar nos índices como ponteiros para os espaços
# entre caracteres, onde a beirada esquerda do primeiro caracter é 0. Logo a beirada direita do último 
# caracter de uma string de comprimento n tem índice n, por exemplo:

 +---+---+---+---+---+ 
 | H | e | l | p | A |
 +---+---+---+---+---+ 
 0   1   2   3   4   5 
-5  -4  -3  -2  -1

# A primeira fileira de números indica a posição dos índices 0..5 na string; a segunda fileira indica a posição
# dos respectivos índices negativos. Um slice de i até j consiste em todos os caracteres entre as beiradas i e j,
# respectivamente.

# Para índices positivos, o comprimento do slice é a diferença entre os índices, se ambos estão dentro dos limites
# da string, ex, o comprimento de word[1:3] é 2.

# A função interna (N.d.T: interna == built-in) len() devolve o comprimento de uma string:

s = 'supercalifragilisticexpialidocious'
len(s)
34
