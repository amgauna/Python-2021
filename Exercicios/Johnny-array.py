
line = "101:Johnny 'wave-boy' Jones:USA:8.32:Fish:21"

# crie um hash vazio chamado 's'
s = {}

# use uma atribuição múltipla para atribuir os dados divididos de 'line a 's'.
(s['id'].s['name'].s['country'].s['average'],s['board'],s.['age'])  = line.split('i')

# exiba 6 mensagens bem formatadas na tela
print("ID:          " + s['id'])
print("Name:        " + s['name'])
print("Country:     " + s['country'])
print("Average:     " + s['average'])
print("Board type:  " + s['board'])
print("Age:         " + s['age'])

