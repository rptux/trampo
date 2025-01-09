# tetrix rotação



import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 300, 600
tamanho_bloco = 30
largura_jogo, altura_jogo = largura_tela // tamanho_bloco, altura_tela // tamanho_bloco
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tetris')

# Definindo as cores
cores = [
    (0, 0, 0),    # Preto
    (255, 0, 0),  # Vermelho
    (0, 255, 0),  # Verde
    (0, 0, 255),  # Azul
    (255, 255, 0),# Amarelo
    (255, 165, 0),# Laranja
    (128, 0, 128) # Roxo
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

# Função para girar a peça
def rotacionar(peca):
    return [list(reversed(coluna)) for coluna in zip(*peca)]

# Função para verificar colisão
def colisao(tabuleiro, peca, offset):
    off_x, off_y = offset
    for y, linha in enumerate(peca):
        for x, bloco in enumerate(linha):
            if bloco:
                if (
                    x + off_x < 0 or
                    x + off_x >= largura_jogo or
                    y + off_y >= altura_jogo or
                    tabuleiro[y + off_y][x + off_x]
                ):
                    return True
    return False

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
                pygame.draw.rect(tela, cores[bloco], (off_x * tamanho_bloco + x * tamanho_bloco, off_y * tamanho_bloco + y * tamanho_bloco, tamanho_bloco, tamanho_bloco))

# Função para criar um novo tabuleiro
def novo_tabuleiro():
    tabuleiro = [[0 for _ in range(largura_jogo)] for _ in range(altura_jogo)]
    return tabuleiro

# Função para limpar linhas completas
def limpar_linhas(tabuleiro):
    linhas_completas = 0
    for i, linha in enumerate(tabuleiro):
        if 0 not in linha:
            del tabuleiro[i]
            tabuleiro.insert(0, [0 for _ in range(largura_jogo)])
            linhas_completas += 1
    return linhas_completas

# Função principal
def main():
    relogio = pygame.time.Clock()
    tabuleiro = novo_tabuleiro()
    peca = random.choice(formas)
    cor = random.randint(1, len(cores) - 1)
    posicao = [largura_jogo // 2, 0]
    queda_rapida = 0

    rodando = True
    while rodando:
        queda_rapida += 1
        if queda_rapida == 25:
            queda_rapida = 0
            posicao[1] += 1
            if colisao(tabuleiro, peca, posicao):
                posicao[1] -= 1
                for y, linha in enumerate(peca):
                    for x, bloco in enumerate(linha):
                        if bloco:
                            tabuleiro[y + posicao[1]][x + posicao[0]] = cor
                peca = random.choice(formas)
                cor = random.randint(1, len(cores) - 1)
                posicao = [largura_jogo // 2, 0]
                limpar_linhas(tabuleiro)
                if colisao(tabuleiro, peca, posicao):
                    rodando = False

        tela.fill((0, 0, 0))
        desenhar_grade(tela)
        desenhar_peca(tela, peca, posicao)

        for y, linha in enumerate(tabuleiro):
            for x, bloco in enumerate(linha):
                if bloco:
                    pygame.draw.rect(tela, cores[bloco], (x * tamanho_bloco, y * tamanho_bloco, tamanho_bloco, tamanho_bloco))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nova_posicao = [posicao[0] - 1, posicao[1]]
                    if not colisao(tabuleiro, peca, nova_posicao):
                        posicao = nova_posicao
                elif evento.key == pygame.K_RIGHT:
                    nova_posicao = [posicao[0] + 1, posicao[1]]
                    if not colisao(tabuleiro, peca, nova_posicao):
                        posicao = nova_posicao
                elif evento.key == pygame.K_DOWN:
                    nova_posicao = [posicao[0], posicao[1] + 1]
                    if not colisao(tabuleiro, peca, nova_posicao):
                        posicao = nova_posicao
                elif evento.key == pygame.K_UP:
                    nova_peca = rotacionar(peca)
                    if not colisao(tabuleiro, nova_peca, posicao):
                        peca = nova_peca

        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
