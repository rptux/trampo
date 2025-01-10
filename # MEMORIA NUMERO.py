# MEMORIA NUMERO


import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações do jogo
size = 4  # Tamanho do tabuleiro (4x4)
width, height = 400, 500  # Aumenta a altura para incluir o placar fora do tabuleiro
card_size = width // size
score_height = 100  # Altura da área do placar
screen = pygame.display.set_mode((width, height + score_height))
pygame.display.set_caption("Jogo de Memória com Números")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonte
font = pygame.font.Font(None, 48)
score_font = pygame.font.Font(None, 36)

# Função para criar o tabuleiro com números
def create_board(size):
    numbers = list(range(1, (size * size // 2) + 1)) * 2
    random.shuffle(numbers)
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(numbers.pop())
        board.append(row)
    return board

# Função para desenhar o tabuleiro
def draw_board(board, revealed):
    for i in range(size):
        for j in range(size):
            x = j * card_size
            y = i * card_size + score_height
            if revealed[i][j]:
                pygame.draw.rect(screen, WHITE, (x, y, card_size, card_size))
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (x + card_size // 2 - text.get_width() // 2, y + card_size // 2 - text.get_height() // 2))
            else:
                pygame.draw.rect(screen, GRAY, (x, y, card_size, card_size))
            pygame.draw.rect(screen, BLACK, (x, y, card_size, card_size), 2)

# Função para desenhar o placar
def draw_score(score, high_score):
    score_text = score_font.render(f"Pontuação: {score}", True, WHITE)
    high_score_text = score_font.render(f"Maior Pontuação: {high_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))

# Função principal do jogo
def main():
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    first_selection = None
    score = 0
    high_score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y > score_height:
                    row = (y - score_height) // card_size
                    col = x // card_size
                    if not revealed[row][col]:
                        revealed[row][col] = True
                        if first_selection is None:
                            first_selection = (row, col)
                        else:
                            r1, c1 = first_selection
                            if board[row][col] == board[r1][c1]:
                                score += 10
                                if score > high_score:
                                    high_score = score
                            else:
                                pygame.time.wait(500)
                                revealed[row][col] = False
                                revealed[r1][c1] = False
                                score -= 5
                            first_selection = None

        screen.fill(BLACK)
        draw_score(score, high_score)
        draw_board(board, revealed)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()