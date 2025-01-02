import pygame.sprite
import assets
import config
import random

class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.gap=100
        self.sprite=assets.get_sprite("pipe-green");
        self.sprite_rect=self.sprite.get_rect()

        self.down_tube=self.sprite
        self.down_tube_rect=self.down_tube.get_rect(topleft=(0,self.sprite_rect.height+self.gap))

        self.up_tube=pygame.transform.flip(self.sprite, False, True)
        self.up_tube_rect=self.up_tube.get_rect(topleft=(0,0))

        height_floor=assets.get_sprite("floor").get_rect().height
        min_y=100
        max_y=config.Screen_height-height_floor-100

        self.image=pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height*2+self.gap), pygame.SRCALPHA)
        self.image.blit(self.down_tube, self.down_tube_rect)
        self.image.blit(self.up_tube, self.up_tube_rect)
        self.rect=self.image.get_rect(midleft=(config.Screen_width,random.uniform(min_y, max_y)))

        super().__init__(*groups)

    def update(self):
        self.rect.x-=2

        if self.rect.x<=-self.rect.width:
            self.kill()
