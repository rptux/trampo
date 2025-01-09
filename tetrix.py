#tetrix simples
import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 300, 600
tamanho_bloco = 30
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tetris')

# Definindo as cores
cores = [
    (0, 0, 0),  # Preto
    (255, 0, 0),  # Vermelho
    (0, 255, 0),  # Verde
    (0, 0, 255),  # Azul
    (255, 255, 0),  # Amarelo
    (255, 165, 0),  # Laranja
    (128, 0, 128),  # Roxo
]

# Definindo as formas das peças de Tetris
formas = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Função para desenhar a grade
def desenhar_grade(tela):
    for i in range(0, largura_tela, tamanho_bloco):
        pygame.draw.line(tela, (128, 128, 128), (i, 0), (i, altura_tela))
    for j in range(0, altura_tela, tamanho_bloco):
        pygame.draw.line(tela, (128, 128, 128), (0, j), (largura_tela, j))

# Função para desenhar peças
def desenhar_peca(tela, peca, offset):
    off_x, off_y = offset
    for y, linha in enumerate(peca):
        for x, bloco in enumerate(linha):
            if bloco:
                pygame.draw.rect(tela, cores[bloco], (off_x + x * tamanho_bloco, off_y + y * tamanho_bloco, tamanho_bloco, tamanho_bloco))

# Função principal
def main():
    relogio = pygame.time.Clock()
    peca = random.choice(formas)
    cor = random.randint(1, len(cores) - 1)
    posicao = [largura_tela // 2, 0]

    rodando = True
    while rodando:
        tela.fill((0, 0, 0))
        desenhar_grade(tela)
        desenhar_peca(tela, peca, posicao)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    posicao[0] -= tamanho_bloco
                elif evento.key == pygame.K_RIGHT:
                    posicao[0] += tamanho_bloco
                elif evento.key == pygame.K_DOWN:
                    posicao[1] += tamanho_bloco

        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
