# calculadora_2_grau_concavidade


# calculadora que, além de resolver equações de 2º grau, também calcula o ponto de máxima ou mínima (vértice da parábola) e a área da concavidade sob o eixo x.


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

# Função para calcular o vértice da parábola (ponto de máxima ou mínima)
def calcular_vertice(a, b, c):
    xv = -b / (2*a)
    yv = a * xv**2 + b * xv + c
    return xv, yv

# Função para calcular a área da concavidade sob o eixo x
def calcular_area(a, b, c):
    x1, x2 = calcular_raizes(a, b, c)
    if x1 is None or x2 is None:
        return None
    area = (a/3) * (x2**3 - x1**3) + (b/2) * (x2**2 - x1**2) + c * (x2 - x1)
    return abs(area)

# Função para obter os coeficientes e calcular os resultados
def resolver_equacao():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")
            return
        x1, x2 = calcular_raizes(a, b, c)
        xv, yv = calcular_vertice(a, b, c)
        area = calcular_area(a, b, c)
        
        resultado = ""
        if x1 is None and x2 is None:
            resultado += "Não há raízes reais.\n"
        elif x2 is None:
            resultado += f"Raiz única: x = {x1:.2f}\n"
        else:
            resultado += f"Raízes: x1 = {x1:.2f}, x2 = {x2:.2f}\n"
        
        resultado += f"Vértice: ({xv:.2f}, {yv:.2f})\n"
        
        if area is not None:
            resultado += f"Área da concavidade sob o eixo x: {area:.2f}\n"
        else:
            resultado += "Não é possível calcular a área da concavidade.\n"
        
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Equações de 2º Grau")
root.geometry("600x400")  # Aumenta o tamanho da janela

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