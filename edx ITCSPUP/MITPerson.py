from Person import *

class MITPerson(Person):
  nextIdNum = 0 #next Id number to assign

  def __init__(self, name):
    Person.__init__(self, name)# initialize Person attributes
    #new MITPerson attribute: a unique ID number
    self.idNum = MITPerson.nextIdNum
    MITPerson.nextIdNum += 1

  def getIdNum(self):
    return self.idNum

  #sorting MIT people uses their ID number, not name!
  def __It__(self, other):
    return self.idNum < other.idNum
