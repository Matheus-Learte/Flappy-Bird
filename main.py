import pygame #Biblioteca para produzir jogos no Python
import config #Configurações setadas no config.py
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
from objects.background import Background #Classe que renderiza o background
from objects.floor import Floor #Classe que renderiza o chão
from objects.column import Column #Classe que cria os obstáculos
from objects.bird import Bird #Classe que renderiza e comanda o passaro


pygame.init() #Inicia o pygame


screen=pygame.display.set_mode((config.Screen_width, config.Screen_height)) #Cria uma janela e seta seu tamanho
pygame.display.set_caption("Flappy Bird") #Seta o nome da janela de "Flappy Bird"
pygame.display.set_icon(pygame.image.load('assets/icons/red_bird.png')) #Seta o icone da janela

clock=pygame.time.Clock() #Cria o objeto Clock para controlar a taxa de atualização
column_event=pygame.USEREVENT #Cria um evento chamado 'column_event' que irá servir para chamar a classe Column e criar os obstaculos
running=True #Variavel para dizer que o jogo está rodando

assets.load_sprites() #Carrega os sprites

sprites=pygame.sprite.LayeredUpdates() #Cria uma classe que serve para gerenciar os sprites e controla a ordem de camadas

for i in range(2):
    Background(i, sprites) #Cria e adiciona o sprite "background" no gurpo de sprites, seta sua profundidade, posiciona na tela e cria um loop para que nunca suma o fundo
    Floor(i, sprites) #Cria e adiciona o sprite "floor" no gurpo de sprites, seta sua profundidade, posiciona na tela e cria um loop para que nunca suma o chão

bird=Bird(sprites) #Cria e adiciona o sprite "bird" no grupo de sprites com a profundidade correta.

pygame.time.set_timer(column_event, 1500) #Faz com que o evento 'column_event' seja adicionado na fila de eventos a cada 1,5 segundos

#Loop principal do jogo
while running:
    for event in pygame.event.get(): #Verifica e executa os eventos que estão na fila
        if event.type==pygame.QUIT: #Evento de quando se aperta para fechar a janela
            running=False
        if event.type==column_event: #Caso seja o evento 'column_event' mandasse criar um obstáculo
            Column(sprites) #Cria um sprite do obstaculo setando sua profundidade e adiciona no grupo de sprites
        
        bird.handle_event(event) #Chama a função 'handle_event' da classe 'Bird' para, caso se aperte o 'espaço' o pássaro suba um pouco na tela

    screen.fill("black") #Preenche a tela de preto
    sprites.draw(screen) #Desenha todos os sprites na tela de acordo com a ordem de camadas setada
    sprites.update() #Chama a função 'update()' de todos os sprites

    pygame.display.flip() #Atualiza a tela
    clock.tick(config.FPS) #Controla o FPS para se manter a 60 quadros

pygame.quit() #Fecha o pygame e termina o programa