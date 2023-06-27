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