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
  for val in sorted(d.keys):
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

# This part covers the second half of the solution.
def part2():
  # We will use the same dictionary, but will try matching three values.
  d = fillDictionary(__location__)
  print("Second part")

def main():
  part1()
  part2()

main()
