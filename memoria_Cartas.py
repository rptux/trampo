# memoria Cartas
# Neste código, a variável score é 
# usada para armazenar a pontuação do j
# ogador. A função draw_board foi 
# modificada para exibir a pontuação 
# na parte inferior da tela. 
# A pontuação é incrementada em 10 
#  quando um par é encontrado e 
# decrementada em 1 ponto quando uma tentativa falha.

import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações do jogo
size = 4  # Tamanho do tabuleiro (4x4)
width, height = 400, 450  # Aumenta a altura para incluir o placar
card_size = width // size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Memória")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Funções do jogo
def create_board(size):
    symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:size//2] * 2
    random.shuffle(symbols)
    board = [symbols[i:i+int(size**0.5)] for i in range(0, size, int(size**0.5))]
    return board

def draw_board(board, revealed, score):
    for i, row in enumerate(board):
        for j, card in enumerate(row):
            rect = pygame.Rect(j * card_size, i * card_size, card_size, card_size)
            if revealed[i][j]:
                pygame.draw.rect(screen, WHITE, rect)
                font = pygame.font.Font(None, 74)
                text = font.render(card, True, BLACK)
                screen.blit(text, (j * card_size + 10, i * card_size + 10))
            else:
                pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
    
    # Desenha o placar
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(score_text, (10, height - 40))

def get_coordinates(pos):
    x, y = pos
    return y // card_size, x // card_size

def reset_game():
    global board, revealed, pairs_found, first_selection, score
    board = create_board(size*size)
    revealed = [[False]*size for _ in range(size)]
    pairs_found = 0
    first_selection = None
    score = 0

def main():
    global first_selection, pairs_found, score
    reset_game()

    running = True
    while running:
        screen.fill(BLACK)
        draw_board(board, revealed, score)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = get_coordinates(event.pos)
                if not revealed[x][y]:
                    revealed[x][y] = True
                    if first_selection is None:
                        first_selection = (x, y)
                    else:
                        if board[x][y] == board[first_selection[0]][first_selection[1]]:
                            pairs_found += 1
                            score += 10  # Incrementa a pontuação
                            if pairs_found == (size*size)//2:
                                pygame.time.wait(2000)
                                reset_game()
                        else:
                            pygame.time.wait(1000)
                            revealed[x][y] = False
                            revealed[first_selection[0]][first_selection[1]] = False
                            score -= 1  # Decrementa a pontuação
                        first_selection = None

    pygame.quit()

if __name__ == "__main__":
    main()