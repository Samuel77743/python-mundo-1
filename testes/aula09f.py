#SPLIT extraindo palavras
#Converte string em lista com cada palavra sendo um índice

nome = 'Samuel Silva'
nomeSplit = nome.split()
print(nomeSplit)
heroi = 'Spider-Man'
heroiSplit = heroi.split('-')
print(heroiSplit)

# JOIN unifica as palavras colocando simbolo ou espaço entre 
# LISTA > STRING
texto = ' '.join(nomeSplit)
print(texto)

texto = '-'.join(heroiSplit)
print(texto)