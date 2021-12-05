import numpy as np

# criando os arrays
np.codigo = [47798, 88333, 71928, 74830, 42536]
np.inadimplencia = [1:'SIM', 0:'NAO'}
np.regiao = [1:'regiao-centro', 2:'regiao_grande_ibis', 3:'regiao_grande_aribiri', 4:'regiao_grande_cobilandia', 5:'regiao_grande_jucu"]
np.litros_mes = [85, 106, 69, 88, 65]
          
# crie um hash vazio chamado 's'
s = {}

# use uma atribuição múltipla para atribuir os dados divididos de 'array a 's'.
(s['codigo'].s['inadimplencia'].s['regiao'].s['litros_mes'])  = np.split('i')

# exiba 6 mensagens bem formatadas na tela
print("CODIGO  " + s['codigo'])
print("INADIMPLENCIA " + s['inadimplencia'])
print("REGIAO     " + s['regiao'])
print("LITROS/MES:  " + s['litros_mes'])
