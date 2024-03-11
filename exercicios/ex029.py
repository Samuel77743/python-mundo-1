# Se a velocidade do carro ultrapassar 80, multa 
# de 7 reais por cada KM ultrapassado

print(f'\n{"RADAR":-^15}')
vel = float(input('Qual a velocidade do veículo -> '))

if vel > 80:
    print(f'{"ACIMA DO LIMITE !":=^15}')
    velUltrapassada = vel - 80
    multa = velUltrapassada * 7
    print(f'Velocidade do veículo: {vel} KM/h')
    print(f'Velocidade excedida: {velUltrapassada} KM/h acima do limite')
    print(f'Multa -------> R$ {multa:.2f}')

else:
    print(f'Velocidade de {vel:.2f} KM/h adequada =)')