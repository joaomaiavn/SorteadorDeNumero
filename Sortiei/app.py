import tkinter as tk #importa a interface gráfica
from tkinter import messagebox #importa caixas de mensagens (pop-up)
import random #usado para gerar numeros ou seleções aleatórias

# Variáveis globais
participantes = []
sorteados = []
numeros_disponiveis = []
numeros_sorteados = []

# Função para atualizar a lista de participantes
def atualizar_participantes():
    global participantes, sorteados
    participantes = participantes_entry.get().split(',')
    participantes = [p.strip() for p in participantes if p.strip()]  # Remove espaços extras
    sorteados = []  # Reinicia a lista de sorteados

# Função para sortear individualmente um nome de cada vez
def sortear_individual():
    global sorteados

    if not participantes:  # Atualiza participantes apenas se a lista estiver vazia
        atualizar_participantes()

    if len(participantes) == 0:
        messagebox.showerror("Erro", "Por favor, insira pelo menos um nome válido!")
        return

    if len(sorteados) == len(participantes):
        messagebox.showinfo("Informação", "Todos os participantes já foram sorteados! O sorteio será reiniciado.")
        sorteados = []  # Reinicia o sorteio

    # Seleciona um participante que ainda não foi sorteado
    nome_sorteado = random.choice([p for p in participantes if p not in sorteados])
    sorteados.append(nome_sorteado)

    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, f"Sorteado: {nome_sorteado}\n")

# Função para sortear números sem repetição
# Função para sortear números sem repetição
def sortear_numeros():
    global numeros_disponiveis, numeros_sorteados

    try:
        total_numeros = int(numeros_entry.get())

        # Inicializa a lista de números disponíveis se for a primeira vez ou se todos foram sorteados
        if not numeros_disponiveis:
            numeros_disponiveis = list(range(1, total_numeros + 1))
            numeros_sorteados = []

        if len(numeros_disponiveis) == 0:
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, "Todos os números já foram sorteados!\n")
            messagebox.showinfo("Informação", "Todos os números já foram sorteados! Reinicie o sorteio se desejar continuar.")
            return

        # Sorteia um número aleatório
        numero_sorteado = random.choice(numeros_disponiveis)
        numeros_sorteados.append(numero_sorteado)
        numeros_disponiveis.remove(numero_sorteado)

        # Exibe o número sorteado
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Número sorteado: {numero_sorteado}\n")

        # Verifica se todos os números foram sorteados após o sorteio
        if len(numeros_disponiveis) == 0:
            resultado_text.insert(tk.END, "Todos os números já foram sorteados!\n")
            messagebox.showinfo("Informação", "Todos os números já foram sorteados!")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")

# Função para dividir participantes em equipes
def sortear_equipes():
    try:
        team_size = int(equipe_entry.get())
        participants = participantes_entry.get().split(',')
        participants = [p.strip() for p in participants if p.strip()]  # Remove espaços extras

        if len(participants) % team_size != 0:
            messagebox.showerror("Erro", "O número de participantes deve ser divisível pelo número de pessoas por equipe!")
            return

        random.shuffle(participants)
        equipes = [participants[i:i + team_size] for i in range(0, len(participants), team_size)]

        resultado_text.delete(1.0, tk.END)  # Limpa o resultado anterior
        for i, equipe in enumerate(equipes, 1):
            resultado_text.insert(tk.END, f"Equipe {i}: {', '.join(equipe)}\n")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de pessoas por equipe!")

# Função para exibir o campo correto de acordo com a escolha do usuário
def mostrar_opcao(opcao):
    esconder_todos_campos()
    atualizar_participantes()  # Atualiza os participantes ao mudar de opção

    if opcao == 'time':
        equipe_label.pack(pady=10)
        equipe_entry.pack(pady=10)
        sortear_time_btn.pack(pady=10)
    elif opcao == 'individual':
        sortear_individual_btn.pack(pady=10)
    elif opcao == 'numeros':
        numeros_label.pack(pady=10)
        numeros_entry.pack(pady=10)
        sortear_numeros_btn.pack(pady=10)

# Função para esconder todos os campos antes de exibir o campo correto
def esconder_todos_campos():
    equipe_label.pack_forget()
    equipe_entry.pack_forget()
    sortear_time_btn.pack_forget()
    sortear_individual_btn.pack_forget()
    numeros_label.pack_forget()
    numeros_entry.pack_forget()
    sortear_numeros_btn.pack_forget()

# Cria a janela principal
janela = tk.Tk()
janela.title("Sortiei")
janela.geometry("800x600")

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
opcao_numeros_btn = tk.Button(janela, text="Sorteio de Números", command=lambda: mostrar_opcao('numeros'))
opcao_numeros_btn.pack(pady=5)

# Entrada para o número de equipes
equipe_label = tk.Label(janela, text="Número de pessoas por equipe:")
equipe_entry = tk.Entry(janela)

# Botão para realizar o sorteio de times
sortear_time_btn = tk.Button(janela, text="Sortear Equipes", command=sortear_equipes)

# Botão para realizar o sorteio individual
sortear_individual_btn = tk.Button(janela, text="Sortear Participante", command=sortear_individual)

# Entrada para o sorteio de números
numeros_label = tk.Label(janela, text="Digite a quantidade total de números:")
numeros_entry = tk.Entry(janela)

# Botão para realizar o sorteio de números
sortear_numeros_btn = tk.Button(janela, text="Sortear Número", command=sortear_numeros)

# Área de texto para exibir os resultados
resultado_text = tk.Text(janela, height=10, width=50)
resultado_text.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
