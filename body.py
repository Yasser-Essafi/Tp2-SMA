from random import randint
import pygame
import core
from pygame.math import Vector2
import math

colorFamily=[(255,0,0),(0,255,0),(0,0,255)]

class Body:
    def __init__(self) -> None:
        
        w, h = pygame.display.get_surface().get_size()
        self.debug = False
        self.pos = [randint(self.radius, w), randint(self.radius, h)]
        self.color = (randint(50, 255), 0, randint(50, 255))
        self.speed = randint(2, 6)
        self.status= ['saines','infectueux', 'immunes' ]
        self.acc = Vector2()
        self.radius=4

  

    def show(self):
        core.Draw.circle(colorFamily[self.family],self.pos)
        

        if self.debug:
            core.Draw.line((255,255,255),self.pos,self.pos,self.radius)
            core.Draw.line((255, 0, 0), self.pos, self.pos )
