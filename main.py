import random
import core
from agent import Agent
def setup():
    core.fps = 30
    core.WINDOW_SIZE = [700, 700]
    core.memory("Infectueux",[])
    core.memory("InfectueuxNb",1)
    core.memory("Saines", [])
    core.memory("SainesNb",1)
    core.memory("Immunes", [])
    core.memory("ImmunesNb",1)
    

    for i in range(0,core.memory("InfectueuxNb")):
        core.memory("Infectueux").append(Agent(random.randint(0,0)))
    for i in range(0,core.memory("SainesNb")):
        core.memory("Saines").append(Agent(random.randint(0,0)))
    for i in range(0,core.memory("ImmunesNb")):
        core.memory("Immunes").append(Agent(random.randint(2,2)))
    
def reset():
    core.memory("Infectueux",[])
    core.memory("Saines", [])
    core.memory("Immunes", [])
    for i in range(0,core.memory("InfectueuxNb")):
        core.memory("Infectueux").append(Agent(random.randint(0,0)))
    for i in range(0,core.memory("SainesNb")):
        core.memory("Saines").append(Agent(random.randint(0,0)))
    for i in range(0,core.memory("ImmunesNb")):
        core.memory("Immunes").append(Agent(random.randint(2,2)))

  
def run():
    core.cleanScreen()
          
    

class Environment:
    def __init__(self, window) -> None:
        # Définir liste des agents
        self.list_agents = []
        self.list_Infectueux = []
        self.list_Saines = []
        self.window = window

    def draw(self):
        for agent in self.list_agents:
            agent.draw(self.window)

        for inf in self.list_Infectueux:
            inf.draw(self.window)
            
        for sai in self.list_Saines:
            sai.draw(self.window)

    def compute_perception(self):
        for agent in self.list_agents:
            for index, Infectueux in enumerate(self.list_Infectueux):
                if Infectueux.body.distance_to_obj(agent.body.pos) <= (agent.fustrum.vision + agent.body.radius):
                    agent.fustrum.list_obstacles.append(Infectueux)

            for index, Saines in enumerate(self.list_creeps):
                if Saines.body.distance_to_obj(agent.body.pos) <= (agent.fustrum.vision + agent.body.radius):
                    agent.fustrum.list_food.append(Saines)

   



    def delete_agent(self, agent):
        agent_id = agent.id
        for index, agt in enumerate(self.list_agents):
            if agt.id == agent_id:
                del self.list_agents[index]
                return agent_id
        
        return None

    def compute_decision(self, agent):

        dist_sai = agent.body.distance_to_obj(self.list_Saines[0].body.pos)
        dist_inf = agent.body.distance_to_obj(self.list_Infectueux[0].body.pos)
        i = 0
        j = 0
        for index, creep in enumerate(self.list_Saines):
            if index == 0:
                continue
            else:
                if agent.body.distance_to_obj(Saines.body.pos) <= dist_sai:
                    i = index
                    dist_sai = agent.body.distance_to_obj(Saines.body.pos)

        for index, inf in enumerate(self.list_Infectueux):
            if index == 0:
                continue
            else:
                if agent.body.distance_to_obj(inf.body.pos) <= dist_inf:
                    j = index
                    dist_inf = agent.body.distance_to_obj(inf.body.pos)
        
        return i, j

            

    def apply_decision(self):
       
        for agent in self.list_agents:
            self.compute_perception()
            i, j = self.compute_decision(agent)
            agent.move(self.list_Infectueux[i].body.pos)
            agent.hide(self.list_Saines[j].body.pos)
            agent.get_pts(self.list_Infectueux)


core.main(setup, run)