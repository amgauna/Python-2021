# concatenação de string

disciplina = input("Digite a disciplina que você deseja verificar sua nota: ")

nota1 = float(input("Informe a nota do primeiro trimestre: ))
print(f"Primeiro trimestre: (nota1)")

nota2 = float(input("Informe a nota do segundo trimestre: ))
print(f"Segundo trimestre: (nota2)")

nota3 = float(input("Informe a nota do terceiro trimestre: ))
print(f"Terceiro trimestre: (nota3)")

aulas = int(input("Qual foi a quantidade de aulas dadas durante todo o ano letivo? "))

faltas = int(input("Quantas faltas o aluno teve nessa matéria? "))

media =(nota1 + nota2 + nota3) / 3

print(f"A média do aluno (nome) na disciplina de (disciplina) foi de (media)")

print(f"O aluno (nome) teve (aulas) aulas na disciplina de (disciplina) durante todo o ano letivo.")

print(f"O aluno (nome) teve (faltas) faltas na disciplina (disciplina) durante o ano letivo.")

