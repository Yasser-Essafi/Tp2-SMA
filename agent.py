import uuid
from body import Body
import pygame
from random import randint

from fustrum import Fustrum

# Class Agent
class EnvObj:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.body = Body()

    def draw(self, window):
        agent_pos = self.body.pos
        agent_radius = self.body.radius
        agent_color = self.body.color
        pygame.draw.circle(window, agent_color,
                   agent_pos, agent_radius)

    def update(self, decision):
        self.body.update(decision)
        # pygame.display.update()





class Agent(EnvObj):
    def __init__(self) -> None:
        super().__init__()
        self.fustrum = Fustrum(3000)
        
    def move(self, pos):
        mouse_pos = pos

        dx = mouse_pos[0] - self.body.pos[0]
        dy = mouse_pos[1] - self.body.pos[1]

        if self.body.pos[0] != mouse_pos[0]:
            if dx > 0:
                self.body.pos[0] += 6
            elif dx < 0:
                self.body.pos[0] -= 6
    
        if self.body.pos[1] != mouse_pos[1]:
            if dy > 0:
                self.body.pos[1] += 6
            elif dy < 0:
                self.body.pos[1] -= 6

    def hide(self, pos):
        mouse_pos = pos

        dx = mouse_pos[0] - self.body.pos[0]
        dy = mouse_pos[1] - self.body.pos[1]

        if self.body.pos[0] != mouse_pos[0]:
            if dx < 0:
                self.body.pos[0] += 5
            elif dx > 0:
                self.body.pos[0] -= 5
    
        if self.body.pos[1] != mouse_pos[1]:
            if dy < 0:
                self.body.pos[1] += 5
            elif dy > 0:
                self.body.pos[1] -= 5

    def get_pts(self, list_agents):
        for index, agent in enumerate(list_agents[:-1]):
            mouse_pos = pygame.mouse.get_pos()
            # print("----> ", self.body.pos, agent.body.pos)
            if (agent.body.pos[0] < (self.body.pos[0] + self.body.radius)) and (agent.body.pos[0] > (self.body.pos[0] - self.body.radius)) and (agent.body.pos[1] < (self.body.pos[1] + self.body.radius)) and (agent.body.pos[1] > (self.body.pos[1] - self.body.radius)):
            # if mouse_pos == agent.body.pos:
                del list_agents[index]
                self.body.radius += 1
                break




class Immunes(EnvObj):
    def __init__(self) -> None:
        super().__init__()
        self.body.radius = 6
        self.body.color = (255, 0, 0)
        self.status= 'immunes'


class Infectueux(EnvObj):
    def __init__(self) -> None:
        super().__init__()
        self.body.color = (0, 200, 0)
        self.body.radius = 6
        self.status='infectueux'

class Saines(EnvObj):
    def __init__(self) -> None:
        super().__init__()
        self.body.color = (0, 200, 0)
        self.body.radius = 6
        self.status='saines'
