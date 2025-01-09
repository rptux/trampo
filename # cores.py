# cores 


import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Exemplo de Cores no Pygame')

# Cores
CORES_JOIAS = [
    (255, 182, 193), (144, 238, 144), (173, 216, 230),
    (255, 228, 181), (240, 230, 140), (224, 255, 255), (221, 160, 221)
]

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
CINZA = (128, 128, 128)
LARANJA = (255, 165, 0)
AMARELO = (255, 255, 0)
VIOLETA = (238, 130, 238)
MARROM = (165, 42, 42)

# Função principal
def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill(BRANCO)

        # Desenhar retângulos com cores suaves
        for idx, cor in enumerate(CORES_JOIAS):
            pygame.draw.rect(tela, cor, (50 + idx * 100, 50, 80, 80))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
