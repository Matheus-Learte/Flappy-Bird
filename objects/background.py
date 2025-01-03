import pygame.sprite #Importa o modulo que serve para gerenciar os objetos (sprites) dentro do jogo
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
import config #Configurações setadas no config.py
from layer import Layer #Importa a classe que define a ordem dos sprites

#Classe que define o fundo do jogo e herda as funções da classe de Sprite.Group() do pygame
class Background(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, index, *groups):
        self._layer=Layer.BACKGROUND
        self.image=assets.get_sprite("background") #Guarda o sprite "background" no self.image
        self.rect=self.image.get_rect(topleft=(config.Screen_width*index ,0)) #Cria um retângulo com o sprite criado, e posiciona na tela

        super().__init__(*groups)

    #Função que atualiza a posição do sprite para trás no eixo x
    def update(self):
        self.rect.x-=1 

        if self.rect.right<=0: #Quando o sprite sai da tela ele reinicia a posição da imagem para a posição mais a direita em relação o eixo x
            self.rect.x=config.Screen_width

    