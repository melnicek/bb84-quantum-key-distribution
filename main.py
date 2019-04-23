#!/bin/env python

import random
import base64
from alice import Alice
from bob import Bob
from eve import Eve
import argparse

if __name__== "__main__":
  parser = argparse.ArgumentParser(description='Quantum key distribution with protocol BB84')

  parser.add_argument('key_amount', help="Amount of keys to create")
  parser.add_argument('key_size', help="Size of each key in bytes")
  parser.add_argument('-v', '--verbose', action="store_true", help="Verbose output")
  parser.add_argument('-e', '--eve', action="store_true", help="Eve is present")

  args = parser.parse_args()

  key_amount = int(args.key_amount)
  key_size = int(args.key_size)
  verbose = args.verbose
  eve_exists = args.eve
  detected = 0

  for i in range(key_amount):

    alice = Alice()
    bob = Bob()
    eve = Eve()

    alice.reset()
    bob.reset()

    qubits = bob.send_qubits(key_size * 8 * 4)

    qubits = qubits
    qubits = qubits
    qubits = qubits
    qubits = qubits
    if(eve_exists == True):
      qubits = eve.measure_qubits(qubits)
    qubits = qubits
    qubits = qubits
    qubits = qubits
    qubits = qubits

    orientations = alice.measure_qubits(qubits)

    indexes = bob.compare_orientations(orientations)

    bob_key = bob.create_key(key_size)
    alice_key = alice.create_key(indexes, key_size)

    if(alice_key != bob_key):
      detected += 1

    if(verbose == True):
      print(" Alice's key: {}".format(alice_key))
      print(" Bob's key:   {}".format(bob_key))
      print(" Eve detected: {}".format(alice_key != bob_key))
      print(" Eve detected {}/{} times".format(detected, key_amount))
      print()

  print("Eve detected {}/{} times".format(detected, key_amount))