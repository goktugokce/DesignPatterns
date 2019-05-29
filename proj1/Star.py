from Planet import *

class Star():
	def __init__(self,x,y,z,chancesOfLife,rangeOfPlanets,goldilocksZoneMin,goldilocksZoneMax,recharge):
		self._x=x
		self._y=y
		self._z=z
		self.chancesOfLife=chancesOfLife
		self.rangeOfPlanets=rangeOfPlanets
		self.goldilocksZoneMin=goldilocksZoneMin
		self.goldilocksZoneMax=goldilocksZoneMax
		self.recharge=recharge
		self.planetArray=[]
		self.rockyPlanetCounter=0
		self.gaseousPlanetCounter=0
		self.habitablePlanetCounter=0
		self.isVisited = False
		for i in range(self.rangeOfPlanets):
			planetGenerator=random.randint(0,2)
			if(planetGenerator==0):
				generatedPlanet=RockyPlanet()
				self.planetArray.append(generatedPlanet)
				self.rockyPlanetCounter=self.rockyPlanetCounter+1
			elif(planetGenerator==1):
				generatedPlanet = GaseousPlanet()
				self.planetArray.append(generatedPlanet)
				self.gaseousPlanetCounter = self.gaseousPlanetCounter + 1
			else:
				generatedPlanet = HabitablePlanet()
				self.planetArray.append(generatedPlanet)
				self.habitablePlanetCounter = self.habitablePlanetCounter + 1
				if((generatedPlanet.distance>=self.goldilocksZoneMin) and (generatedPlanet.distance<=self.goldilocksZoneMax)):
					if(random.randint(1,10000)<=self.chancesOfLife*10000):
						generatedPlanet.life=True

class DwarfStar(Star):
	def __init__(self):
		super().__init__(random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			0.0006,
			random.randint(8,15),
			30,
			90,
			2**20)
class GiantStar(Star):
	def __init__(self):
		super().__init__(random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			0.0005,
			random.randint(5,10),
			100,
			250,
			2**30)
class MediumStar(Star):
	def __init__(self):
		super().__init__(random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			random.randint(2**3,2**64)-1,
			0.0009,
			random.randint(2,9),
			60,
			140,
			2**25)

