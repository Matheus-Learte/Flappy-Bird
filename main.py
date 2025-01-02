import pygame #Biblioteca para produzir jogos no Python
import config #Configurações setadas no config.py
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
from objects.background import Background #Arquivo que renderiza o background
from objects.floor import Floor
from objects.column import Column

#Inicia o pygame
pygame.init()


screen=pygame.display.set_mode((config.Screen_width, config.Screen_height)) #Cria uma janela e seta seu tamanho
clock=pygame.time.Clock() #Cria o objeto Clock para controlar a taxa de atualização
column_event=pygame.USEREVENT
running=True

assets.load_sprites() #Carrega os sprites

sprites=pygame.sprite.LayeredUpdates() #Cria uma classe que serve para gerenciar os sprites e controla a ordem de camadas

Background(0, sprites) #Adiciona o "background" ao grupo de sprites e setando o canto superior esquerdo do sprite no canto superior esquerdo 
Background(1, sprites) #Adiciona o "background" ao grupo de sprites e setando o canto superior esquerdo do sprite no canto superior direito
Floor(0, sprites)
Floor(1, sprites)

pygame.time.set_timer(column_event, 1500)

#Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==column_event:
            Column(sprites)

    screen.fill("black") #Preenche a tela de preto
    sprites.draw(screen) #Coloca o sprite "background" na tela
    sprites.update()

    pygame.display.flip() #Atualiza a tela
    clock.tick(config.FPS) #Controla o FPS para se manter a 60 quadros

pygame.quit() #Fecha o pygame e termina o programa