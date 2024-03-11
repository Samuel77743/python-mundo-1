# Calcular preço de viagem
# 0,50 por km para viagens de até 200Km
# 0,45 por km para viagens além

print(f'{"CALCULAR VIAGEM":-^20}')

distancia = float(input('Qual a distância em Km da viagem? '))

print(f'{"PREÇO DA VIAGEM":=^20}')

if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia

print(f'VALOR A PAGAR -> R$ {preco:.2f}')
