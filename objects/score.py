import pygame.sprite #Importa o modulo que serve para gerenciar os objetos (sprites) dentro do jogo
import config #Configurações setadas no config.py
import assets #Arquivo em que temos as funções que carregam os sprites e os audios
from layer import Layer #Importa a classe que define a ordem dos sprites

#Classe que define o 'Score' do jogo e herda as funções da classe de Sprite.Group() do pygame
class Score(pygame.sprite.Sprite):
    #Função construtora
    def __init__(self, *groups):
        self._layer=Layer.UI #Seta a profundidade

        self.value=0 #Inicia o valor do pontos como '0'
        self.image=assets.get_sprite(str(self.value)) #Guarda o sprite "0" no self.image
        self.rect=self.image.get_rect(center=(config.Screen_width/2, 50)) #Cria um retângulo com o sprite criado, e posiciona na tela

        super().__init__(*groups)

    #Função que atualiza a pontuação
    def atualiza(self):
        self.value+=99 #Soma mais 1 ao valor da pontuação
        str_value= str(self.value) #Cria uma variável auxiliar com o valor da pontuação em formato de string

        self.img=[] #Inicializa uma lista 'self.img' para guardar os sprites os numeros da pontuação
        self.width=0 #Cria uma váriavel para guardar o tamanho total que o retângulo que conterá o valor deve ter

        for number in str_value: #Loop que passa por cada um dos algarismos da pontuação
           img=assets.get_sprite(number) #Pega sprite que equivale ao algarismo atual
           self.img.append(img) #Guarda no final a lista 'self.img'
           self.width+=img.get_width() #Pega a largura do sprite atual e soma com o valor de 'self.width'
        
        self.height=self.img[0].get_height() #Pega qual a altura que o retângulo deve ter pegando a altura do primeiro sprite da lista
        self.image=pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA) #Cria uma superfície com a altura do 'self.height' e largura do 'self.width'
        self.rect=self.image.get_rect(center=(config.Screen_width/2, 50)) #Cria um retângulo com essa superfície e posiciona na tela

        pos=0 #Variável auxiliar para dizer a posição que o sprite de cada algarismo de ser colocado
        for num in self.img: #Loop que passa que passa por cada um dos sprites guardados na lista 'self.img'
            self.image.blit(num, (pos,0)) #Coloca o spirte atual na posição (pos, 0)
            pos+=num.get_width() #Atualiza a variável 'pos' somando 