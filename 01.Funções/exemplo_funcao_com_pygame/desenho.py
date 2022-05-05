import pygame

def limpa(tela):
    tela.fill((255, 255, 255))  # Preenche com a cor branca

def desenha_bolinha(tela, posicao_x, posicao_y, largura_tela, altura_tela):
    # O sistema de coordenadas da tela tem a origem no canto superior esquerdo
    # e o eixo Y aumenta para baixo. Precisamos inverter isso:
    x_tela = posicao_x + 50
    y_tela = altura_tela - (posicao_y + 50)
    cor = (0, 0, 255)  # azul

    pygame.draw.circle(tela, cor, (x_tela, y_tela), 10)

def desenha_texto(tela, texto):
    fonte = pygame.font.SysFont(None, 18)
    imagem_do_texto = fonte.render(texto, True, (0, 0, 0))
    tela.blit(imagem_do_texto, (20, 20))
