from aluno import Aluno
from arquivo import criar_arquivo

alunos = [
    Aluno("Fulano", [10,8,9], 'elfutec9@elfutec.page'),
    Aluno("Beltrano", [5,4,3], 'elfutec9@elfutec.page'),
    Aluno("Ciclano", [3,3,3], 'elfutec9@elfutec.page'),
    Aluno("Pedro", [5,3,9], 'elfutec9@elfutec.page')
]


# for aluno in alunos:
#     if aluno.get_situacao() == "APROVADO":
#         alunos_aprovados.append(aluno)
#     else:
#         alunos_reprovados.append(aluno)

def get_alunos_aprovados():
    return [aluno for aluno in alunos if aluno.get_situacao() == "APROVADO"]

def gerar_arquivo_alunos_aprovados():
    linhas_alunos_aprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "APROVADO"]
    criar_arquivo(
        "gerador-aprovados-reprovados/saida/alunos_aprovados.txt", 
        linhas_alunos_aprovados, 
        "ALUNOS APROVADOS:"
    )

def gerar_arquivo_alunos_reprovados():
    linhas_alunos_reprovados = [f"{aluno.get_linha_arquivo()}\n" for aluno in alunos if aluno.get_situacao() == "REPROVADO"]
    criar_arquivo(
        "gerador-aprovados-reprovados/saida/alunos_reprovados.txt", 
        linhas_alunos_reprovados, 
        "ALUNOS REPROVADOS:"
    )

def enviar_emails_alunos_aprovados():
    alunos = get_alunos_aprovados();
    for aluno in alunos:
        print(f"{aluno.nome_completo} {aluno.email}")