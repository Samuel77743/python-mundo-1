# Descobrindo a hipotenusa
from math import hypot, sqrt

print('{:=^40}'.format('CALCULANDO HIPOTENUSA'))
catOp = float(input('Qual a largura do Cateto Oposto -> '))
catAdj = float(input('Qual a largura do Cateto Adjacente -> '))

hipotenusa = hypot(catAdj, catOp)
print(f'Valor da HIPOTENUSA -> {hipotenusa}')

# MANEIRA MANUAL DE SE CALCULAR A HIPOTENUSA

hipotenusa = catAdj**2 + catOp**2
hipotenusa = sqrt(hipotenusa)

print(f'VALOR DA HIPOTENUSA -> {hipotenusa}')