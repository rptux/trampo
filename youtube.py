# youtube




import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

# Função para fazer o download do vídeo
def baixar_video():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo do YouTube.")
        return
    
    # Permitir que o usuário escolha o diretório de destino
    pasta_destino = filedialog.askdirectory()
    if not pasta_destino:
        messagebox.showerror("Erro", "Por favor, selecione um diretório de destino.")
        return
    
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeos do YouTube")
root.geometry("500x200")

tk.Label(root, text="Link do vídeo do YouTube:").pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=10)

tk.Button(root, text="Baixar Vídeo", command=baixar_video).pack(pady=10)

root.mainloop()