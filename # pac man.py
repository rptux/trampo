# pac man
# rev 1, com colição no fantasma
# rev 2, adição de 3 vidas

#import pygame
#import sys
#import random

# Inicializando o Pygame
#pygame.init()

# Configurações da tela
#largura_tela, altura_tela = 560, 620
#tela = pygame.display.set_mode((largura_tela, altura_tela))
#pygame.display.set_caption('Pac-Man')

# Configurações das cores
#PRETO = (0, 0, 0)
#AZUL = (0, 0, 255)
#AMARELO = (255, 255, 0)
#BRANCO = (255, 255, 255)
#VERMELHO = (255, 0, 0)

# Configurações do Pac-Man
#largura_pacman, altura_pacman = 20, 20
#posicao_pacman = [280, 310]
#velocidade_pacman = 5
#direcao_pacman = 'STOP'

# Configurações do Fantasma
#largura_fantasma, altura_fantasma = 20, 20
#posicao_fantasmas = [
 #   [140, 160],
  #  [420, 160],
   # [140, 460],
    #[420, 460]
#]
#direcoes_fantasmas = ['UP', 'DOWN', 'LEFT', 'RIGHT']
#velocidade_fantasma = 3

# Labirinto simples
#labirinto = [
 #   "############################",
  #  "#............##............#",
#    "#.####.#####.##.#####.####.#",
#    "#.####.#####.##.#####.####.#",
#    "#.####.#####.##.#####.####.#",
#    "#..........................#",
#    "#.####.##.########.##.####.#",
#    "#.####.##.########.##.####.#",
#    "#......##....##....##......#",
#    "######.##### ## #####.######",
#    "######.##### ## #####.######",
#    "######.##          ##.######",
#    "######.## ######## ##.######",
#    "######.## ######## ##.######",
#    "          ########          ",
#    "######.## ######## ##.######",
#    "######.## ######## ##.######",
#    "######.##          ##.######",
#    "######.## ######## ##.######",
#    "######.## ######## ##.######",
#    "#............##............#",
#    "#.####.#####.##.#####.####.#",
#    "#.####.#####.##.#####.####.#",
#    "#....#................#....#",
#    "####.##.##.########.##.##.##",
#    "####.##.##.########.##.##.##",
#    "#......##....##....##......#",
#    "#.##########.##.##########.#",
#    "#.##########.##.##########.#",
#    "#..........................#",
#    "############################"
#]

# Função para desenhar o labirinto
#def desenhar_labirinto(tela):
 #   for y, linha in enumerate(labirinto):
  #      for x, caractere in enumerate(linha):
   #         if caractere == '#':
    #            pygame.draw.rect(tela, AZUL, (x * 20, y * 20, 20, 20))

# Função para desenhar o Pac-Man
#def desenhar_pacman(tela, posicao):
   # pygame.draw.circle(tela, AMARELO, (posicao[0] + 10, posicao[1] + 10), largura_pacman // 2)

# Função para desenhar os fantasmas
#def desenhar_fantasmas(tela, posicoes):
  #  for pos in posicoes:
    #    pygame.draw.rect(tela, VERMELHO, (pos[0], pos[1], largura_fantasma, altura_fantasma))

# Função para desenhar pontos
#def desenhar_pontos(tela):
 #   for y, linha in enumerate(labirinto):
  #      for x, caractere in enumerate(linha):
   #         if caractere == '.':
    #            pygame.draw.circle(tela, BRANCO, (x * 20 + 10, y * 20 + 10), 3)

# Função para mover o Pac-Man
#def mover_pacman(pos, direcao):
 #   if direcao == 'UP':
     #   pos[1] -= velocidade_pacman
  #  elif direcao == 'DOWN':
      #  pos[1] += velocidade_pacman
   # elif direcao == 'LEFT':
       # pos[0] -= velocidade_pacman
    #elif direcao == 'RIGHT':
        #pos[0] += velocidade_pacman
    #return pos

# Função para mover os fantasmas
#def mover_fantasmas(posicoes, direcoes):
 #   for i, pos in enumerate(posicoes):
  #      if direcoes[i] == 'UP':
   #         pos[1] -= velocidade_fantasma
    #    elif direcoes[i] == 'DOWN':
     #       pos[1] += velocidade_fantasma
      #  elif direcoes[i] == 'LEFT':
       #     pos[0] -= velocidade_fantasma
        #elif direcoes[i] == 'RIGHT':
         #   pos[0] += velocidade_fantasma
        #if pos[0] < 0 or pos[0] > largura_tela - largura_fantasma or pos[1] < 0 or pos[1] > altura_tela - altura_fantasma:
         #   direcoes[i] = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    #return posicoes, direcoes

# Função principal
#def main():
 #   global posicao_pacman, direcao_pacman, posicao_fantasmas, direcoes_fantasmas

  #  relogio = pygame.time.Clock()
   # rodando = True

    #while rodando:
     #   for evento in pygame.event.get():
      #      if evento.type == pygame.QUIT:
      #          pygame.quit()
      #          sys.exit()

      #  teclas = pygame.key.get_pressed()
       # if teclas[pygame.K_LEFT]:
        #    direcao_pacman = 'LEFT'
        #if teclas[pygame.K_RIGHT]:
         #   direcao_pacman = 'RIGHT'
        #if teclas[pygame.K_UP]:
         #   direcao_pacman = 'UP'
        #if teclas[pygame.K_DOWN]:
         #   direcao_pacman = 'DOWN'

        #posicao_pacman = mover_pacman(posicao_pacman, direcao_pacman)
        #posicao_fantasmas, direcoes_fantasmas = mover_fantasmas(posicao_fantasmas, direcoes_fantasmas)

        # Verificação de colisão com fantasmas
        #pacman_rect = pygame.Rect(posicao_pacman[0], posicao_pacman[1], largura_pacman, altura_pacman)
        #for pos in posicao_fantasmas:
         #   fantasma_rect = pygame.Rect(pos[0], pos[1], largura_fantasma, altura_fantasma)
          #  if pacman_rect.colliderect(fantasma_rect):
           #     print("Você foi pego por um fantasma! Fim de jogo.")
            #    rodando = False

        # Atualizando a tela
        #tela.fill(PRETO)
        #desenhar_labirinto(tela)
        #desenhar_pacman(tela, posicao_pacman)
        ##desenhar_fantasmas(tela, posicao_fantasmas)
        #desenhar_pontos(tela)
        #pygame.display.flip()
        #relogio.tick(30)

    #pygame.quit()

#if __name__ == '__main__':
 #   main()
#
## rev 3 acrescentando 3 vidas

