#Imprimindo Cosseno, seno e tangente
from math import sin, cos, tan, radians

angulo = int(input('Digite o valor do Ângulo -> '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Seno -> {seno:.2f}')
print(f'Cosseno -> {cosseno:.2f}')
print(f'Tangente -> {tangente:.2f}')