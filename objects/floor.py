import pygame.sprite #Importa o modulo que serve para gerenciar os objetos (sprites) dentro do jogo
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
import config #Configurações setadas no config.py
from layer import Layer #Importa a classe que define a ordem dos sprites

#Cria uma classe que define o chão que herda funções da classe sprite.Group() do pygame
class Floor(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, index, *groups):
        self._layer=Layer.FLOOR #Seta a profundidade
        self.image=assets.get_sprite("floor") #Guarda o sprite "floor" no self.image
        self.rect=self.image.get_rect(bottomleft=(config.Screen_width*index, config.Screen_height)) #Cria um retângulo com o sprite criado, e posiciona na tela
        self.mask=pygame.mask.from_surface(self.image)
        
        super().__init__(*groups)
    
    #Função que atualiza a posição do sprite para trás no eixo x
    def update(self):
        self.rect.x-=2

        if self.rect.right<=0: #Quando o sprite sai da tela ele reinicia a posição da imagem para a posição mais a direita em relação o eixo x
            self.rect.x=config.Screen_width