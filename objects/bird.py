import pygame.sprite
import config
import assets
from layer import Layer
from objects.column import Column
from objects.floor import Floor

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
        self.rect=self.image.get_rect(topleft=(-50, 50)) #Cria um retângulo com o sprite criado, e posiciona na tela
        self.mask=pygame.mask.from_surface(self.image) #Cria uma cria uma máscara envolvendo os pixels não invisíveis do sprite do pássaro

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

        if self.rect.x<=50: #Checa se o pássaro está atrás da posição 50 no eixo x
            self.rect.x+=2 #Impulsiona o pássaro 2 posições para frente no eixo x 

    #Função que faz com que ao o 'espaço' ser apertado o pássaro suba um pouco na tela
    def handle_event(self, event):
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE: #Testa se o 'espaço' foi apertado
            self.fall=-6 #Atribui a quantidad de queda -7 para fazer o passaro subir a cada vez que o espaço por apertado

    #Função que verifica se o pássaro bateu no chão ou no cano
    def check_collision(self, sprites):
        for sprite in sprites: #Loop que passa por todos os sprites
            if (type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(self.mask, (self.rect.x-sprite.rect.x, self.rect.y-sprite.rect.y)): #Verifica se o sprite é uma coluna ou o chão e vê se a mascara desse sprite e a do pássaro se interceptam
                return True
        return False