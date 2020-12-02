from os import error, system
import os

# Working directory location
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def fillDictionary(loc):
  d = {};
  # Open file with values
  f = open(os.path.join(loc, 'puzzle_input.txt'), "r")
  # Map values in file into a dictionary
  for line in f:
    d[line] = True;
  # Close file after reading values
  f.close()
  return d

# This part covers the first half of the solution.
def part1():
  # Initialize variables for later use.
  d = fillDictionary(__location__)
  result = False
  # Try to find 2020 sum pair in dictionary
  for val in sorted(d.keys()):
    # Try to use difference of value as key. If True, match is found.
    try:
      result = str(str(2020-int(val)) + "\n") in d;
    except error:
      print("An error occurred.")
    # If match is found, write all respective values to a new file.
    if result == True:
      f = open(os.path.join(__location__, 'answer1.txt'), "w")
      f.write("First Value: " + val)
      f.write("Second value: " + str(2020-int(val)) + "\n")
      f.write("Multipying both:" + str(int(val) * (2020-int(val))))
      f.close()
      break
  print("End of first part.")

def writeAnswer2(one, two, three):
  f = open(os.path.join(__location__, 'answer2.txt'), "w")
  f.write("First Value: " + str(one) + "\n")
  f.write("Second value: " + str(two) + "\n")
  f.write("Third value: " + str(three) + "\n")
  f.write("Product: " + str(one * two* three))
  f.close()

# This part covers the second half of the solution.
def part2():
  # A dictionary approach fails here. A list has to be used instead.
  l = []
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  # Map values in file into a list of integers.
  for line in f:
    l.append(int(line))
  # Close file after reading values
  f.close()
  # Sort the list.
  l = sorted(l)
  for one in l:
    # Subtract 2020 by the previous value.
    top_ceiling = 2020-one
    # Try to find values lower than the top ceiling.
    for two in l:
      if two < top_ceiling:
        mid_ceiling = top_ceiling - two
        for three in l:
          if three == mid_ceiling:
            writeAnswer2(one, two,three)
  print("End of second part.")

def main():
  part1()
  part2()

main()
