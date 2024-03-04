# Qnts vezes aparece 'A' e em qual posição

nome = str(input('Digite o nome -> ')).strip().upper()
letra = str(input('Letra a analisar qual letra -> ')).upper()

contagem = nome.count(letra)

primeiroA = nome.find(letra) + 1
ultimoA = nome.rfind(letra) + 1

print('{:=^20}'.format('CONTAGEM'))
print(f"Quantidade de Letras '{letra}' -> {contagem}")

print(f'{"Índices da Letra":=^20}')
print(f'Posição 1º "{letra}" -> {primeiroA}')
print(f'Posição 2º "{letra}" -> {ultimoA}')