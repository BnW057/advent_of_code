import os
import re
from typing import Counter

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # Count variable for iteration
  count1 = 0
  count2 = 0
  # Open file to read values
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  for line in f:
    # Use regular expressions to extract values for the formula
    # First integer easy.
    lower = int(re.search(r'\d+', line).group())
    # since includes the hyphen as a negative sign, absolute value used.
    upper = abs(int(re.search(r'(?:-)\d+', line).group()))
    # Isolate the char followed by colon, then isolate char.
    target = re.search(r'\w(?::)', line).group()[0]
    # Isolate string that follow colon, then isolate string.
    sample = str(re.search(r'(?:: )\w+', line).group())[2:]
    # For the second part:
    # Extract the value pointed to by the first provided index.
    first = sample[lower-1]
    # Extract the value pointed to by the second provided index.
    second = sample[upper-1]
    # Test if the target is within the range inside the sample. Count.
    if sample.count(target) >= lower and sample.count(target) <= upper:
      count1+=1
    # Might as well ensure the sample contains the value to be tested.
    verify = sample.count(target)>0
    if verify:
      # This boolean is a toggle. If toggles once only, count.
      once = False
      if first == target:
        once = not(once)
      if second == target:
        once = not(once)
      if once:
        count2+=1
  f.close()
  print("First part: The total of correct passwords is " + str(count1))
  print("Second part: The total is: " + str(count2))

main()
