# damas
# 30/12/24
# ricardo
# tamanho do tabuleiro 600x600


import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela = 600
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo de Damas')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (128, 128, 128)

# Configurações do tabuleiro
linhas = 8
colunas = 8
largura_celula = largura_tela // colunas
altura_celula = altura_tela // linhas

# Função para desenhar o tabuleiro
def desenhar_tabuleiro(tela):
    for linha in range(linhas):
        for coluna in range(colunas):
            if (linha + coluna) % 2 == 0:
                pygame.draw.rect(tela, BRANCO, (coluna * largura_celula, linha * altura_celula, largura_celula, altura_celula))
            else:
                pygame.draw.rect(tela, PRETO, (coluna * largura_celula, linha * altura_celula, largura_celula, altura_celula))

# Classe para representar uma peça
class Peca:
    def __init__(self, linha, coluna, cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self.rei = False

    def tornar_rei(self):
        self.rei = True

    def desenhar(self, tela):
        raio = largura_celula // 2 - 10
        pygame.draw.circle(tela, self.cor, (self.coluna * largura_celula + largura_celula // 2, self.linha * altura_celula + altura_celula // 2), raio)
        if self.rei:
            pygame.draw.circle(tela, VERMELHO, (self.coluna * largura_celula + largura_celula // 2, self.linha * altura_celula + altura_celula // 2), raio - 10)

# Inicializa as peças no tabuleiro
def inicializar_pecas():
    pecas = []
    for linha in range(linhas):
        fila_pecas = []
        for coluna in range(colunas):
            if linha < 3 and (linha + coluna) % 2 != 0:
                fila_pecas.append(Peca(linha, coluna, VERMELHO))
            elif linha > 4 and (linha + coluna) % 2 != 0:
                fila_pecas.append(Peca(linha, coluna, AZUL))
            else:
                fila_pecas.append(None)
        pecas.append(fila_pecas)
    return pecas

# Função para verificar se um movimento é válido
def movimento_valido(pecas, linha, coluna, nova_linha, nova_coluna):
    if nova_linha < 0 or nova_linha >= linhas or nova_coluna < 0 or nova_coluna >= colunas:
        return False
    if pecas[nova_linha][nova_coluna] is not None:
        return False
    if abs(nova_linha - linha) == 1 and abs(nova_coluna - coluna) == 1:
        return True
    if abs(nova_linha - linha) == 2 and abs(nova_coluna - coluna) == 2:
        meio_linha = (linha + nova_linha) // 2
        meio_coluna = (coluna + nova_coluna) // 2
        if pecas[meio_linha][meio_coluna] is not None and pecas[meio_linha][meio_coluna].cor != pecas[linha][coluna].cor:
            pecas[meio_linha][meio_coluna] = None
            return True
    return False

# Função principal
def main():
    pecas = inicializar_pecas()
    rodando = True
    peca_selecionada = None
    vez_azul = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                coluna = x // largura_celula
                linha = y // altura_celula

                if peca_selecionada:
                    if movimento_valido(pecas, peca_selecionada.linha, peca_selecionada.coluna, linha, coluna):
                        pecas[peca_selecionada.linha][peca_selecionada.coluna], pecas[linha][coluna] = None, pecas[peca_selecionada.linha][peca_selecionada.coluna]
                        pecas[linha][coluna].linha, pecas[linha][coluna].coluna = linha, coluna
                        if (linha == 0 and pecas[linha][coluna].cor == AZUL) or (linha == linhas - 1 and pecas[linha][coluna].cor == VERMELHO):
                            pecas[linha][coluna].tornar_rei()
                        vez_azul = not vez_azul
                    peca_selecionada = None
                else:
                    if pecas[linha][coluna] is not None and ((pecas[linha][coluna].cor == AZUL and vez_azul) or (pecas[linha][coluna].cor == VERMELHO and not vez_azul)):
                        peca_selecionada = pecas[linha][coluna]

        desenhar_tabuleiro(tela)
        for linha in pecas:
            for peca in linha:
                if peca:
                    peca.desenhar(tela)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
