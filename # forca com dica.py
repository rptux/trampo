# forca com dica




import pygame
import random
from PyDictionary import PyDictionary

# Inicializando o Pygame
pygame.init()

# Inicializando o PyDictionary
dicionario = PyDictionary()

# Configurações da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Forca')

# Definindo cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Lista de palavras (pode ser expandida conforme necessário)
palavras = ["PYTHON", "DESENVOLVEDOR", "PROGRAMA", "ALGORITMO", "TECLADO"]

# Função para desenhar a forca
def desenhar_forca(tela, tentativas):
    pygame.draw.line(tela, PRETO, (50, 500), (200, 500), 10)
    pygame.draw.line(tela, PRETO, (125, 500), (125, 100), 10)
    pygame.draw.line(tela, PRETO, (125, 100), (300, 100), 10)
    pygame.draw.line(tela, PRETO, (300, 100), (300, 150), 10)
    if tentativas > 0:
        pygame.draw.circle(tela, PRETO, (300, 200), 50, 10)  # Cabeça
    if tentativas > 1:
        pygame.draw.line(tela, PRETO, (300, 250), (300, 400), 10)  # Corpo
    if tentativas > 2:
        pygame.draw.line(tela, PRETO, (300, 300), (250, 350), 10)  # Braço esquerdo
    if tentativas > 3:
        pygame.draw.line(tela, PRETO, (300, 300), (350, 350), 10)  # Braço direito
    if tentativas > 4:
        pygame.draw.line(tela, PRETO, (300, 400), (250, 500), 10)  # Perna esquerda
    if tentativas > 5:
        pygame.draw.line(tela, PRETO, (300, 400), (350, 500), 10)  # Perna direita

# Função para obter dica da palavra
def obter_dica(palavra):
    significado = dicionario.meaning(palavra)
    if significado:
        # Pega o primeiro significado disponível para a palavra
        dica = list(significado.values())[0][0]
    else:
        dica = "Sem definição disponível"
    return dica

# Função principal
def main():
    fonte = pygame.font.Font(None, 74)
    palavra = random.choice(palavras)
    dica = obter_dica(palavra)
    letras_adivinhadas = []
    tentativas = 0
    jogo_terminado = False

    rodando = True
    while rodando:
        tela.fill(BRANCO)
        desenhar_forca(tela, tentativas)

        # Exibir dica na parte superior
        fonte_dica = pygame.font.Font(None, 36)
        texto_dica = fonte_dica.render(f"Dica: {dica}", True, PRETO)
        tela.blit(texto_dica, (50, 20))

        # Exibir palavra oculta
        palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
        texto_palavra = fonte.render(palavra_oculta, True, PRETO)
        tela.blit(texto_palavra, (400, 300))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if not jogo_terminado:
                    letra = pygame.key.name(evento.key).upper()
                    if letra not in letras_adivinhadas:
                        letras_adivinhadas.append(letra)
                        if letra not in palavra:
                            tentativas += 1
                        if tentativas >= 6:
                            jogo_terminado = True
                        if set(palavra).issubset(set(letras_adivinhadas)):
                            jogo_terminado = True
                else:
                    if evento.key == pygame.K_r:
                        palavra = random.choice(palavras)
                        dica = obter_dica(palavra)
                        letras_adivinhadas = []
                        tentativas = 0
                        jogo_terminado = False

        if jogo_terminado:
            if set(palavra).issubset(set(letras_adivinhadas)):
                mensagem = "Você venceu! Pressione R para jogar novamente"
            else:
                mensagem = f"Você perdeu! A palavra era {palavra}. Pressione R para jogar novamente"
            texto_mensagem = fonte.render(mensagem, True, PRETO)
            tela.blit(texto_mensagem, (50, 400))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
