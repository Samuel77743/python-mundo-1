#Aumento de Salário

salario = float(input('Qual o valor do salário -> R$ '))
aumento = float(input('% do aumento -> '))

aumento = aumento/100 #convertendo em porcentagem
novoSalario = salario + salario*aumento

print('{:=^20}'.format('CONCLUSÃO'))
print('Salário atual ----> R$ {:.2f}'.format(salario))
print('Valor do aumento -> R$ {:.2f} ({:.0f}%)'.format(salario*aumento, aumento*100))
print('NOVO SALÁRIO -----> R$ {:.2f}'.format(novoSalario))