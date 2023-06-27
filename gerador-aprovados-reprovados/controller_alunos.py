# Objetivo: Gerar uma lista de alunos aprovados e reprovados
# - pegar os dados dos alunos - ok
# - validar a média das notas dos aprovados e reprovados - ok
# - criar um arquivo de texto com os aprovados e outro arquivo de texto com os reprovados

from aluno import Aluno
from arquivo import criar_arquivo

alunos = [
    Aluno("Fulano", [10,8,9]),
    Aluno("Beltrano", [5,4,3]),
    Aluno("Ciclano", [10,10,10]),
    Aluno("Pedro", [5,3,9])
]


# for aluno in alunos:
#     if aluno.get_situacao() == "APROVADO":
#         alunos_aprovados.append(aluno)
#     else:
#         alunos_reprovados.append(aluno)


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