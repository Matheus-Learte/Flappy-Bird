import pygame.sprite
import assets
import config

class Column(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self.image=assets.get_sprite("pipe-green");
        self.rect=self.image.get_rect(bottomleft=(config.Screen_width*index, config.Screen_height))

        super().__init__(*groups)