import sys
import numpy as np

# criando as listas
lista_array = ([ ['CÓDIGO', 'INADIMPLÊNCIA', 'REGIÃO', 'LITROS/MÊS'],
                 [47798, 0, 1:'regiao-centro', 85],
                 [88333, 0, 2:'regiao_grande_ibis', 106],
                 [71928, 0, 3:'regiao_grande_aribiri', 69],
                 [74830, 0, 4:'regiao_grande_cobilandia', 88],
                 [42536, 0, 5:'regiao_grande_jucu', 65] 
               ])
                 
# criando os arrays
cria_array = np.array.format(lista_array)

# exiba as mensagens bem formatadas na tela
for line in sys.stdin:
if 'Exit' == line.rstrip():
break
          
print(line.cria_array)
