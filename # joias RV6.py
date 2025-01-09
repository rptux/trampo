# joias RV6
# suavizando o tom das joias
# lógica: cores iguais
# 1 forma 


import pygame
import random
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 480, 540  # Aumentei a altura da tela para exibir a pontuação e o nível
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo de Joias')

# Configurações das cores com tons mais suaves
CORES_JOIAS = [
    (255, 182, 193), # Rosa Claro
    (144, 238, 144), # Verde Claro
    (173, 216, 230), # Azul Claro
    (255, 255, 224), # Amarelo Claro
    (216, 191, 216), # Magenta Claro
    (224, 255, 255)  # Ciano Claro
]

# Configurações do tabuleiro
largura_joia, altura_joia = 60, 60
colunas, linhas = 8, 8
tabuleiro = [[random.choice(CORES_JOIAS) for _ in range(colunas)] for _ in range(linhas)]
selecionado = None
pontos = 0
nivel = 1

# Função para desenhar o tabuleiro de joias
def desenhar_tabuleiro(tela):
    for y in range(linhas):
        for x in range(colunas):
            pygame.draw.rect(tela, tabuleiro[y][x], (x * largura_joia, y * altura_joia + 60, largura_joia, altura_joia))
            pygame.draw.rect(tela, (255, 255, 255), (x * largura_joia, y * altura_joia + 60, largura_joia, altura_joia), 1)

# Função para trocar duas joias
def trocar_joias(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    tabuleiro[y1][x1], tabuleiro[y2][x2] = tabuleiro[y2][x2], tabuleiro[y1][x1]
    # som_troca.play()  # Removendo a linha que toca o som de troca

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
    global pontos, nivel
    pontos += len(combinacoes)
    # som_eliminacao.play()  # Removendo a linha que toca o som de eliminação
    for x, y in combinacoes:
        tabuleiro[y][x] = None

    # Descer as joias restantes
    for x in range(colunas):
        coluna = [tabuleiro[y][x] for y in range(linhas) if tabuleiro[y][x] is not None]
        falta_preencher = linhas - len(coluna)
        coluna = [random.choice(CORES_JOIAS) for _ in range(falta_preencher)] + coluna
        for y in range(linhas):
            tabuleiro[y][x] = coluna[y]

    # Aumentar o nível a cada 50 pontos
    if pontos >= nivel * 50:
        nivel += 1
        aumentar_dificuldade()

# Função para aumentar a dificuldade
def aumentar_dificuldade():
    global colunas, linhas, tabuleiro, largura_joia, altura_joia

    if colunas < 12:
        colunas += 1
        linhas += 1
        largura_joia = altura_tela // linhas
        altura_joia = largura_tela // colunas
        tabuleiro = [[random.choice(CORES_JOIAS) for _ in range(colunas)] for _ in range(linhas)]

# Função para exibir a pontuação e nível
def exibir_informacoes(tela, pontos, nivel):
    fonte = pygame.font.Font(None, 36)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    texto_nivel = fonte.render(f"Nível: {nivel}", True, (255, 255, 255))
    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_nivel, (200, 10))

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
                y = (y - 60) // altura_joia  # Ajuste para a nova posição do tabuleiro
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
        exibir_informacoes(tela, pontos, nivel)
        pygame.display.flip()
        relogio.tick(30)

if __name__ == '__main__':
    main()

