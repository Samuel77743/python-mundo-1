# O nome é 'Santo'?

nome = str(input('Informe o nome -> '))
fatiarNome = nome.split()

print('O nome é "Santo"? {}'.format(fatiarNome[0] == 'Santo'))


# Código ineficaz:
# print('O nome é Santo -> {}'.format(nome[:5] == 'Santo'))
