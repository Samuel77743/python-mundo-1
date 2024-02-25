resp = input('Digite um título -> ')

print('Alinhamento À Esquerda:')
print('{:<20}'.format(resp), end='\n\n')

print('Alinhamento Centralizado:')
print('{:^20}'.format(resp), end='\n\n')

print('Alinhamento À Direita:')
print('{:>20}'.format(resp), end='\n\n')

print('{:^30}'.format("Com caractéres de enfeite"))
print('{:-^50}'.format(resp))