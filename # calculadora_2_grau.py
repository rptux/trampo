# calculadora_2_grau

#ajustar o tamanho da janela e usar a bliblioteca
# tkinter.font para ajustar dinamicamente o tamanho 
# da fonte conforme o tamanho da janela. 30/12/2024

import tkinter as tk
from tkinter import messagebox
import math

# Função para calcular as raízes da equação de 2º grau
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        x1 = -b / (2*a)
        return x1, None
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# Função para obter os coeficientes e calcular as raízes
def resolver_equacao():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")
            return
        x1, x2 = calcular_raizes(a, b, c)
        if x1 is None and x2 is None:
            label_resultado.config(text="Não há raízes reais.")
        elif x2 is None:
            label_resultado.config(text=f"Raiz única: x = {x1:.2f}")
        else:
            label_resultado.config(text=f"Raízes: x1 = {x1:.2f}, x2 = {x2:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Equações de 2º Grau (ax² + bx + c = 0)  Prof. Ricardo")
root.geometry("650x400")  # Aumenta o tamanho da janela

tk.Label(root, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calcular", command=resolver_equacao).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
#
#
# vamos comentar o código
#Passos para criar a calculadora:
#Configurar a interface gráfica com tkinter.
#Adicionar campos de entrada para os coeficientes da equação.
#Adicionar um botão para calcular as raízes.
#Exibir os resultados na interface.
#
#Explicação do Código
#Função calcular_raizes:

#Calcula as raízes da equação de 2º grau usando a fórmula de Bhaskara.
#Retorna as raízes x1 e x2. Se o delta for negativo, retorna None para ambas as raízes.
#Função resolver_equacao:

#Obtém os coeficientes a, b e c dos campos de entrada.
#Verifica se a é zero e exibe uma mensagem de erro, pois a não pode ser zero em uma equação de 2º grau.
#Calcula as raízes e atualiza o rótulo label_resultado com as raízes encontradas ou uma mensagem de erro.
#Configuração da Interface Gráfica:

#Cria a janela principal usando tk.Tk().
#Adiciona rótulos e campos de entrada para os coeficientes a, b e c.
#Adiciona um botão "Calcular" que chama a função resolver_equacao quando clicado.
#Adiciona um rótulo label_resultado para exibir o resultado.
#Ferramentas e Recursos
#Visual Studio Code: Um editor de código poderoso e gratuito que pode ser usado para escrever e executar scripts Python.
#Biblioteca Python tkinter: Para criar a interface gráfica.
#Implementação na Sala de Aula
#Introdução ao Python e tkinter: Ensinar os conceitos básicos de Python e como criar interfaces gráficas usando tkinter.
#Projetos Práticos: Dividir os alunos em grupos e atribuir projetos práticos que envolvam a criação de calculadoras científicas para resolver diferentes tipos de equações.
#Discussão e Análise: Analisar os resultados obtidos e discutir como os conceitos matemáticos foram aplicados e como a interface gráfica facilita a interação com o programa.
#Este projeto ajuda os alunos a entender melhor os conceitos matemáticos, habilidades de programação e como criar interfaces gráficas interativas.#