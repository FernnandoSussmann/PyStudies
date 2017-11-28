class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "This drunk is named " + self.name

import random

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f,d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunks(d)
    return (start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk("Homer")
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials = 20):
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print "Random walk of " + str(numSteps) + "steps"
        print "Mean =", sum(distances)/len(distances)
        print "Max =", max(distances), "Min =", min(distances)
