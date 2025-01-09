# joias RV2
#para garantir que as combinações sejam eliminadas 
# corretamente e que as joias desçam para preencher os espaços 
# em branco. Também vamos adicionar a lógica para que novas joias 
# sejam geradas no topo do tabuleiro para substituir as joias eliminadas.


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
largura_joia, altura_joia = 60, 60
colunas, linhas = 8, 8
tabuleiro = [[random.choice(CORES_JOIAS) for _ in range(colunas)] for _ in range(linhas)]
selecionado = None

# Função para desenhar o tabuleiro de joias
def desenhar_tabuleiro(tela):
    for y in range(linhas):
        for x in range(colunas):
            pygame.draw.rect(tela, tabuleiro[y][x], (x * largura_joia, y * altura_joia, largura_joia, altura_joia))
            pygame.draw.rect(tela, (255, 255, 255), (x * largura_joia, y * altura_joia, largura_joia, altura_joia), 1)

# Função para trocar duas joias
def trocar_joias(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    tabuleiro[y1][x1], tabuleiro[y2][x2] = tabuleiro[y2][x2], tabuleiro[y1][x1]

# Função para verificar combinações
def verificar_combinacoes():
    combinacoes = set()

    # Verificar combinações horizontais
    for y in range(linhas):
        for x in range(colunas - 2):
            if tabuleiro[y][x] == tabuleiro[y][x + 1] == tabuleiro[y][x + 2]:
                combinacoes.update([(x, y), (x + 1, y), (x + 2, y)])

    # Verificar combinações verticais
    for x in range(colunas):
        for y in range(linhas - 2):
            if tabuleiro[y][x] == tabuleiro[y + 1][x] == tabuleiro[y + 2][x]:
                combinacoes.update([(x, y), (x, y + 1), (x, y + 2)])

    return list(combinacoes)

# Função para eliminar combinações e descer joias
def eliminar_combinacoes(combinacoes):
    for x, y in combinacoes:
        tabuleiro[y][x] = None

    # Descer as joias restantes
    for x in range(colunas):
        coluna = [tabuleiro[y][x] for y in range(linhas) if tabuleiro[y][x] is not None]
        falta_preencher = linhas - len(coluna)
        coluna = [random.choice(CORES_JOIAS) for _ in range(falta_preencher)] + coluna
        for y in range(linhas):
            tabuleiro[y][x] = coluna[y]

# Função principal
def main():
    global selecionado

    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x //= largura_joia
                y //= altura_joia
                if selecionado:
                    trocar_joias(selecionado, (x, y))
                    combinacoes = verificar_combinacoes()
                    if combinacoes:
                        eliminar_combinacoes(combinacoes)
                    else:
                        trocar_joias(selecionado, (x, y))  # Troca de volta se não houver combinação
                    selecionado = None
                else:
                    selecionado = (x, y)

        # Atualizando a tela
        tela.fill((0, 0, 0))
        desenhar_tabuleiro(tela)
        pygame.display.flip()
        relogio.tick(30)

if __name__ == '__main__':
    main()
