#Analisando Texto

nome = input("Escreva seu nome completo -> ")

print("\n{:=^20}".format('RESULTADO'))
print(f'Em maiúsculo -> {nome.upper()}')
print(f'Em minúsculo -> {nome.lower()}')

print('Quantidade de letras no NOME COMPLETO')
print('RESPOSTA -> {}'.format(len(nome) - nome.count(' ')))

#Primeira maneira
#Usando find()
print(f"(find) Quantidade de Letras no 1º nome -> {nome.find(' ')}")

# Segunda maneira
# Split para retornar lista, porém quero apenas a do primeiro indice
primeiroNome = nome.split()[0]
print(f'(split) Quantidade de letras no 1º nome -> {len(primeiroNome)}')