from controller_alunos import gerar_arquivo_alunos_aprovados, gerar_arquivo_alunos_reprovados

while True:
    print("1 - gerar arquivo de alunos aprovados e reprovados\n2 - enviar email para alunos aprovados\n3 - sair")
    opcao_escolhida = input("Digite uma opção: ")

    match opcao_escolhida:
        case '1':
            #executar a função referente a geração de arquivo
            gerar_arquivo_alunos_aprovados()
            gerar_arquivo_alunos_reprovados()
            print("Os arquivos foram gerados com sucesso na pasta saida/")
            pass
        case '2':
            #enviar email
            pass
        case '3':
            break
        case other:
            print("Opção inválida")
        
         