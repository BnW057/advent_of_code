import os
from array import *
import re

__location__ = os.path.realpath(
  os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # Create 2D array for container bag and contained bags list.
  containers = []
  # Open puzzle input
  with open(os.path.join(__location__, 'puzzle_input.txt'), 'r') as f:
    for line in f:
      if line == '\n':
        continue
      print(line)

main()
