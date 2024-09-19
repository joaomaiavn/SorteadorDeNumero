import tkinter as tk
from tkinter import messagebox
import random

# Lista para armazenar os participantes sorteados
participantes = []
sorteados = []

# Função para dividir participantes em equipes
def sortear_equipes():
    try:
        team_size = int(equipe_entry.get())
        participants = participantes_entry.get().split(',')
        participants = [p.strip() for p in participants if p.strip()]  # Remove espaços extras

        if len(participants) % team_size != 0:
            messagebox.showerror("Erro", "O número de participantes deve ser divisível pelo número de equipes!")
            return

        random.shuffle(participants)
        equipes = [participants[i:i + team_size] for i in range(0, len(participants), team_size)]
        
        resultado_text.delete(1.0, tk.END)  # Limpa o resultado anterior
        for i, equipe in enumerate(equipes, 1):
            resultado_text.insert(tk.END, f"Equipe {i}: {', '.join(equipe)}\n")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de equipes!")

# Função para sortear individualmente um nome de cada vez
def sortear_individual():
    global participantes, sorteados
    
    if not participantes:
        participantes = participantes_entry.get().split(',')
        participantes = [p.strip() for p in participantes if p.strip()]  # Remove espaços extras
        sorteados = []  # Reinicia a lista de sorteados

    if len(participantes) == 0:
        messagebox.showerror("Erro", "Por favor, insira pelo menos um nome válido!")
        return
    
    if len(participantes) == len(sorteados):
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Todos os participantes foram sorteados!")
        return

    nome_sorteado = random.choice([p for p in participantes if p not in sorteados])
    sorteados.append(nome_sorteado)
    
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, f"Sorteado: {nome_sorteado}\n")

# Função para exibir o campo correto de acordo com a escolha do usuário
def mostrar_opcao(opcao):
    if opcao == 'time':
        equipe_label.pack(pady=10)
        equipe_entry.pack(pady=10)
        sortear_time_btn.pack(pady=10)
        sortear_individual_btn.pack_forget()  # Oculta o botão de sorteio individual
        continuar_btn.pack_forget()
    elif opcao == 'individual':
        equipe_label.pack_forget()  # Oculta o campo de equipe
        equipe_entry.pack_forget()
        sortear_time_btn.pack_forget()  # Oculta o botão de times
        sortear_individual_btn.pack(pady=10)
        continuar_btn.pack(pady=10)

# Cria a janela principal
janela = tk.Tk()
janela.title("Sortiei")
janela.geometry("1920x1080")

# Título
titulo = tk.Label(janela, text="Sortiei", font=("Arial", 16))
titulo.pack(pady=10)

# Entrada para os nomes dos participantes
participantes_label = tk.Label(janela, text="Nomes dos Participantes (separados por vírgula):")
participantes_label.pack(pady=10)
participantes_entry = tk.Entry(janela, width=50)
participantes_entry.pack(pady=10)

# Botões para escolher a opção de sorteio
opcao_label = tk.Label(janela, text="Escolha uma opção:")
opcao_label.pack(pady=10)
opcao_time_btn = tk.Button(janela, text="Escolha de Time", command=lambda: mostrar_opcao('time'))
opcao_time_btn.pack(pady=5)
opcao_individual_btn = tk.Button(janela, text="Sorteio Individual", command=lambda: mostrar_opcao('individual'))
opcao_individual_btn.pack(pady=5)

# Entrada para o número de equipes
equipe_label = tk.Label(janela, text="Número de pessoas por equipe:")
equipe_entry = tk.Entry(janela)

# Botão para realizar o sorteio de times
sortear_time_btn = tk.Button(janela, text="Sortear Equipes", command=sortear_equipes)

# Botão para realizar o sorteio individual
sortear_individual_btn = tk.Button(janela, text="Iniciar Sorteio Individual", command=sortear_individual)

# Botão para continuar o sorteio individual (próximo nome)
continuar_btn = tk.Button(janela, text="Continuar", command=sortear_individual)

# Área de texto para exibir os resultados
resultado_text = tk.Text(janela, height=10, width=50)
resultado_text.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
