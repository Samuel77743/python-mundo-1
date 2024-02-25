#Calculando Área

print('{:=^20}\n'.format('CALCULANDO ÁREA'))

altura = float(input('ALTURA -> '))
largura = float(input('LARGURA -> '))

area = altura*largura
litrosNecess = area/2

print('\nÁREA -> {:.2f}m²'.format(area))
print('QNT DE LITRO NECESSÁRIA -> {:.2f} Litros'.format(litrosNecess))

