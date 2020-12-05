import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # Open file to read values
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  # Initialize loop variable for trying different paths
  config = [1,1]
  # Initialize positional value. Only this dimension is needed.
  position = 0
  # Initialize trees value. Counts how many trees you hit.
  trees = 0
  hitList = []
  # Extract the length of a line from the file.
  lineLength = len(f.readline())
  # Try different configurations
  while config[1] <= 2:
    # Reset the file pointer to beginning
    f.seek(0)
    # Tree counter for every run
    trees = 0
    position = 0
    for index, line in enumerate(f):
      if config[1] == 2 and index % 2 != 0:
        continue
      # If the position value is larger than the length, modulate.
      # Put the remaining value in the carry.
      if position >= len(line.rstrip("\n")):
        position = position % len(line.rstrip("\n"))
      if line[position] == "#":
        trees+=1;
      position += config[0]
    print("Current configuration: " + str(config))
    print("The number of trees hit is: " + str(trees))
    hitList.append(trees)
    config[0] += 2
    if config[1] == 2:
      break
    if config[0] > 8:
      config[0] = 1
      config[1] = 2
  print(hitList)

main()
