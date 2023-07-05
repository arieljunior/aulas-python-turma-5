class Aluno():
    def __init__(self, nome_completo, notas, email):
        self.nome_completo = nome_completo
        self.notas = notas
        self.email = email

    def get_media_nota(self):
        total = 0
        for nota in self.notas:
            total += nota
        media = total / len(self.notas)
        return round(media, 1)
    
    def get_situacao(self):
        media = self.get_media_nota()
        if media >= 7:
            return "APROVADO"
        else:
            return "REPROVADO"
        
    def get_linha_arquivo(self):
        media = self.get_media_nota()
        situacao = self.get_situacao()
        return f"{self.nome_completo} | media: {media} | situacao: {situacao}"
    
    @staticmethod
    def montar_lista_destinatarios(alunos, situacao):
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
        return destinatarios