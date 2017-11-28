class Location(object):

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.Y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.t - yo
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return  "<" + str(self.x) + ", " + str(self.y) + ">"
