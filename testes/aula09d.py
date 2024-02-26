#Manipulando Strings
# FIND e IN

#FIND diz o índice ou dá menos 1 se não achar
print('{:=^20}'.format('FIND'))
print('João'.find('ã'))
print('João'.find('o', 2))
print('Samuel'.find('y'))

#Operador IN - Retorna True e False
print('{:=^20}'.format('Operador IN'))
print('el' in 'Samuel')
print('a' in 'Creuzebeck')
print('a' in 'André'.lower())