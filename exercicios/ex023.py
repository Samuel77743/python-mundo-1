# Qnts Unidades, Dezenas e Centenas

resp = int(input('Digite o número -> '))

respFormatada = str('{:04.0f}'.format(resp))

print('{:=^20}'.format(resp))

print(f'Unidade -----------> {respFormatada[3]}')
print(f'Dezena ------------> {respFormatada[2]}')
print(f'Centena -----------> {respFormatada[1]}')
print(f'Unidade de Milhar -> {respFormatada[0]}')