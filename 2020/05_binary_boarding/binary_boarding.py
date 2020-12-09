from array import *
from io import UnsupportedOperation
import os

__location__ = os.path.realpath(
  os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  max_rows = pow(2,7)
  max_columns = pow(2,3)
  # Populate 2D array with possible spots, default to False.
  seats = [[]]
  for row in range(0, max_rows):
    seats.append([])
    for column in range(0, max_columns):
      seats[row].append(False)
  # Variables for handling 2D array
  row = col = 0

  # Get data from file
  with open(os.path.join(__location__, 'puzzle_input.txt'), "r") as f:
    # Traverse every line
    for line in f:
      lower_row = 0
      upper_row = max_rows
      lower_col = 0
      upper_col = max_columns
      # Traverse every character and approximate correct seat
      for c in line:
        if c == "F":
          upper_row = (upper_row + lower_row) / 2
        elif c == "B":
          lower_row =lower_row + (upper_row - lower_row) / 2
        elif c == "L":
          upper_col = (upper_col + lower_col) / 2
        elif c == "R":
          lower_col = lower_col + (upper_col - lower_col) / 2
      # Choose the correct coordinates based on last choice
      if line[6] == "F":
        row = lower_row
      else: row = upper_row - 1
      if line[len(line)-1] == "L":
        col = lower_col
      else: col = upper_col - 1
      row = int(row)
      col = int(col)
      seats[row][col] = True

    # Find highest seatID

    highest = 0
    for i in range(len(seats)):
      for j in range(len(seats[i])):
        if seats[i][j] == True:
          seatID = i * 8 + j
          if seatID > highest:
            highest = seatID
    print(highest)

main()
