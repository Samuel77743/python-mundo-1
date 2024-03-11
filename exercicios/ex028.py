from random import randint
from time import sleep
again = 'S' #Variável usada posteriormente

print(f'{"=-="*10}TENTE ADIVINHAR{"=-="*10}')

while again == 'S':

    num = randint(1, 5)
    print('Em que número o Computador "pensou" entre 1 - 5?')
    resposta = int(input('Sua resposta -> '))

    if resposta == num:
        print(f'Acertou! O computador pensou em {num}')
    else:
        print(f'ERROU! O computador pensou em {num}')
    
        again = str(input('\nGostaria de tentar novamente? [S/N] -> ')).upper()



