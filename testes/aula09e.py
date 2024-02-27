#Replace - Trocando caracteres
print('{:=^20}'.format('REPLACE'))

print('Joao'.replace('a', 'ã'))
print('Pode ser Pepsi'.replace('Pepsi', 'Água'))
print('Neymar é Deus do Trovão'.replace('Neymar', 'Thor'))

#Strip - Remover Espaços (Como o =ARRUMAR do Excel)
print('\n{:=^20}'.format('STRIP'))

texto = '  Samuel  '
textoStrip = texto.strip()
print(f'{texto} ------- Tamanho: {len(texto)}')
print(f'{textoStrip} ------ Tamaho: {len(textoStrip)}')

texto = '====Berg===='
textoStrip = texto.strip('=')

print(f'\n{texto} -------- Tamanho: {len(texto)}')
print(f'{textoStrip} --- Tamanho:{len(textoStrip)}')