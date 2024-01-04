arquivo = open("texto.txt", "w") # "w" sobresecreve todo o conteudo
arquivo.write("Ola, Mundo!\n")

arquivo = open("texto.txt", "a") # "a" anexa novo conteudo sem sobrescrever
arquivo.write("Minha segunda linha\n")

#arquivo = open("texto.txt", "w") 
# se eu só abrir um novo "w" mesmo que não use o write, tudo já escrito usando "w" vai sumir, com "a" fica

#arquivo.write("") 
# abrir o texto.txt com "w" e enviar uma string vazia com o write irá limpar tudo que estiver no arquivo até "a"


arquivo.close()