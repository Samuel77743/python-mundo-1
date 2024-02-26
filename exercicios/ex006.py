#Dobro, triplo e Raíz Quadrada

resp = int(input('Digite o número -> '))
dobro = resp*2
triplo = resp*3
raiz = resp**(1/2)

print('{:=^20}'.format('DOBRO'))
print('dobro -> {}'.format(dobro), end='\n\n')

print('{:=^20}'.format('TRIPLO'))
print('triplo -> {}'.format(triplo), end='\n\n')

print('{:=^20}'.format('RAÍZ QUADRADA'))
print('raíz quadrada -> {:.2f}'.format(raiz))