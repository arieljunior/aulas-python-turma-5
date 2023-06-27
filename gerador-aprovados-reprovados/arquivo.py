def criar_arquivo(caminho_arquivo, linhas, titulo):
    linhas.insert(0, f"{titulo}\n")
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        arquivo.writelines(linhas)