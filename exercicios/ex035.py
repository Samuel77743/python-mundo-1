#Aumento de Salário
# Maiores que 1250: 10%
# Abaixo ou igual a 1250: 15%

print(f'\n{"CALCULANDO SALÁRIO":-^20}')

salarioAtual = float(input('Qual o salário atual -> R$ '))

if salarioAtual > 1250:
    novoSalario = salarioAtual + salarioAtual * 10/100
else:
    novoSalario = salarioAtual + salarioAtual * 15/100

print(f'{"CONCLUSÃO":-^20}')
print(f'Salário Antigo -> R$ {salarioAtual:.2f}')
print(f'Salário atualizado -> R$ {novoSalario:.2f}')