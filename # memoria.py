# memoria

import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 600, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Memória')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Configurações do jogo
largura_cartao = 100
altura_cartao = 100
margem = 20

# Gerar um conjunto de pares de cartas
def gerar_pares():
    valores = list(range(1, 9)) * 2
    random.shuffle(valores)
    return valores

# Desenhar o tabuleiro de cartas
def desenhar_tabuleiro(tela, pares, cartas_viradas):
    tela.fill(BRANCO)
    for i in range(4):
        for j in range(4):
            x = j * (largura_cartao + margem) + margem
            y = i * (altura_cartao + margem) + margem
            indice = i * 4 + j
            if indice in cartas_viradas:
                pygame.draw.rect(tela, AZUL, (x, y, largura_cartao, altura_cartao))
                texto = fonte.render(str(pares[indice]), True, BRANCO)
                tela.blit(texto, (x + largura_cartao // 2 - texto.get_width() // 2, y + altura_cartao // 2 - texto.get_height() // 2))
            else:
                pygame.draw.rect(tela, VERDE, (x, y, largura_cartao, altura_cartao))
    pygame.display.flip()

# Função principal do jogo
def jogo_memoria():
    global fonte
    fonte = pygame.font.Font(None, 74)
    pares = gerar_pares()
    cartas_viradas = []
    par_atual = []
    rodando = True
    pares_encontrados = 0

    while rodando:
        desenhar_tabuleiro(tela, pares, cartas_viradas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                linha = y // (altura_cartao + margem)
                coluna = x // (largura_cartao + margem)
                indice = linha * 4 + coluna

                if indice not in cartas_viradas:
                    par_atual.append(indice)
                    cartas_viradas.append(indice)

                if len(par_atual) == 2:
                    if pares[par_atual[0]] == pares[par_atual[1]]:
                        pares_encontrados += 1
                        if pares_encontrados == 8:
                            print("Você venceu!")
                            pygame.time.wait(2000)
                            return True
                    else:
                        desenhar_tabuleiro(tela, pares, cartas_viradas)
                        pygame.time.wait(1000)
                        cartas_viradas.remove(par_atual[0])
                        cartas_viradas.remove(par_atual[1])
                    par_atual = []

        pygame.display.flip()

    return True

# Função principal
def main():
    while True:
        if not jogo_memoria():
            break

if __name__ == '__main__':
    main()
