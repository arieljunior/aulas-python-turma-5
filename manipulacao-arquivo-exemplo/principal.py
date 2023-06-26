
# w = write (escrever no arquivo)
# r = read (ler o arquivo)
# x = Escrita, Retorna um erro caso o arquivo não exista

def ler_arquivo():
    arquivo = open("manipulacao-arquivo-exemplo/exempl.txt", "r", encoding="utf8")
    #Forma 1 de ler um arquivo
    resultado = arquivo.read()
    print(resultado)

    #Forma 2 de ler um arquivo
    # resultado = arquivo.readline(3)
    # print(resultado)

    #Forma 3 de ler um arquivo
    # linhas = arquivo.readlines()
    # for linha in linhas:
    #     print(linha)
    arquivo.close()

def escrever_arquivo():
    arquivo = open("manipulacao-arquivo-exemplo/exemplo.txt", "w", encoding="utf8")
    # arquivo.write(["linha 1", "linha 2"])
    arquivo.writelines(["linha 1\n", "linha 2"])
    arquivo.close()

def ler_arquivo_com_with():
    with open("manipulacao-arquivo-exemplo/exemplo.txt", "r", encoding="utf8") as arquivo:
        conteudo = arquivo.readlines()
        print(conteudo)

# ler_arquivo()
# escrever_arquivo()
ler_arquivo_com_with()