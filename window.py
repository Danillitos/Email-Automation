import tkinter as tk
from tkinter import filedialog as fd
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

def select_file_xlsx():
    filename = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if filename != '':           
        selectedExcel.delete(0, tk.END)
        filename = filename.replace('/', '\\')
        selectedExcel.insert(0, filename)
    else: 
        pass

def PegarDados():
    emailValor = email.get()
    senhaValor = senha.get()
    sendSelectedExcel = selectedExcel.get()
    sendSelectedFile = selectedFile.get()

    backend.processar(emailValor, senhaValor, sendSelectedExcel, sendSelectedFile)


# _Functions_ ^


email_label = tk.Label(text="Email:", font=("Arial", fontSize))
email = tk.Entry(window, font=("Arial", fontSize))

senha_label = tk.Label(text="Senha:", font=("Arial", fontSize))
senha = tk.Entry(window, show='*', font=("Arial", fontSize))

selectedExcel = tk.Entry(window, width=60)
buttonExcel = tk.Button(text='...', command=select_file_xlsx, width=5)
selectedExcelLabel = tk.Label(text='Excel com emails:')

selectedFile = tk.Entry(window, width=60)
buttonFile = tk.Button(text='...', width=5)
selectedFileLabel = tk.Label(text='Selecionar Arquivo para realizar envios:')

startButton = tk.Button(text="Começar", width=10, height=3, command=PegarDados)

# _Screen draw_

email_label.grid(row=0, sticky=tk.W, pady=10, padx=5)
email.grid(row=1, sticky=tk.W, padx=5)

senha_label.grid(row=2, sticky=tk.W, pady=10, padx=5)
senha.grid(row=3, sticky=tk.W, padx=5)

selectedExcelLabel.grid(row=4, sticky=tk.W, pady=10)
selectedExcel.grid(row=5, sticky=tk.W, padx=5)
buttonExcel.grid(row=5, sticky=tk.W, column=1, padx=5)

selectedFileLabel.grid(row=6, sticky=tk.W, pady=10)
selectedFile.grid(row=7, sticky=tk.W, padx=5)
buttonFile.grid(row=7, sticky=tk.W, column=1, padx=5)

startButton.grid(row=8, sticky=tk.W, padx=5, pady=10)

window.mainloop()