import random
from dino_runner.components.obstacle.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super()._init_(image, self.type)
        self.rect.y = 325