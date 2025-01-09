# joias RV 15 


import pygame
import random
import sys
import pygame_gui

# Inicializando o Pygame
pygame.init()

# Obtendo as dimensões da tela do monitor
largura_tela = pygame.display.Info().current_w
altura_tela = pygame.display.Info().current_h

# Configurações da tela
tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE)
pygame.display.set_caption('Jogo de Joias')

# Inicializando o Pygame GUI Manager
gerenciador_gui = pygame_gui.UIManager((largura_tela, altura_tela))

# Configurações das cores com tons mais suaves
CORES_JOIAS = [
    (255, 182, 193), # Rosa Claro
    (144, 238, 144), # Verde Claro
    (173, 216, 230)  # Azul Claro
]

FORMAS_JOIAS = ['quadrado', 'triangulo']

# Configurações do tabuleiro
colunas, linhas = 8, 8
largura_joia, altura_joia = largura_tela // colunas, (altura_tela - 100) // linhas  # Deixar espaço para exibir a pontuação
tabuleiro = [[(random.choice(CORES_JOIAS), random.choice(FORMAS_JOIAS)) for _ in range(colunas)] for _ in range(linhas)]
selecionado = None
pontos = 0
nivel = 1

# Função para desenhar o tabuleiro de joias
def desenhar_tabuleiro(tela):
    for y in range(linhas):
        for x in range(colunas):
            cor, forma = tabuleiro[y][x]
            if forma == 'quadrado':
                pygame.draw.rect(tela, cor, (x * largura_joia, y * altura_joia + 60, largura_joia, altura_joia))
            elif forma == 'triangulo':
                pygame.draw.rect(tela, (255, 255, 255), (x * largura_joia, y * altura_joia + 60, largura_joia, altura_joia))  # Fundo branco para triângulo
                pontos_triangulo = [(x * largura_joia + largura_joia // 2, y * altura_joia + 60), 
                                    (x * largura_joia, y * altura_joia + 60 + altura_joia), 
                                    (x * largura_joia + largura_joia, y * altura_joia + 60 + altura_joia)]
                pygame.draw.polygon(tela, cor, pontos_triangulo)
            pygame.draw.rect(tela, (255, 255, 255), (x * largura_joia, y * altura_joia + 60, largura_joia, altura_joia), 1)

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
            if (tabuleiro[y][x][0] == tabuleiro[y][x + 1][0] == tabuleiro[y][x + 2][0]) and (tabuleiro[y][x][1] == tabuleiro[y][x + 1][1] == tabuleiro[y][x + 2][1]):
                combinacoes.update([(x, y), (x + 1, y), (x + 2, y)])

    # Verificar combinações verticais
    for x in range(colunas):
        for y in range(linhas - 2):
            if (tabuleiro[y][x][0] == tabuleiro[y + 1][x][0] == tabuleiro[y + 2][x][0]) and (tabuleiro[y][x][1] == tabuleiro[y + 1][x][1] == tabuleiro[y + 2][x][1]):
                combinacoes.update([(x, y), (x, y + 1), (x, y + 2)])

    return list(combinacoes)

# Função para eliminar combinações e descer joias
def eliminar_combinacoes(combinacoes):
    global pontos, nivel
    pontos += len(combinacoes) * 10  # 10 pontos por joia eliminada
    for x, y in combinacoes:
        tabuleiro[y][x] = (None, None)

    # Descer as joias restantes
    for x in range(colunas):
        coluna = [tabuleiro[y][x] for y in range(linhas) if tabuleiro[y][x] != (None, None)]
        falta_preencher = linhas - len(coluna)
        coluna = [(random.choice(CORES_JOIAS), random.choice(FORMAS_JOIAS)) for _ in range(falta_preencher)] + coluna
        for y in range(linhas):
            tabuleiro[y][x] = coluna[y]

    # Aumentar o nível a cada 200 pontos
    if pontos >= nivel * 200:
        nivel += 1
        pontos += 50  # Bônus de nível
        if nivel >= 5:
            aumentar_dificuldade()

# Função para aumentar a dificuldade
def aumentar_dificuldade():
    global colunas, linhas, tabuleiro, largura_joia, altura_joia

    if colunas < 12:
        colunas += 1
        linhas += 1
        largura_joia = largura_tela // colunas
        altura_joia = (altura_tela - 100) // linhas
        tabuleiro = [[(random.choice(CORES_JOIAS), random.choice(FORMAS_JOIAS)) for _ in range(colunas)] for _ in range(linhas)]

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

    # Criando botões de minimizar e fechar
    botao_minimizar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((largura_tela - 100, 10), (80, 30)), text='Minimizar', manager=gerenciador_gui)
    botao_fechar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((largura_tela - 200, 10), (80, 30)), text='Fechar', manager=gerenciador_gui)

    while rodando:
        tempo_delta = relogio.tick(30) / 1000.0  # Calcular o tempo delta para atualizar o gerenciador GUI

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.USEREVENT:
                if evento.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if evento.ui_element == botao_minimizar:
                        pygame.display.iconify()  # Minimizar janela
                    if evento.ui_element == botao_fechar:
                        rodando = False  # Fechar jogo
            if evento.type == pygame.MOUSEBUTTONDOWN:
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

            gerenciador_gui.process_events(evento)  # Processar eventos do GUI Manager

        # Atualizando a tela
        tela.fill((0, 0, 0))
        desenhar_tabuleiro(tela)
        exibir_informacoes(tela, pontos, nivel)

        gerenciador_gui.update(tempo_delta)  # Atualizar o gerenciador GUI
        gerenciador_gui.draw_ui(tela)  # Desenhar a interface GUI na tela

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
