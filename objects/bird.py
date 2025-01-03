import pygame.sprite
import config
import assets
from layer import Layer

class Bird(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, *groups):
        self._layer=Layer.PLAYER #Seta a profundidade
        self.images=[
            assets.get_sprite('redbird-upflap'),
            assets.get_sprite('redbird-midflap'),
            assets.get_sprite('redbird-downflap')
        ] #Lista de sprites do pássaro

        self.image=self.images[0] #Guarda o sprite "redbird-upflap" no self.image
        self.rect=self.image.get_rect(topleft=(0, 0)) #Cria um retângulo com o sprite criado, e posiciona na tela

        self.fall=0 #Seta uma variável de quantidade de queda como 0

        super().__init__(*groups)

    # Função que vai trocando entre os três sprites do pásaro para criar a ilusão de 'bater asas',
    #vai aumentando a variável de quantidade de queda em relação a cosntante 'Newton' e faz o pássaro cair
    #de acordo com a quantidade de queda
    def update(self):
        self.images.insert(0, self.images.pop()) #Joga o sprite do final da lista para a primeira posição  
        self.image=self.images[0] #Atribui esse novo sprite para a variável self.image

        self.fall+=config.NEWTON #Acumula a quantidade de queda
        self.rect.y+=self.fall #Faz o pássaro cair em relação a essa quantidade de queda

    #Função que faz com que ao o 'espaço' ser apertado o pássaro suba um pouco na tela
    def handle_event(self, event):
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE: #Testa se o 'espaço' foi apertado
            self.fall=-7 #Atribui a quantidad de queda -7 para fazer o passaro subir a cada vez que o espaço por apertado