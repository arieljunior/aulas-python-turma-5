
# w = write (escrever no arquivo)
# r = read (ler o arquivo)
arquivo = open("manipulacao-arquivo-exemplo/exemplo.txt", "r", encoding="utf8")

resultado = arquivo.read()
print(resultado)

arquivo.close()