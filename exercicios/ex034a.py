# Programa que ler 3 números e fala qual o maior e menor

print(f'{"MAIOR e MENOR":-^20}')

resp1 = int(input('Digite o 1º número -> '))
resp2 = int(input('Digite o 2º número -> '))
resp3 = int(input('Digite o 3º número -> '))

menor = resp1
maior = resp1

if resp2 < menor and resp2 < resp3:
    menor = resp2

elif resp3 < menor:
    menor = resp3

if resp2 > maior and resp2 > resp3:
    maior = resp2

elif resp3 > maior:
    maior = resp3

print(f'Maior -> {maior}\nMenor -> {menor}') 


