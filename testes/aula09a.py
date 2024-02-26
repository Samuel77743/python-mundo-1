# Manipulando Strings
# Básicos
frase = 'Você foi agora a coisa mais importante que já me aconteceu neste momento até hoje em toda a minha vida'

#Maiúsculo:
print('{:=^30}'.format('MAIÚSCULO'))
teste = frase.upper()
print(teste)

#Minúsculo:
print('\n{:=^30}'.format('minúsculo'))
teste = frase.lower()
print(teste)

#Capitalize
print('\n{:=^30}'.format('O capitalize'))
teste = frase.capitalize()
print(teste)

#Title
print('\n{:=^30}'.format('O Título'))
teste = frase.title()
print(teste)