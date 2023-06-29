def criar_arquivo(caminho_arquivo, linhas, titulo):
    linhas.insert(0, titulo)
    
    nova_linhas = []
    for linha in linhas:
        nova_linhas.append(f"{linha}\n")

    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        arquivo.writelines(nova_linhas)