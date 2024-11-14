import tkinter as tk
from tkinter import ttk
import calendar

def gerar_calendario():
    try:
        ano = int(entry_ano.get())
        calendario_texto = ""

        # Configurando o calendário para cada mês
        for mes in range(1, 13):
            calendario_texto += calendar.month_name[mes] + "\n"
            calendario_texto += "D  S  T  Q  Q  S  S\n"
            
            # Obter calendário do mês como uma lista de semanas
            mes_calendario = calendar.monthcalendar(ano, mes)
            for semana in mes_calendario:
                for dia in semana:
                    if dia == 0:
                        calendario_texto += "   "
                    else:
                        calendario_texto += f"{dia:2} "
                calendario_texto += "\n"
            calendario_texto += "\n"

        # Exibir calendário na caixa de texto
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, calendario_texto)
    except ValueError:
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, "Por favor, insira um ano válido.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Calendário")
root.geometry("600x700")
root.configure(bg="#e6f7ff")

# Título
titulo = tk.Label(root, text="Gerador de Calendário", font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#007acc")
titulo.pack(pady=10)

# Entrada do ano
frame_ano = tk.Frame(root, bg="#e6f7ff")
frame_ano.pack(pady=10)

label_ano = tk.Label(frame_ano, text="Digite o ano:", font=("Arial", 12), bg="#e6f7ff", fg="#333333")
label_ano.pack(side=tk.LEFT, padx=5)

entry_ano = tk.Entry(frame_ano, font=("Arial", 12), width=10)
entry_ano.pack(side=tk.LEFT)

# Botão para gerar o calendário
btn_gerar = tk.Button(root, text="Gerar Calendário", command=gerar_calendario, font=("Arial", 12, "bold"), bg="#007acc", fg="white", padx=10, pady=5)
btn_gerar.pack(pady=10)

# Caixa de texto para exibir o calendário
text_calendario = tk.Text(root, wrap=tk.NONE, font=("Courier New", 10), bg="white", fg="black", height=30, width=60)
text_calendario.pack(pady=10)

# Barra de rolagem para a caixa de texto
scrollbar = tk.Scrollbar(root, orient="vertical", command=text_calendario.yview)
scrollbar.pack(side="right", fill="y")
text_calendario.config(yscrollcommand=scrollbar.set)

# Iniciar o loop principal da interface gráfica
root.mainloop()
