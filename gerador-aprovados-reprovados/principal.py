import controller_alunos

while True:
    print("1 - gerar arquivo de alunos aprovados e reprovados\n2 - enviar email para alunos aprovados\n3 - sair")
    opcao_escolhida = input("Digite uma opção: ")

    match opcao_escolhida:
        case '1':
            #executar a função referente a geração de arquivo
            controller_alunos.gerar_arquivo_alunos_aprovados()
            controller_alunos.gerar_arquivo_alunos_reprovados()
            print("Os arquivos foram gerados com sucesso na pasta saida/")
        case '2':
            #enviar email
            controller_alunos.enviar_emails_alunos_aprovados()
        case '3':
            break
        case other:
            print("Opção inválida")
        
         