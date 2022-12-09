import random
from dino_runner.utils.constants import SCREEN_HEIGHT
from pygame.sprite import Sprite 

class PowerUP():
    def __init__(self):
        self.image = image
        self.rect = self.image.get_rect()
        self.type = typeself.rect.x = SCREEN_HEIGHT + random.randint(800,1000)
        self.rect.y = random.randint(100,150)
        self.start_time = 0
        self.width = self.image.get_width()
        

    



