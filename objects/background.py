import pygame.sprite
import assets
import config

#Classe que define o fundo do jogo e e herda as funções da classe de Ssprite.Group() do pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self.image=assets.get_sprite("background") # Guarda o sprite "background" no self.image
        self.rect=self.image.get_rect(topleft=(config.Screen_width*index ,0))

        super().__init__(*groups)

    #Função que atualiza a posição do sprite para trás no eixo x
    def update(self):
        self.rect.x-=1 

        if self.rect.right<=0:
            self.rect.x=config.Screen_width

    