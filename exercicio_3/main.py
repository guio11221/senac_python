import tkinter as tk
from tkinter import messagebox

# Função para validar campos
def validar_campo(nome, endereco, idade):
    if not nome or not endereco or not idade:
        messagebox.showinfo("Campos Vazios", "Por favor, preencha todos os campos.")
        return False
    if not idade.isdigit():
        messagebox.showinfo("Idade Inválida", "Por favor, insira uma idade válida.")
        return False
    return True

# Função chamada ao clicar no botão
def on_submit():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    idade = idade_entry.get()

    # Validando os campos
    if validar_campo(nome, endereco, idade):
        messagebox.showwarning("Aviso", f"Seja bem-vindo {nome}, \nSeu endereço é {endereco} \nE a idade é: {idade}")
    else:
        messagebox.showinfo("Erro", "Por favor, corrija os erros e tente novamente.")

# Configurações da Janela
windows = tk.Tk()
windows.title("Formulário Simples")
windows.geometry('400x300')

# Cor de fundo da janela
windows.configure(bg="#525252") 

# Nome completo
tk.Label(windows, text="Nome completo:", bg="#d3d3d3").pack(pady=5)
nome_entry = tk.Entry(windows, width=40, bg="#a3a1aa", fg="white", font="Times", borderwidth=2)
nome_entry.pack()

# Endereço
tk.Label(windows, text="Endereço completo:", bg="#d3d3d3").pack(pady=5)
endereco_entry = tk.Entry(windows, width=40,  bg="#a3a1aa", fg="white", font="Times", borderwidth=2)
endereco_entry.pack()

# Idade
tk.Label(windows, text="Idade:", bg="#d3d3d3").pack(pady=5)
idade_entry = tk.Entry(windows, width=40, bg="#a3a1aa", fg="white", font="Times", borderwidth=2)
idade_entry.pack()

# Botão de enviar
submit_button = tk.Button(windows, text="Enviar", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=20)

# Inicia o loop da janela
windows.mainloop()
