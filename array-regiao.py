import sys
sys.version_info
sys.__stdin__

import numpy as np

# criando as listas
titulo = ['CÓDIGO', 'INADIMPLÊNCIA', 'REGIÃO', 'LITROS/MÊS']
codigo = [47798, 88333, 71928, 74830, 42536]
inadimplencia = [0, 0, 0, 0, 0]
regiao = [1, 2, 3, 4, 5]
lista_regiao = ['regiao-centro', 'regiao_grande_ibis', 'regiao_grande_aribiri', 'regiao_grande_cobilandia', 'regiao_grande_jucu']
litros_mes = [85, 106, 69, 88, 65]
          
# criando os arrays
titulo_array = np.array(titulo)
codigo_array = np.array(codigo)
inadimplencia_array = np.array(inadimplencia)
regiao_array = np.array(regiao)
lista_regiao_array = np.array(lista_regiao)
litros_mes_array = np.array(litros_mes)

# exiba as mensagens bem formatadas na tela
print({titulo_array}, {codigo_array}, {inadimplencia_array}, {regiao_array}, {lista_regiao_array}, {litros_mes_array})
