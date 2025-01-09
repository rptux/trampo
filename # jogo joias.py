# jogo joias
import pygame
import random
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 600, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo de Joias')

# Configurações das cores
CORES_JOIAS = [
    (255, 0, 0),   # Vermelho
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarelo
    (255, 0, 255), # Magenta
    (0, 255, 255)  # Ciano
]

# Configurações do tabuleiro
largura_joia, altura_joia = 40, 40
colunas, linhas = 8, 8
tabuleiro = [[random.choice(CORES_JOIAS) for _ in range(colunas)] for _ in range(linhas)]

# Função para desenhar o tabuleiro de joias
def desenhar_tabuleiro(tela):
    for y in range(linhas):
        for x in range(colunas):
            pygame.draw.rect(tela, tabuleiro[y][x], (x * largura_joia, y * altura_joia, largura_joia, altura_joia))

# Função principal
def main():
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizando a tela
        tela.fill((0, 0, 0))
        desenhar_tabuleiro(tela)
        pygame.display.flip()
        relogio.tick(30)

if __name__ == '__main__':
    main()
