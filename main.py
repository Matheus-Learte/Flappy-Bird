import pygame #Biblioteca para produzir jogos no Python
import config #Configurações setadas no config.py
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
from objects.background import Background #Classe que renderiza o background
from objects.floor import Floor #Classe que renderiza o chão
from objects.column import Column #Classe que cria os obstáculos
from objects.bird import Bird #Classe que renderiza e comanda o passaro
from objects.game_over_msg import Game_Over #Classe que renderiza a mensagem de 'Game Over'
from objects.start_msg import Start #Classe que renderiza a mensagem de 'Start' do jogo
from objects.score import Score #Classe que renderiza e comanda o score

#Função que ao ser chamado renderiza o fundo e o chão do jogo
def cenario(nome):
    for i in range(2):
        Background(i, nome) #Cria e adiciona o sprite "background" no gurpo de sprites, seta sua profundidade, posiciona na tela e cria um loop para que nunca suma o fundo
        Floor(i, nome) #Cria e adiciona o sprite "floor" no gurpo de sprites, seta sua profundidade, posiciona na tela e cria um loop para que nunca suma o chão


pygame.init() #Inicia o pygame

screen=pygame.display.set_mode((config.Screen_width, config.Screen_height)) #Cria uma janela e seta seu tamanho
pygame.display.set_caption("Flappy Bird") #Seta o nome da janela de "Flappy Bird"
pygame.display.set_icon(pygame.image.load('assets/icons/red_bird.png')) #Seta o icone da janela

clock=pygame.time.Clock() #Cria o objeto Clock para controlar a taxa de atualização
column_event=pygame.USEREVENT #Cria um evento chamado 'column_event' que irá servir para chamar a classe Column e criar os obstaculos
running=True #Variavel para dizer se a janela do jogo está aberta
StartGame=False #Variável para dizer se o jogo está rodando
GameOver=False #Variável para dizer se o jogador perdeu

assets.load_sprites() #Carrega os sprites

sprites=pygame.sprite.LayeredUpdates() #Cria uma classe que serve para gerenciar os sprites e controla a ordem de camadas
cenario(sprites) #Carrega o cenário
bird=Bird(sprites) #Renderiza o pássaro
start=Start(sprites) #Renderiza a mensagem se 'Start'
pontos=Score(sprites) #Renderiza os pontos

#Loop principal do jogo
while running:
    for event in pygame.event.get(): #Verifica e executa os eventos que estão na fila
        if event.type==pygame.QUIT: #Evento de quando se aperta para fechar a janela
            running=False
        if event.type==column_event: #Caso seja o evento 'column_event' mandasse criar um obstáculo
            Column(sprites) #Cria um sprite do obstaculo setando sua profundidade e adiciona no grupo de sprites
        if event.type==pygame.KEYDOWN: #Testa se algum botão foi clicado no teclado
            if (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE) and not StartGame and not GameOver: #Caso ambas variáveis de controle 'StartGame' e 'GameOver'sejam 'False' e tenha sido apertado o 'espaço' ele apaga a mensagem de start e começa a carregar os obstáculos
                StartGame=True
                pygame.time.set_timer(column_event, 1500)
                start.kill()
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_r) and GameOver: #Caso 'GameOver' seja igual True e tenha sido apertado o botão 'R' o jogo é reiniciado apagando todos os sprites e os recarregando
                GameOver=False #Seta como 'False' para entrar no if anterior
                StartGame=False #Seta como 'False' para entrar no if anterior
                sprites.empty() #Serve para apagar todos os sprites
                cenario(sprites) #Recarrega o cenário
                start=Start(sprites) #Recarrega a mensagem de 'Start'
                bird=Bird(sprites) #Renderiza de novo o pássaro
                pontos=Score(sprites) #Reinicia os pontos

        if StartGame: #Caso o jogador não tenha perdido ainda
            bird.handle_event(event) #Chama a função 'handle_event' da classe 'Bird' para, caso se aperte o 'espaço' o pássaro suba um pouco na tela

    screen.fill("black") #Preenche a tela de preto
    sprites.draw(screen) #Desenha todos os sprites na tela de acordo com a ordem de camadas setada
    
    if StartGame: #Caso o jogador não tenha perdido ainda
        sprites.update() #Chama a função 'update()' de todos os sprites

    if bird.check_collision(sprites) and not GameOver: #Caso o pássaro tenha bátido ou no chão ou em algum obstáculo e a variável 'GameOver' seja 'False'
        GameOver=True 
        StartGame=False
        pygame.time.set_timer(column_event, 0) #Para de mandar comandos para renderizar obstáculos
        Game_Over(sprites) #Renderiza a mensagem de 'Game-Over'
            
    for sprite in sprites: #Loop que passa por todos os sprites
        if type(sprite) is Column and sprite.passed(): #Verifica se o tipo do sprite é 'Column' e se sprite.passed() está retornando True
            pontos.atualiza() #Adiciona mais 1 ponto no score

    pygame.display.flip() #Atualiza a tela
    clock.tick(config.FPS) #Controla o FPS para se manter a 60 quadros

pygame.quit() #Fecha o pygame e termina o programa