from unittest import main, TestCase
from aluno import Aluno

class AlunoTeste(TestCase):
    def setUp(self):
        super().setUp()
        self.aluno = Aluno("Teste", [10,9,9], "teste@teste.com")

    def testar_media_nota(self):
        self.aluno.notas = [10,5]
        media = self.aluno.get_media_nota()

        total = 0
        for nota in self.aluno.notas:
            total += nota
        media_esperada = round(total / len(self.aluno.notas), 1)
        self.assertEqual(media, media_esperada, "Erro no calculo de média da nota")
    
    def testar_situacao(self):
        situacao_aprovado = self.aluno.get_situacao()
        self.aluno.notas = [5,5]
        situacao_reprovado = self.aluno.get_situacao()

        self.assertEqual(situacao_aprovado, "APROVADO", "Erro na validação de situação aprovado")
        self.assertEqual(situacao_reprovado, "REPROVADO", "Erro na validação de situação reprovado")

    def teste_get_linha_arquivo(self):
        linha = self.aluno.get_linha_arquivo()
        media = self.aluno.get_media_nota()
        situacao = self.aluno.get_situacao()

        media_esta_dentro_da_linha = linha.find(str(media)) > -1
        situacao_esta_dentro_da_linha = linha.find(situacao) > -1
        nome_esta_dentro_da_linha = linha.find(self.aluno.nome_completo) > -1
        self.assertTrue(media_esta_dentro_da_linha, "Media do aluno não esta na linha para gerar o arquivo")
        self.assertTrue(situacao_esta_dentro_da_linha, "Situação do aluno não esta na linha para gerar o arquivo")
        self.assertTrue(nome_esta_dentro_da_linha, "Nome completo do aluno não esta na linha para gerar o arquivo")

    def testar_montagem_lista_destinatarios(self):
        destinatarios = Aluno.montar_lista_destinatarios([self.aluno], "APROVADO")

        tem_chave_email = False
        tem_chave_mensagem = False

        for destinatario in destinatarios:
            if "email" in destinatario:
                tem_chave_email = True
            if "mensagem" in destinatario:
                tem_chave_mensagem = True

        self.assertTrue(tem_chave_email, "Não foi encontrado a chave email")
        self.assertTrue(tem_chave_mensagem, "Não foi encontrado a chave mensagem")

if __name__ == "__main__":
    main()