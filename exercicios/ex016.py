#Qual a parte do número antes da vírgula
from math import trunc

num = float(input("Digite um número float -> "))

print(f'A parte inteira de {num} corresponde a {trunc(num)}')

#Maneira mais simples
print(f'\nA parte inteira de {num} corresponde a {int(num)}')
