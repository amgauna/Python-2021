import sys
sys.version_info
sys.__stdin__

import numpy as np

# criando os arrays
titulo = np.array(['CÓDIGO', 'INADIMPLÊNCIA', 'REGIÃO', 'LITROS/MÊS'])
codigo = np.array([47798, 88333, 71928, 74830, 42536])
inadimplencia = np.array([0, 0, 0, 0, 0])
regiao = np.array([1, 2, 3, 4, 5])
lista_regiao = np.array.['regiao-centro', 'regiao_grande_ibis', 'regiao_grande_aribiri', 'regiao_grande_cobilandia', 'regiao_grande_jucu']
litros_mes = np.array[85, 106, 69, 88, 65]

# exiba as mensagens bem formatadas na tela
print({titulo}, {codigo}, {inadimplencia}, {regiao}, {lista_regiao}, {litros_mes}, "\n" )

