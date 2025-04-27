import tkinter as tk

# _Libaries_ ^^

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

# _Window Config_ ^^

email_label = tk.Label(text="Email:", font=("Arial", 12))
email = tk.Entry(window, font=("Arial", 12))

senha_label = tk.Label(text="Senha:", font=("Arial", 12))
senha = tk.Entry(window, show='*', font=("Arial", 12))

# _Screen draw_

email_label.pack(pady=5)
email.pack(pady=8)

senha_label.pack(pady=5)
senha.pack(pady=8)

window.mainloop()