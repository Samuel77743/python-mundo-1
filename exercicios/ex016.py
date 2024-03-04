#Qual a parte do número antes da vírgula
from math import trunc, floor

num = float(input("Digite um número float -> "))

print(f'A parte inteira de {num} corresponde a {trunc(num)}')

#Maneira mais simples
print(f'\nA parte inteira de {num} corresponde a {int(num)}')

# Dividindo por 1 com // (mas continua com .)
print(f'\nA parte inteira de {num} corresponde a {num//1}')

#Última forma
print(f'Arredondado para baixo -> {floor(num)}')
