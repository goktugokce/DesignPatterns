from Star import *
class Universe():
    def __init__(self):
        self.starNumber=2**10
        self.starArray=[]
        self.dwarfStarCounter=0
        self.giantStarCounter=0
        self.mediumStarCounter=0
        for i in range(self.starNumber):
            starGenerator=random.randint(0,2)
            if(starGenerator==0):
                generatedStar=DwarfStar()
                self.starArray.append(generatedStar)
                self.dwarfStarCounter=self.dwarfStarCounter+1
            elif(starGenerator==1):
                generatedStar=GiantStar()
                self.starArray.append(generatedStar)
                self.giantStarCounter=self.giantStarCounter+1
            else:
                generatedStar=MediumStar()
                self.starArray.append(generatedStar)
                self.mediumStarCounter=self.mediumStarCounter+1

    def printUniverse(self):
        self.dwarfStarRockyPlanetCounter=0
        self.dwarfStarGaseousPlanetCounter=0
        self.dwarfStarHabitablePlanetCounter=0
        self.giantStarRockyPlanetCounter=0
        self.giantStarGaseousPlanetCounter=0
        self.giantStarHabitablePlanetCounter=0
        self.mediumStarRockyPlanetCounter=0
        self.mediumStarGaseousPlanetCounter=0
        self.mediumStarHabitablePlanetCounter=0
        self.dwarfIntelligentLifeCounter=0
        self.giantIntelligentLifeCounter=0
        self.mediumIntelligentLifeCounter=0
        for j in self.starArray:
            if (isinstance(j,DwarfStar)):
                for k in j.planetArray:
                    if(isinstance(k,RockyPlanet)):
                        self.dwarfStarRockyPlanetCounter=self.dwarfStarRockyPlanetCounter+1
                    elif(isinstance(k, GaseousPlanet)):
                        self.dwarfStarGaseousPlanetCounter=self.dwarfStarGaseousPlanetCounter+1
                    elif(isinstance(k, HabitablePlanet)):
                        self.dwarfStarHabitablePlanetCounter=self.dwarfStarHabitablePlanetCounter+1
                        if(k.life==True):
                            self.dwarfIntelligentLifeCounter=self.dwarfIntelligentLifeCounter+1
            elif(isinstance(j,GiantStar)):
                for k in j.planetArray:
                    if(isinstance(k, RockyPlanet)):
                        self.giantStarRockyPlanetCounter=self.giantStarRockyPlanetCounter+1
                    elif (isinstance(k, GaseousPlanet)):
                        self.giantStarGaseousPlanetCounter=self.giantStarGaseousPlanetCounter+1
                    elif (isinstance(k, HabitablePlanet)):
                        self.giantStarHabitablePlanetCounter=self.giantStarHabitablePlanetCounter+1
                        if(k.life==True):
                            self.giantIntelligentLifeCounter=self.giantIntelligentLifeCounter+1
            elif(isinstance(j,MediumStar)):
                for k in j.planetArray:
                    if (isinstance(k, RockyPlanet)):
                        self.mediumStarRockyPlanetCounter=self.mediumStarRockyPlanetCounter+1
                    elif (isinstance(k, GaseousPlanet)):
                        self.mediumStarGaseousPlanetCounter=self.mediumStarGaseousPlanetCounter+1
                    elif (isinstance(k, HabitablePlanet)):
                        self.mediumStarHabitablePlanetCounter=self.mediumStarHabitablePlanetCounter+1
                        if(k.life==True):
                            self.mediumIntelligentLifeCounter=self.mediumIntelligentLifeCounter+1
        print("Total number of stars in my universe: {}".format(self.starNumber))
        print("There are {} Dwarf Stars With:".format(self.dwarfStarCounter))
        print("\t {} Rocky Planets".format(self.dwarfStarRockyPlanetCounter))
        print("\t {} Gaseous Planets".format(self.dwarfStarGaseousPlanetCounter))
        print("\t {} Habitable Planets".format(self.dwarfStarHabitablePlanetCounter))
        print("\t {} Planets with Intelligent Life".format(self.dwarfIntelligentLifeCounter))
        print("\n")
        print("There are {} Giant Stars With:".format(self.giantStarCounter))
        print("\t {} Rocky Planets".format(self.giantStarRockyPlanetCounter))
        print("\t {} Gaseous Planets".format(self.giantStarGaseousPlanetCounter))
        print("\t {} Habitable Planets".format(self.giantStarHabitablePlanetCounter))
        print("\t {} Planets with Intelligent Life".format(self.giantIntelligentLifeCounter))
        print("\n")
        print("There are {} Medium Stars With:".format(self.mediumStarCounter))
        print("\t {} Rocky Planets".format(self.mediumStarRockyPlanetCounter))
        print("\t {} Gaseous Planets".format(self.mediumStarGaseousPlanetCounter))
        print("\t {} Habitable Planets".format(self.mediumStarHabitablePlanetCounter))
        print("\t {} Planets with Intelligent Life".format(self.mediumIntelligentLifeCounter))
        print("\n")


