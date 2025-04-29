from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from docx import Document
import pandas as pd
import smtplib
import os

def processar(remetente, senha, excelEmails, emailsColuna, arquivoDocx):

    lista_emails = pd.read_excel(excelEmails, usecols=[emailsColuna])

    msg = MIMEMultipart()
    msg["From"] = remetente

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(remetente, senha)
    
    def ler_docx(Docx):
        doc = Document(Docx)
        texto = []
        for paragraphs in doc.paragraphs:
            texto.append(paragraphs.text)
        return '\n'.join(texto)


    for destinatario in lista_emails[emailsColuna]:

        msg["To"] = destinatario
        msg["Subject"] = "Teste"

        conteudo_word = ler_docx(arquivoDocx)
        msg.attach(MIMEText(conteudo_word, "plain"))
        
        server.sendmail(remetente, destinatario, msg.as_string())
     
    server.quit()