lista = [
    "Primeira linha\n",
    "Segunda linha\n"
]

arquivo = open("texto02.txt", "w")
arquivo.writelines(lista)

arquivo.close()