import json
import os

CONFIG_FILE = 'config.json'

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "email": "",
            "senha": "",
            "excelEmails": "",
            "emailsColuna": "",
            "arquivoDocx": "",
            "anexos": ""
        }
    
def salvar_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)