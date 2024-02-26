# Aluguel de carro
# Diária: 60 reais
# Tarifa por KM rodado: 0,15 reais

print('_'*23)
print('|{:^10}|{:^10}|'.format('Diária', 'Por KM'))
print('-'*23)
print('|{:^10}|{:^10}|'.format('R$ 60.00', 'R$ 0,15'))
print('-'*23)

dias = int(input('Quantos dias permaneceu com o carro -> '))
km = float(input('Quantos KMs foram percorridos -> '))

valorDias = dias*60
valorKm = km*0.15

tarifa = valorDias + valorKm

print('\n{:=^22}'.format('VALOR A PAGAR'))
print('Por dias ({:2} dias)----> R$ {:.2f}'.format(dias, valorDias))
print('Por KM({:.2f} Km) --------> R$ {:.2f}'.format(km, valorKm))
print('\nTOTAL ----> R$ {:.2f}'.format(tarifa))

