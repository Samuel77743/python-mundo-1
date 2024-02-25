#Dobro, triplo e Raíz Quadrada

resp = int(input('Digite o número -> '))

print('{:=^20}'.format('DOBRO'))
print('dobro -> {}'.format(resp*2), end='\n\n')

print('{:=^20}'.format('TRIPLO'))
print('triplo -> {}'.format(resp*3), end='\n\n')

print('{:=^20}'.format('RAÍZ QUADRADA'))
print('raíz quadrada -> {:.0f}'.format(resp**(1/2)))