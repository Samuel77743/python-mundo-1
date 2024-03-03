# Separando U.M., C, D, U

num = int(input('Informe o número -> '))

print('{:=^20}'.format('DECOMPOSIÇÃO'))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
unMilhar = num // 1000 % 10   

print(f'\nUNIDADE -------> {unidade}')
print(f'DEZENA ----------> {dezena}')
print(f'CENTENA ---------> {centena}')
print(f'UN. DE MILHAR ---> {unMilhar}')