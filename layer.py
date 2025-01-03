from enum import IntEnum, auto #Importa a classe e a funçãoq que servem para criar enumereções em ordem

#Define a ordem de profundidade dos sprites
class Layer(IntEnum):
    BACKGROUND=auto() #1
    OBSTACLE=auto() #2
    FLOOR=auto() #3
    PLAYER=auto() #4
    UI=auto() #5