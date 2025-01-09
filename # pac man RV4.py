# pac man RV4
#corrigir os problemas com os pontos coletados não desaparecendo, o Pac-Man saindo 
# do labirinto e o erro de índice fora do alcance. Vamos fazer algumas melhorias:

#Limitar a movimentação do Pac-Man para dentro dos limites do labirinto.

#Corrigir a remoção dos pontos coletados.

#Adicionar verificação para evitar que o Pac-Man saia do 
# labirinto e cause um erro de índice fora do alcance.


import pygame
import sys
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 560, 620
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pac-Man')

# Configurações das cores
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Configurações do Pac-Man
largura_pacman, altura_pacman = 20, 20
posicao_inicial_pacman = [280, 310]
velocidade_pacman = 5
direcao_pacman = 'STOP'

# Configurações do Fantasma
largura_fantasma, altura_fantasma = 20, 20
posicao_inicial_fantasmas = [
    [140, 160],
    [420, 160],
    [140, 460],
    [420, 460]
]
direcoes_fantasmas = ['UP', 'DOWN', 'LEFT', 'RIGHT']
velocidade_fantasma = 3

# Labirinto simples
labirinto = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "          ########          ",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#....#................#....#",
    "####.##.##.########.##.##.##",
    "####.##.##.########.##.##.##",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Convertendo o labirinto para uma lista mutável para remover pontos
labirinto_lista = [list(linha) for linha in labirinto]

# Função para desenhar o labirinto
def desenhar_labirinto(tela):
    for y, linha in enumerate(labirinto_lista):
        for x, caractere in enumerate(linha):
            if caractere == '#':
                pygame.draw.rect(tela, AZUL, (x * 20, y * 20, 20, 20))

# Função para desenhar o Pac-Man
def desenhar_pacman(tela, posicao):
    pygame.draw.circle(tela, AMARELO, (posicao[0] + 10, posicao[1] + 10), largura_pacman // 2)

# Função para desenhar os fantasmas
def desenhar_fantasmas(tela, posicoes):
    for pos in posicoes:
        pygame.draw.rect(tela, VERMELHO, (pos[0], pos[1], largura_fantasma, altura_fantasma))

# Função para desenhar pontos
def desenhar_pontos(tela):
    for y, linha in enumerate(labirinto_lista):
        for x, caractere in enumerate(linha):
            if caractere == '.':
                pygame.draw.circle(tela, BRANCO, (x * 20 + 10, y * 20 + 10), 3)

# Função para mover o Pac-Man
def mover_pacman(pos, direcao):
    nova_pos = pos[:]
    if direcao == 'UP':
        nova_pos[1] -= velocidade_pacman
    elif direcao == 'DOWN':
        nova_pos[1] += velocidade_pacman
    elif direcao == 'LEFT':
        nova_pos[0] -= velocidade_pacman
    elif direcao == 'RIGHT':
        nova_pos[0] += velocidade_pacman

    # Limitar a movimentação aos limites do labirinto
    x, y = nova_pos[0] // 20, nova_pos[1] // 20
    if 0 <= y < len(labirinto_lista) and 0 <= x < len(labirinto_lista[0]) and labirinto_lista[y][x] != '#':
        return nova_pos
    return pos

# Função para mover os fantasmas
def mover_fantasmas(posicoes, direcoes):
    for i, pos in enumerate(posicoes):
        if direcoes[i] == 'UP':
            pos[1] -= velocidade_fantasma
        elif direcoes[i] == 'DOWN':
            pos[1] += velocidade_fantasma
        elif direcoes[i] == 'LEFT':
            pos[0] -= velocidade_fantasma
        elif direcoes[i] == 'RIGHT':
            pos[0] += velocidade_fantasma
        x, y = pos[0] // 20, pos[1] // 20
        if labirinto_lista[y][x] == '#':
            direcoes[i] = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    return posicoes, direcoes

# Função principal
def main():
    global posicao_pacman, direcao_pacman, posicao_fantasmas, direcoes_fantasmas

    relogio = pygame.time.Clock()
    rodando = True
    vidas = 3
    pontos = 0
    posicao_pacman = posicao_inicial_pacman[:]
    posicao_fantasmas = [pos[:] for pos in posicao_inicial_fantasmas]

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            direcao_pacman = 'LEFT'
        if teclas[pygame.K_RIGHT]:
            direcao_pacman = 'RIGHT'
        if teclas[pygame.K_UP]:
            direcao_pacman = 'UP'
        if teclas[pygame.K_DOWN]:
            direcao_pacman = 'DOWN'

        posicao_pacman = mover_pacman(posicao_pacman, direcao_pacman)
        posicao_fantasmas, direcoes_fantasmas = mover_fantasmas(posicao_fantasmas, direcoes_fantasmas)

        # Verificação de colisão com pontos
        x, y = posicao_pacman[0] // 20, posicao_pacman[1] // 20
        if 0 <= y < len(labirinto_lista) and 0 <= x < len(labirinto_lista[0]):
            if labirinto_lista[y][x] == '.':
                labirinto_lista[y][x] = ' '
                pontos += 1
                if all('.' not in linha for linha in labirinto_lista):
                    print("Parabéns, você coletou todos os pontos e venceu os fantasmas!")
                    rodando = False

        # Verificação de colisão com fantasmas
        pacman_rect = pygame.Rect(posicao_pacman[0], posicao_pacman[1], largura_pacman, altura_pacman)
        colidiu = False
        for pos in posicao_fantasmas:
            fantasma_rect = pygame.Rect(pos[0], pos[1], largura_fantasma, altura_fantasma)
            if pacman_rect.colliderect(fantasma_rect):
                colidiu = True
                break

        if colidiu:
            vidas -= 1
            if vidas > 0:
                print(f"Você perdeu uma vida! Vidas restantes: {vidas}")
                posicao_pacman = posicao_inicial_pacman[:]
                posicao_fantasmas = [pos[:] for pos in posicao_inicial_fantasmas]
                direcao_pacman = 'STOP'
            else:
                print("Você foi pego por um fantasma! Fim de jogo.")
                rodando = False

        # Atualizando a tela
        tela.fill(PRETO)
        desenhar_labirinto(tela)
        desenhar_pacman(tela, posicao_pacman)
        desenhar_fantasmas(tela, posicao_fantasmas)
        desenhar_pontos(tela)

        # Exibindo pontuação e vidas
        fonte = pygame.font.Font(None, 36)
        texto_pontos = fonte.render(f"Pontos: {[_{{{CITATION{{{_1{](https://github.com/AlexCuenca20/AlexCuenca20.github.io/tree/f14fbf996edb8c6ac2aecae9ecd47f371ce929df/src%2FGame.js)[_{{{CITATION{{{_2{](https://github.com/ZavalniukAlexey/Zavalniuk_Alexey_/tree/a7d0512131cec42fa36ea2ab34629529aa2c459d/pacman_git%2Fgit%2FField.cpp)[_{{{CITATION{{{_3{](https://github.com/Carlos-Descalzi/pacman-bge/tree/e50f307143b0885e16a1c07aa07847078530fc25/levelmap.py)[_{{{CITATION{{{_4{](https://github.com/eguneys/OLDeguneys.github.io/tree/492fa26fff053cfe6f6b8b39768aea20eaee3ac2/public%2Fgames%2Fpacman-unicode%2Fscripts%2F16aa69ed.main.js)[_{{{CITATION{{{_5{](https://github.com/nantoniazzi/game-pacman/tree/f428dda53724e996194fb00bbac8684cb745c845/src%2Fmain%2Fjava%2Fcom%2Fcodingame%2Fgame%2FWorld.java)[_{{{CITATION{{{_6{](https://github.com/pkrasam/sol-man/tree/e1120d30fbfce1e607de04621612eb13fadbde5f/src%2Fpacman%2Fmap.rs)