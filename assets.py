import os #Biblioteca para navegar entre os diretórios
import pygame #Biblioteca para desenvolvimento de jogos

#Dicionarios que guardam os sprites e os audios carregados 
sprites={} 
audios={}

#Função para carregar todos os sprites e guardar no dicionario 'sprites'
def load_sprites():
    path=os.path.join("assets", "sprites")

    for file in os.listdir(path):
        sprites[file.split('.')[0]]=pygame.image.load(os.path.join(path, file))

#Função para retornar um sprite
def get_sprite(name):
    return sprites[name]

#Função para carregar os audios e guardar no dicionario 'audios'
def load_audios():
    path=os.path.join("assets", "audios")

    for file in os.listdir(path):
        audios[file.split('.')[0]]=pygame.mixer.Sound(os.path.join(path, file))

#Função para reproduzir um audio específico
def get_audio(name):
    audios[name].play()