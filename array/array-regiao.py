import sys
sys.version_info
sys.__stdin__

import NumPy

# criando os arrays
titulo = array.typecode(['CÓDIGO', 'INADIMPLÊNCIA', 'REGIÃO', 'LITROS/MÊS'])
codigo = array.typecode([47798, 88333, 71928, 74830, 42536])
inadimplencia = array.typecode([0, 0, 0, 0, 0])
regiao = array.typecode([1, 2, 3, 4, 5])
lista_regiao = array.typecode(['regiao-centro', 'regiao_grande_ibis', 'regiao_grande_aribiri', 'regiao_grande_cobilandia', 'regiao_grande_jucu'])
litros_mes = array.typecode([85, 106, 69, 88, 65])

# exiba as mensagens bem formatadas na tela
print( {titulo}, {codigo}, {inadimplencia}, {regiao}, {lista_regiao}, {litros_mes}, "\n" )

