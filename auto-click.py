import pyautogui
import tkinter as tk
from tkinter import messagebox
import threading
import time
import keyboard

# Função para realizar o auto-clique
def auto_click(interval):
    try:
        interval = float(interval) / 1000  # Converter de milissegundos para segundos

        while auto_clicking:  # A execução continua enquanto a flag for True
            pyautogui.click()  # Realiza o clique
            time.sleep(interval)  # Espera pelo intervalo

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o intervalo.")

# Função para iniciar o auto-clique em uma thread separada
def start_auto_click():
    global auto_clicking
    interval = interval_entry.get()
    
    if not interval:  # Verifica se o campo está vazio
        messagebox.showerror("Erro", "Por favor, insira um intervalo válido!")
        return
    
    auto_clicking = True  # Inicia o auto-clique
    threading.Thread(target=auto_click, args=(interval,)).start()
    start_button.config(state="disabled")  # Desativa o botão enquanto o auto-clique está ativo
    stop_button.config(state="normal")  # Habilita o botão de parar
    interval_entry.config(state="disabled")  # Desativa o campo de intervalo

# Função para parar o auto-clique
def stop_auto_click():
    global auto_clicking
    auto_clicking = False
    start_button.config(state="normal")  # Reativa o botão de iniciar
    stop_button.config(state="disabled")  # Desativa o botão de parar
    interval_entry.config(state="normal")  # Reativa o campo de intervalo

# Função para monitorar a tecla 'P' (com chamada periódica)
def monitor_keyboard():
    if keyboard.is_pressed('p'):  # Se a tecla 'P' for pressionada
        stop_auto_click()
    # Verifica novamente após 100ms
    root.after(100, monitor_keyboard)

# Criando a interface gráfica
root = tk.Tk()
root.title("Auto Clicker")

# Variável para controlar o estado do auto-clique
auto_clicking = False

# Configuração do layout
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

interval_label = tk.Label(frame, text="Intervalo (em milissegundos):")
interval_label.pack()

interval_entry = tk.Entry(frame)
interval_entry.pack()

start_button = tk.Button(frame, text="Iniciar Auto-Click", command=start_auto_click)
start_button.pack(pady=10)

stop_button = tk.Button(frame, text="Parar Auto-Click", command=stop_auto_click, state="disabled")
stop_button.pack()

# Inicia o monitoramento da tecla 'P' no loop principal
root.after(100, monitor_keyboard)  # Inicia a verificação periódica

# Inicia o loop da interface gráfica
root.mainloop()