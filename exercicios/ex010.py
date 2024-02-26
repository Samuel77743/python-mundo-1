#QUANTOS DÓLARES A PESSOA PODE COMPRAR?

print('{:-^20}'.format('REAL >>> DÓLAR'))

cotacao = 4.98

real = float(input('Quantos Reais você tem -> R$ '))
dolar = real/cotacao

print("\nCONVERSÃO:")
print('R$ {:.2f} >>> U$ {:.2f}'.format(real, dolar))