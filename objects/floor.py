import pygame.sprite
import assets
import config
from layer import Layer

# Cria uma classe que define o chão que herda funções da classe sprite.Group() do pygame
class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer=Layer.FLOOR
        self.image=assets.get_sprite("floor") # Guarda o sprite "floor" no self.image
        self.rect=self.image.get_rect(bottomleft=(config.Screen_width*index, config.Screen_height))

        super().__init__(*groups)
    
    def update(self):
        self.rect.x-=2

        if self.rect.right<=0:
            self.rect.x=config.Screen_width