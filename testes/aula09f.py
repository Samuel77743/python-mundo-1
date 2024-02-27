#SPLIT extraindo palavras
#Converte string em lista com cada palavra sendo um índice

nome = 'Samuel Silva'
nomeStrip = nome.split()
print(nomeStrip)

#JOIN unifica as palavras colocando simbolo ou espaço entre
texto = ', '.join(nomeStrip)
print(texto)