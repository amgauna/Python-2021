# CPF 
# Deve ser incluído um teste se o CPF possui 11 dígitos e preencher com zeros 
# a esquerda se forem menos dígitos, desta forma a formatação fica correta para 
# CPFs que começam com zero

teste = input("CPF: ") # 12345678900
if len(teste) < 11:
    teste = teste.zfill(11)
cpf = '{}.{}.{}-{}'.format(teste[:3], teste[3:6], teste[6:9], teste[9:])
print(cpf) # 123.456.789-00
