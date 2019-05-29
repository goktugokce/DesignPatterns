from Universe import *
import math
class Probe():
    def __init__(self,probeUniverse):
        self.startedX=random.randint(0,2**64)-1
        self.startedY=random.randint(0,2**64)-1
        self.startedZ=random.randint(0,2**64)-1
        self.traveledDistance=0
        self.numberOfVisitedStars=0
        self.numberOfExploredPlanets=0
        self.fuel=2**70
        self.probeUniverse=Universe()
        self.measuredDistance=0
        self.lifeCounter=0
        self.planetID=""
        self.nextX=self.startedX
        self.nextY=self.startedY
        self.nextZ=self.startedZ
        self.printInformation()
    def printInformation(self):
        for i in self.probeUniverse.starArray:
            if(i.isVisited==False):
                self.measuredDistance=math.sqrt((self.nextX-i._x)**2+(self.nextY-i._y)**2+(self.nextZ-i._z)**2)
                i.isVisited=True
                if self.fuel>=self.measuredDistance:
                    self.nextX=i._x
                    self.nextY=i._y
                    self.nextZ=i._z
                    self.traveledDistance=self.traveledDistance+self.measuredDistance
                    self.numberOfVisitedStars=self.numberOfVisitedStars+1
                    self.fuel=self.fuel-self.measuredDistance+i.recharge
                    for k in i.planetArray:
                        self.numberOfExploredPlanets=self.numberOfExploredPlanets+1
                        if(k.life==True):
                            self.lifeCounter=self.lifeCounter+1
                            self.planetID=k.id

        print("Your origin was ({} {} {})".format(self.startedX,self.startedY,self.startedZ))
        print("Traveled {}".format(self.traveledDistance))
        print("\t You have {} fuel remaining".format(self.fuel))
        print("\t Visited {} stars".format(self.numberOfVisitedStars))
        print("\t Explored {} planets".format(self.numberOfExploredPlanets))
        if(self.lifeCounter>0):
            print("Life founded on planet {}".format(self.planetID))
        else:
            print("No Life Founded")
