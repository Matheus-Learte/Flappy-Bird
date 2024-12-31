import pygame #Biblioteca para produzir jogos no Python
import config #Configurações setadas no config.py

#Inicia o pygame
pygame.init()


screen=pygame.display.set_mode((config.Screen_width, config.Screen_height)) #Cria uma janela e seta seu tamanho
clock=pygame.time.Clock() #Cria o objeto Clock para controlar a taxa de atualização
running=True

#Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill("black")

    pygame.display.flip() #Atualiza a tela
    clock.tick(config.FPS) #Controla o FPS para se manter a 60 quadros

pygame.quit() #Fecha o pygame e termina o programa