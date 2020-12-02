from os import error, system
import os

def main():
  # Initialize variables for later use.
  d = {};
  result = False
  __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
  # Open file with values
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  # Map values in file into a dictionary
  for line in f:
    d[line] = True;
  # Close file after reading values
  f.close()
  # Try to find 2020 sum pair in dictionary
  for val in sorted(d):
    # Try to use difference of value as key. If True, match is found.
    try:
      result = str(str(2020-int(val)) + "\n") in d;
    except error:
      print("An error occurred.")
    if result == True:
      f = open(os.path.join(__location__, 'answer1.txt'), "w")
      f.write("First Value: " + val)
      f.write("Second value: " + str(2020-int(val)) + "\n")
      f.write("Multipying both:" + str(int(val) * (2020-int(val))))
      f.close()
      return
  print("End of execution.")

main()
