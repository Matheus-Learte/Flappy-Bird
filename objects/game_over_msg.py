import pygame.sprite #Importa o modulo que serve para gerenciar os objetos (sprites) dentro do jogo
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
import config #Configurações setadas no config.py
from layer import Layer #Importa a classe que define a ordem dos sprites

#Classe que define a mensagem de 'Game-Over' do jogo e herda as funções da classe de Sprite.Group() do pygame
class Game_Over(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, *groups):
        self._layer=Layer.UI #Seta a profundidade
        self.image=assets.get_sprite("gameover") #Guarda o sprite "gameover" no self.image
        self.rect=self.image.get_rect(center=(config.Screen_width/2, config.Screen_height/2)) #Cria um retângulo com o sprite criado, e posiciona na tela

        super().__init__(*groups)