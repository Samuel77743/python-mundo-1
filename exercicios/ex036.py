# Pode-se criar um triângulo?
# Como saber:
# - Nenhuma reta pode ser maior do que a soma das outras duas

# Linha para título
def linha():
    print('-='*10)

#Começo    
linha()
print(f'{"TRIÂNGULO":-^20}')
linha()

retas = []
ordinal = 1
while ordinal <= 3:
    retas.append(int(input(f'Qual o tamanho da {ordinal}º reta -> '))) 
    ordinal += 1

reta1Verif = retas[0] < (retas[1] + retas[2])
reta2Verif = retas[1] < (retas[0] + retas[2])
reta3Verif = retas[2] < (retas[0] + retas[1])

info = f"""
    Reta 1 -> {retas[0]}
    Reta 2 -> {retas[1]}
    Reta 3 -> {retas[2]}"""

if reta1Verif and reta2Verif and reta3Verif:
    print(f"\nÉ possível formar um triângulo com as medidas:{info}")

else:
    print(f'\nNÃO é possível formar um triângulo com as medidas:{info}')
    




