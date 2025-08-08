import tkinter as tk;
from tkinter import messagebox

def mostrar_alerta():
    nome = entrada.get()
    
    if nome:
        messagebox.showinfo("Olá!", f"Bem vindo, {nome}")
    else:
        messagebox.showwarning('Atenção', "Digite um nome!")

janela = tk.Tk()
janela.title("Exemplo com Entry e Alerta")
janela.geometry("300x150")

tk.Label(janela, text="Seu nome:").pack()
entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Mostrar Alerta", command=mostrar_alerta).pack()
janela.mainloop()