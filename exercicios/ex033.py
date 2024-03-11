# O ano é bissexto ou não é?
#Para o ano ser Bissexto ele precisa:
# - Ser divisível por 4
# - Os anos que forem múltiplos de 100 também devem ser divisíveis por 400

print(f'{"ANO É BISSEXTO?":-^20}')
print('DICA: Se colocar "0" corresponderá ao ano atual\n')
ano = int(input('Digite o ano -> '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é bissexto')

else:
    print(f'{ano} não é bissexto')