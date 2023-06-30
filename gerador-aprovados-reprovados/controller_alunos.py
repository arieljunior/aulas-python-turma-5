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
    
    destinatarios = []
    for aluno in alunos:
        mensagem = ""
        if situacao == "APROVADO":
            mensagem = f"Olá {aluno.nome_completo}\nParabéns, você foi aprovado no curso de Python.\nA média da sua nota foi {aluno.get_media_nota()}"
        elif situacao == "REPROVADO":
            mensagem = f"Olá {aluno.nome_completo}\nObrigado, por fazer parte dessa jornada do nosso curso de Python.\nPorém, a sua nota foi miserávelmente baixa, infelizmente você não terá direito ao ceritificado"
        
        if len(mensagem) > 0:
            destinatarios.append({
                "email": aluno.email,
                "mensagem": mensagem
            })

    enviados = servico_email.enviar_emails(destinatarios, titulo)
    if enviados > 0:
        print(f"Foram enviados {enviados} emails")
    else:
        print("Não foi enviado nenhum email")

    