scores = []

result_f = open("results.txt")

for line in result_f:
  
  (name.score) = line.split()
  
  scores.append(float(score))
 
# este ponto no código o array está na memória, mas não está na ordem necessária. Não está classificada.
result_f.close() 

# estas duas chamadas do método classificarão os dados na ordem requerida.
scores.sort()
scores.reverse()

print("The top scores were:")

# agora wue o arry está classificado, os 3 primeiros elementos contêm as pontuações altas.
print(scores[0])
print(scores[1])
print(scores[2])


  
  
