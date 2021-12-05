import sys
sys.version_info
sys.__stdin__

import numpy as np

# criando as listas
lista_array = { ('CÓDIGO', 'INADIMPLÊNCIA', 'REGIÃO', 'LITROS/MÊS'),
                (47798, 0, 1:'regiao-centro', 85),
                (88333, 0, 2:'regiao_grande_ibis', 106),
                (71928, 0, 3:'regiao_grande_aribiri', 69),
                (74830, 0, 4:'regiao_grande_cobilandia', 88),
                (42536, 0, 5:'regiao_grande_jucu', 65) 
              }
                 
# criando os arrays
np.cria_array = format(lista_array)

# exiba as mensagens bem formatadas na tela
for np.cria_array in sys.stdin:
if 'Exit' == np.cria_array.rstrip():
break
          
print(np.cria_array)
