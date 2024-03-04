# Pedra, Papel Tesoura

from random import choice

escolhas = [
    'Pedra',
    'Papel',
    'Tesoura'
]

print(f'{"PEDRA, PAPEL, TESOURA":=^50}')
respJogador = str(input('SUA RESPOSTA ---> ')).capitalize()
if not(respJogador in escolhas):
    print('Resposta Inválida')

else:
    respCPU = choice(escolhas)
    print(f'\n{"RESULTADO":-^20}')
    print(f'{respJogador} x {respCPU}')

    if respJogador == respCPU:
        print('EMPATE')

    elif respJogador == escolhas[0] and respCPU == escolhas[1]:
        print('CPU Ganhou!')
    elif respJogador == escolhas[1] and respCPU == escolhas[2]:
        print('CPU Ganhou!')
    elif respJogador == escolhas[2] and respCPU == escolhas[0]:
        print('CPU Ganhou')

    else:
        print('Jogador ganhou. Parabéns!')


