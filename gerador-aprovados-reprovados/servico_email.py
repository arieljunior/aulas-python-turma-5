import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv
import arquivo 
import datetime
dotenv.load_dotenv()

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
SENHA_LOGIN = os.getenv("SENHA_LOGIN")
HOST = os.getenv("HOST") #smtp.gmail.com
PORTA = os.getenv("PORTA") #587

def gerar_arquivo_log_erro(log_erros):
    data_hora_atual = datetime.datetime.today().strftime('%d_%m_%y_%H_%M_%S')
    arquivo.criar_arquivo(
        f"gerador-aprovados-reprovados/saida/erros/log-erro-emails{data_hora_atual}.txt", 
        log_erros, 
        f"Erros de email ({data_hora_atual}):"
    )

def enviar_emails(destinatarios, titulo_email = "nome generico q vou pensar dps"):
    log_erros = []
    emails_enviados = 0
    # insere informações do servidor gmail (Google)
    servidor = smtplib.SMTP(HOST, PORTA)
    try:
        #inicia uma função de segurança
        servidor.starttls()
        #realiza o login com o serviço de email
        servidor.login(EMAIL_LOGIN, SENHA_LOGIN)
        for destinatario in destinatarios:
            #configura a mensagem de email
            mensagem = MIMEMultipart()
            mensagem['From'] = EMAIL_LOGIN
            mensagem['To'] = destinatario['email']
            mensagem['Subject'] = titulo_email

            #configura o corpo do email
            conteudo_email = MIMEText(destinatario['mensagem'], 'plain')
            mensagem.attach(conteudo_email)
            try:
                servidor.send_message(mensagem)
                emails_enviados += 1
            except smtplib.SMTPRecipientsRefused:
                log_erros.append(f"o email ({destinatario['email']}) não é valido")
            except:
                log_erros.append(f"o email ({destinatario['email']}) não é valido")
                pass
            del mensagem
    except:
        log_erros.append("Problemas no serviço de envio de email")
    finally:
        servidor.quit()
        if len(log_erros) > 0:
            gerar_arquivo_log_erro(log_erros)
        return emails_enviados
    
