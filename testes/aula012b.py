# Organizando códigos de cores em dicionário

cores = {
    "limpa":'\033[m',
    "negrito":'\033[4m',
    "azul":"\033[34m",
    "amarelo-sub":"\033[4;33m"
}

print('{}Será{} que o livro do {}"Pequeno Príncipe"{} é {}bom?{}'.format(cores['negrito'], cores['limpa'], cores['amarelo-sub'], cores['limpa'], cores['azul'], cores['limpa']))