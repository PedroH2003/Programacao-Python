# Abertura do arquivo em modo de leitura
with open("texto.txt", "r") as arquivo: 
    for linha in arquivo: # Para cada linha no arquivo
        print(linha, end="") # Imprima essa linha


print("\n")
with open("texto02.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.rstrip())

print("\n")
with open("texto.txt", "r") as arquivo:
    print(arquivo.read(), end="")


print("\n")
with open("texto02.txt", "r") as arquivo:
    print(arquivo.readline(), end="") # Imprime primeira linha
    print(arquivo.readline(), end="") # Imprime segunda linha


print("\n")
with open("texto.txt", "r") as arquivo:
    # Armazena as linhas na lista "linhas"
    linhas = arquivo.readlines() 

for linha in linhas: # Para cada linha da lista
    print(linha, end="") # Imprima a linha


