import random

class Qubit(object):

  bloch = 0

  def __init__(self, bloch):
    self.bloch = bloch
  
  def measure(self, rotation):
    if(rotation == "horizontal"):
      if(self.bloch == 90 or self.bloch == 270):
        return int(self.bloch == 270)
      else:
        if(random.randint(0,1) == 1):
          self.bloch = 90
        else:
          self.bloch = 270
        return int(self.bloch == 90)
    
    if(rotation == "vertical"):
      if(self.bloch == 0 or self.bloch == 180):
        return int(self.bloch == 180)
      else:
        if(random.randint(0,1) == 1):
          self.bloch = 0
        else:
          self.bloch = 180
        return int(self.bloch == 0)