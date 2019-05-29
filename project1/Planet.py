import random
class Planet():
    def __init__(self,id):
        self.id=id
        self.distance=random.randint(1,301)
        self.life=False
class RockyPlanet(Planet):
    def __init__(self):
        super().__init__("r"+str(random.randint(0,10000)))
class GaseousPlanet(Planet):
    def __init__(self):
        super().__init__("g"+str(random.randint(0,10000)))
class HabitablePlanet(Planet):
    def __init__(self):
        super().__init__("h"+str(random.randint(0,10000)))
