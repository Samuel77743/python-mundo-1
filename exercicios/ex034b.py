# Programa que ler 3 números e fala qual o maior e menor

print(f'{"MAIOR e MENOR":-^20}')

ordinal = 1

while ordinal <= 3:
    num = int(input(f'DIGITE O {ordinal}º número -> '))
    
    #Caso seja a primeira iteração
    if ordinal == 1:
        maior = num
        menor = num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    ordinal += 1

print(f'Menor -> {menor}\nMaior -> {maior}')    