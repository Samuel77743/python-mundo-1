#PRODUTO COM DESCONTO

print('{:_^30}'.format('Produto com Desconto'))

valor = float(input('{:^25}'.format('Qual o valor do produto -> ')))
desconto_por = float(input('{:^25}'.format('Qual a % de Desconto -> ')))

desconto_val = valor*(desconto_por/100)
valor_desconto = valor - desconto_val

print('\n{:=^20}'.format('SUBTOTAL'))

print('R$ {:.2f}\n-'.format(valor))
print('R$ {:.2f}'.format(desconto_val))
print('R$ {:.2f}'.format(valor_desconto))