import tkinter as tk
from tkinter import filedialog as fd
import pyautogui
import backend

# _Libaries_ ^

window = tk.Tk()
window.title('Automação de Email')

largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()

largura_window = int(largura_tela * 0.7)
altura_window = int(altura_tela * 0.7)

pos_x = (largura_tela - largura_window) // 2
pos_y = (altura_tela - altura_window) // 2

window.geometry(f"{largura_window}x{altura_window}+{pos_x}+{pos_y}")
window.minsize(largura_window, altura_window)

fontSize = 11

# _Window Config_ ^

# Essas três funções são estupidas, vou fazer uma função que faz tudo unificado depois
def select_file_xlsx():
    filename = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if filename != '':           
        selectedExcel.delete(0, tk.END)
        filename = filename.replace('/', '\\')
        selectedExcel.insert(0, filename)
    else: 
        pass

def select_file_docx():
    filename = fd.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if filename != '':           
        docxFile.delete(0, tk.END)
        filename = filename.replace('/', '\\')
        docxFile.insert(0, filename)
    else: 
        pass

def select_files():
    filename = fd.askopenfilenames()
    if filename != '':
        anexoFile.insert(0, filename)
    else: 
        pass

def PegarDados():
    
    emailValor = email.get().strip()
    senhaValor = senha.get().strip()
    sendSelectedExcel = selectedExcel.get().strip()
    receiver = columnName.get().strip()
    sendDocxFile = docxFile.get().strip()
    sendFiles = anexoFile.get().strip()

    if not all([emailValor, senhaValor, sendSelectedExcel, receiver, sendDocxFile]):
        return pyautogui.alert(text="Atenção! É necessário preencher todos os campos antes de continuar", title="Erro")

    backend.processar(emailValor, senhaValor, sendSelectedExcel, receiver, sendDocxFile, sendFiles)


# _Functions_ ^


email_label = tk.Label(text="Email:", font=("Arial", fontSize))
email = tk.Entry(window, font=("Arial", fontSize), width=45)

senha_label = tk.Label(text="Senha:", font=("Arial", fontSize))
senha = tk.Entry(window, show='*', font=("Arial", fontSize), width=45)

selectedExcel = tk.Entry(window, width=60)
buttonExcel = tk.Button(text='...', command=select_file_xlsx, width=5)
selectedExcelLabel = tk.Label(text='Excel com destinatários:')

columnNameLabel = tk.Label(text="Nome da coluna de destinatários:")
columnName = tk.Entry(window, font=("Arial", fontSize))


docxFile = tk.Entry(window, width=60)
buttonDocx = tk.Button(text='...', command=select_file_docx, width=5)
docxFileLabel = tk.Label(text='Selecionar word para o corpo do email:')

anexoFile = tk.Entry(window, width=60)
buttonAnexo = tk.Button(text='...', command=select_files, width=5)
anexoFileLabel = tk.Label(text='Selecionar Arquivos para realizar envio:')

startButton = tk.Button(text="Começar", width=10, height=3, command=PegarDados)

# _Screen draw_

email_label.grid(row=0, sticky=tk.W, pady=10, padx=5)
email.grid(row=1, sticky=tk.W, padx=5)

senha_label.grid(row=2, sticky=tk.W, pady=10, padx=5)
senha.grid(row=3, sticky=tk.W, padx=5)

selectedExcelLabel.grid(row=4, sticky=tk.W, pady=10)
selectedExcel.grid(row=5, sticky=tk.W, padx=5)
buttonExcel.grid(row=5, sticky=tk.W, column=1, padx=5)

columnNameLabel.grid(row=4, column=2)
columnName.grid(row=5, column=2)

docxFileLabel.grid(row=6, sticky=tk.W, pady=10)
docxFile.grid(row=7, sticky=tk.W, padx=5)
buttonDocx.grid(row=7, sticky=tk.W, column=1, padx=5)

anexoFileLabel.grid(row=8, sticky=tk.W, pady=10)
anexoFile.grid(row=9, sticky=tk.W, padx=5)
buttonAnexo.grid(row=9, sticky=tk.W, column=1, padx=5)

startButton.grid(row=10, sticky=tk.W, padx=5, pady=10)

window.mainloop()