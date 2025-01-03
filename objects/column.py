import pygame.sprite #Importa o modulo que serve para gerenciar os objetos (sprites) dentro do jogo
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
import config  #Configurações setadas no config.py
import random #Biblioteca com funções para gerar numeros aleatórios. É utilizada para gerar uma posição aleatória para o obstáculo no eixo y
from layer import Layer  #Importa a classe que define a ordem dos sprites

#Classe que define o obstáculo do jogo e herda as funções da classe de Sprite.Group() do pygame
class Column(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, *groups):
        self._layer=Layer.OBSTACLE #Seta a profundidade
        self.gap=100 #Define o espaço entre o cano de cima e o de baixo como 100
        self.sprite=assets.get_sprite("pipe-green"); #Atribui o sprite "pipe-green" a variável self.sprite
        self.sprite_rect=self.sprite.get_rect() #Cria um retângulo com esse sprite

        self.down_tube=self.sprite #Seta o sprite do tubo de baixo
        self.down_tube_rect=self.down_tube.get_rect(topleft=(0,self.sprite_rect.height+self.gap)) #Cria um retângulo com o sprite setado anteriormente e posiciona em relação a superfície que será colocado dentro

        self.up_tube=pygame.transform.flip(self.sprite, False, True) #Inverte o sprite do tubo para ficar de cabeça para baixo e guarda no self.up_tube
        self.up_tube_rect=self.up_tube.get_rect(topleft=(0,0))  #Cria um retângulo com o sprite setado anteriormente e posiciona em relação a superfície que será colocado dentro

        height_floor=assets.get_sprite("floor").get_rect().height #Pega a altura do chão
        min_y=100 #Seta uma posição mínima no eixo y
        max_y=config.Screen_height-height_floor-100 #Seta uma posição máximano eixo y

        self.image=pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height*2+self.gap), pygame.SRCALPHA) #Cria uma superfície da largura dos tubos e altura dos dois tubos mais o gap
        self.image.blit(self.down_tube, self.down_tube_rect) #Coloca o tubo de baixo dentro da superficie
        self.image.blit(self.up_tube, self.up_tube_rect) #Coloca o tubo de cima dentro da superficie
        self.rect=self.image.get_rect(midleft=(config.Screen_width,random.uniform(min_y, max_y))) #Cria um retângulo com essa superfície e posiciona na tela

        super().__init__(*groups)

    #Função para ir atualizando a posição do obstáculo
    def update(self):
        self.rect.x-=2 #Faz o objeto ir andando para trás

        if self.rect.right<=0: #Apaga o objeto criado quando ele sair da tela 
            self.kill()
