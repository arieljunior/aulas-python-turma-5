from aluno import Aluno
from arquivo import criar_arquivo
import servico_email

alunos = [
    Aluno("Joseph", [10,8,9], 'hegef74913@dronetz.com'),
    Aluno("Pedro", [5,3,3], 'hegef74913@dronetz.com')
]


# for aluno in alunos:
#     if aluno.get_situacao() == "APROVADO":
#         alunos_aprovados.append(aluno)
#     else:
#         alunos_reprovados.append(aluno)

def get_alunos_por_situacao(situacao):
    return [aluno for aluno in alunos if aluno.get_situacao() == situacao]

def gerar_arquivo_alunos_aprovados():
    linhas_alunos_aprovados = get_alunos_por_situacao("APROVADO")
    criar_arquivo(
        "gerador-aprovados-reprovados/saida/alunos_aprovados.txt", 
        linhas_alunos_aprovados, 
        "ALUNOS APROVADOS:"
    )

def gerar_arquivo_alunos_reprovados():
    linhas_alunos_reprovados = get_alunos_por_situacao("REPROVADO")
    criar_arquivo(
        "gerador-aprovados-reprovados/saida/alunos_reprovados.txt", 
        linhas_alunos_reprovados, 
        "ALUNOS REPROVADOS:"
    )

def enviar_emails_alunos_por_situacao(situacao, titulo):
    alunos = get_alunos_por_situacao(situacao);
    
    destinatarios = Aluno.montar_lista_destinatarios(alunos, situacao)

    enviados = servico_email.enviar_emails(destinatarios, titulo)
    if enviados > 0:
        print(f"Foram enviados {enviados} emails")
    else:
        print("Não foi enviado nenhum email")

    