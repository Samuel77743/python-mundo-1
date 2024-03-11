# É par ou ímpar

print(f'\n{"É PAR OU ÍMPAR?":-^20}')

try:
    resp = int(input('Digite o número -> '))
    print('Par' if resp % 2 == 0 else 'Ímpar')
except ValueError:
    print('Digite apenas números inteiros!')