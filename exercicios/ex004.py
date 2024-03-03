#Métodos de String

resp = input('Digite algo -> ')

print('Tipo da variável -> {}'.format(type(resp)))
print('Pode ser convertido em número? {}'.format(resp.isnumeric()))
print('É puramente texto? {}'.format(resp.isalpha()))
print('É texto ou número? {}'.format(resp.isalnum()))
print('É somente espaço(s)? {}'.format(resp.isspace()))

print('\nEstá em maiúsculo? {}'.format(resp.isupper()))
print('Está em minúsculo? {}'.format(resp.islower()))

print("Primeira letra de cada palavra em maiúsculo -> {}".format(resp.istitle()))