# Importa e inicia pacotes
import fisica
import desenho
import pygame

pygame.init()

# Cria tela principal
LARGURA_METROS = 10
LARGURA = 500  # em pixels
ALTURA = 400  # em pixels
ESCALA = LARGURA / LARGURA_METROS
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Exemplo de funções')

# Inicializa variáveis
executando = True
simular = False
posicao_inicial_x = 0
posicao_inicial_y = 0
velocidade_inicial_x = 4  # m/s
velocidade_inicial_y = 7  # m/s
t0 = 0

# Loop principal
while executando:
    # Trata eventos
    for evento in pygame.event.get():
        # Verifica consequências
        if evento.type == pygame.QUIT:  # Clicou no X para fechar a janela
            executando = False
        if evento.type == pygame.MOUSEBUTTONUP:
            simular = True
            t0 = pygame.time.get_ticks()  # Reseta o tempo da simulação

    if simular:
        # Calcula tempo decorrido em segundos
        tempo_decorrido = (pygame.time.get_ticks() - t0) / 1000

        # Calcula nova posição
        posicao_x_metros = fisica.calcula_posicao(posicao_inicial_x, velocidade_inicial_x, 0, tempo_decorrido)
        posicao_y_metros = fisica.calcula_posicao(posicao_inicial_y, velocidade_inicial_y, -9.8, tempo_decorrido)
        # Converte para pixels
        posicao_x_pixels = int(posicao_x_metros * ESCALA)
        posicao_y_pixels = int(posicao_y_metros * ESCALA)

        # Desenha a nova tela
        desenho.limpa(tela)
        desenho.desenha_bolinha(tela, posicao_x_pixels, posicao_y_pixels, LARGURA, ALTURA)
    else:
        # Desenha a nova tela
        desenho.limpa(tela)
        desenho.desenha_bolinha(tela, 0, 0, LARGURA, ALTURA)
    desenho.desenha_texto(tela, 'Clique com o mouse para (re)iniciar a simulação')

    # Mostra a nova tela para o usuário
    pygame.display.update()

# Finalização
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

