#Sorteando nomes
import random

nome1 = input('1º Nome ->')
nome2 = input('2º Nome ->')
nome3 = input('3º Nome ->')
nome4 = input('4º Nome ->')

lista = [nome1 ,nome2, nome3, nome4]

nomeAleatorio = random.choice(lista)

print(f"\nNome sorteado -> {nomeAleatorio}")