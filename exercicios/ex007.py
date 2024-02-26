#Cálculo de Média

print('{:=^20}'.format("Calculando Média"))
nota1 = int(input('Digite a nota da 1º nota -> '))
nota2 = int(input('Digite a nota da 2º nota -> '))

media = (nota1 + nota2) / 2

print('\nA média entre {:.2f} e {:.2f} é igual a {:.2f}'.format(nota1, nota2, media))