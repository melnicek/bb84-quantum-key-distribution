import random
from qubit import Qubit

class Alice(object):

  bits = []
  orientations = []
  key = []

  def __init__(self):
    pass

  def reset(self):
    self.bits = []
    self.orientations = []
    self.key = []
  
  def measure_qubits(self, recived_qubits):

    for i in range(len(recived_qubits)):
      self.orientations.append(random.randint(0,1))

    for i in range(len(recived_qubits)):
      if(self.orientations[i] == 0):
        self.bits.append(recived_qubits[i].measure("horizontal"))
      else:
        self.bits.append(recived_qubits[i].measure("vertical"))

    return self.orientations

  def create_key(self, indexes_of, length):
    for i in indexes_of:
      self.key.append(self.bits[i])
    byte_array = []
    try:
      for i in range(0,99999999,8):
        tmp = ""
        for b in range(8):
          tmp += str(self.key[i+b])
        byte_array.append(int(tmp,2))
        if(len(byte_array) == length):
          break
    except:
      pass
    return byte_array
