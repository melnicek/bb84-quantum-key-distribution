import random
from qubit import Qubit

class Eve(object):

  def __init__(self):
    pass
  
  def measure_qubits(self, recived_qubits):

    orientations = []

    for i in range(len(recived_qubits)):
      orientations.append(random.randint(0,1))

    for i in range(len(recived_qubits)):
      if(orientations[i] == 0):
        recived_qubits[i].measure("horizontal")
      else:
        recived_qubits[i].measure("vertical")

    return recived_qubits