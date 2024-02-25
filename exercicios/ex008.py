#Convertendo metros em centímetros

print('{:=^30}'.format('Convertendo M em CM'))
metros = float(input('Qual a medida em Metros? '))

cm = metros*100

print('\n{:.2f}m >>> {:.2f}cm'.format(metros, cm))