import numpy as np

# criando as listas
titulo = ['CÓDIGO', "INADIMPLÊNCIA', REGIÃO', 'LITROS/MÊS']
codigo = [47798, 88333, 71928, 74830, 42536]
inadimplencia = [1:'SIM', 0:'NAO'}
regiao = [1:'regiao-centro', 2:'regiao_grande_ibis', 3:'regiao_grande_aribiri', 4:'regiao_grande_cobilandia', 5:'regiao_grande_jucu"]
litros_mes = [85, 106, 69, 88, 65]
          
# criando os arrays
titulo_array = np.array(titulo)
codigo_array = np.array(codigo)
inadimplencia_array = np.array(inadimplencia)
regiao_array = np.array(regiao)
litros_mes_array = np.array(litros_mes)

# exiba as mensagens bem formatadas na tela
print(titulo_array)
print(cogigo_array)
print(inadimplencia_array)
print(regiao_array)
print(litros_mes_array)
