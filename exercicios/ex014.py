# De Cº para Fº

print('{:=^20}'.format('CELSIUS >>> FAHRENHEIT'))
celsius = float(input('Digite o valor em Cº -> '))

fahrenheit = (celsius * 9/5) + 32

print('{:.1f} Cº >>>>> {:.1f} Fº'.format(celsius, fahrenheit))