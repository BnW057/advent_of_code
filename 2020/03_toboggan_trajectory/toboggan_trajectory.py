import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # Open file to read values
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  # Initialize loop variable for trying different paths
  cont = True
  # Initialize offset variable for different starting points.
  offset = 0
  # Initialize positional value. Only this dimension is needed.
  position = 0
  # Initialize trees value. Counts how many trees you hit.
  trees = 0
  shortest = sys.maxsize
  # Extract the length of a line from the file.
  lineLength = len(f.readline())
  # Enter file read loop
  while cont:
    # Reset the file pointer to beginning
    f.seek(0)
    # Tree counter for every run
    trees = 0
    position = offset
    for line in f:
      # If the position value is larger than the length, modulate.
      # Put the remaining value in the carry.
      if position >= len(line.rstrip("\n")):
        position = position % len(line.rstrip("\n"))
      if line[position] == "#":
        trees+=1;
      position += 3
    if shortest > trees:
      shortest = trees
    offset+=1
    if offset == lineLength:
      cont = not cont
  print("The number of trees hit is: " + str(trees))

main()
