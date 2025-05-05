from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from docx import Document
import pandas as pd
import smtplib
import os

def processar(remetente, senha, excelEmails, emailsColuna, arquivoDocx, anexos):

    lista_emails = pd.read_excel(excelEmails, usecols=[emailsColuna])

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(remetente, senha)
    
    def ler_docx(Docx):
        doc = Document(Docx)
        texto = []
        for paragraphs in doc.paragraphs:
            texto.append(paragraphs.text)
        return '\n'.join(texto)


    for destinatario in lista_emails[emailsColuna]:

        msg = MIMEMultipart()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = "Teste" #LEMBRE DE ALTERAR LEMBRE DE ALTERAR LEMBRE DE ALTERAR LEMBRE DE ALTERAR LEMBRE DE ALTERAR 

        conteudo_word = ler_docx(arquivoDocx)
        msg.attach(MIMEText(conteudo_word, "plain"))

        arquivos = anexos.split()
        for caminho in arquivos:
            with open(caminho, "rb") as f:
                parte = MIMEBase("application", "octet-stream")
                parte.set_payload(f.read())
            encoders.encode_base64(parte)
            parte.add_header("Content-Disposition", f"attachment; filename={os.path.basename(caminho)}")
            msg.attach(parte)
        
        server.sendmail(remetente, destinatario, msg.as_string())
     
    server.quit()