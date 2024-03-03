#Manipulando Strings
#Tamanho e contagem de texto

frase = 'eae man'

#Qnt de Caracteres
print('{:=^20}'.format('Qnt de caracteres'))
teste = len(frase)
print(teste)
print(len(str(1000)))

#Contagem de texto
print('\n{:=^20}'.format('Contagem de Texto'))
teste = 'Minha Brasília Amarela'.count('a')
print(teste)

# Jesus
teste = 'super super man'.count('super')
print(teste)
teste = 'super super man'.count('super', 0, 5)
print(teste)