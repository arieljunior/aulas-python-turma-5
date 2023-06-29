import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

dotenv.load_dotenv()

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SENHA_LOGIN = os.getenv("SENHA_LOGIN")
HOST = os.getenv("HOST") #smtp.gmail.com
PORTA = os.getenv("PORTA") #587

def enviar_emails():
    # insere informações do servidor gmail (Google)
    servidor = smtplib.SMTP(HOST, PORTA)
    #inicia uma função de segurança
    servidor.starttls()
    #realiza o login com o serviço de email
    servidor.login(EMAIL_LOGIN, SENHA_LOGIN)

    #configura a mensagem de email
    mensagem = MIMEMultipart()
    mensagem['From'] = EMAIL_LOGIN
    mensagem['To'] = 'ariel.junior@al.infnet.edu.br'
    mensagem['Subject'] = 'segundo teste'

    #configura o corpo do email
    conteudo_email = MIMEText("blablalblalbla", 'plain')
    mensagem.attach(conteudo_email)

    servidor.send_message(mensagem)
    servidor.quit()

