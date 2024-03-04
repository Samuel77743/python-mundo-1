# Primeiro e Último nome

nome = str(input('Qual o nome -> ')).split()

firstName = nome[0]
lastName = nome[len(nome)-1]

print(f'{"RESULTADO":=^20}')
print(f'Primeiro nome ---> {firstName}')
print(f'Último nome -----> {lastName}')