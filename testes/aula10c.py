# Todos tipos de Operadores Relacionais
#   = < > <= >= NOT

num = int(input('Digite um número entre 1 e 10 -> '))

if (num > 10) or (num < 0):
    print('Resposta Inválida')
else:
    if num == 5:
        print(f'{num} é igual a 5')
    elif num < 5:
        print(f'{num} é menor que 5')
    else:
        print(f'{num} é maior que 5')

