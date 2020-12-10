from array import *
import os

__location__ = os.path.realpath(
  os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # One list for tracking answers within a same group
  group_answers = []
  # One list for tracking all least occurrences from all groups
  answer_list = []
  # Get file contents
  with open(os.path.join(__location__, 'puzzle_input.txt'), "r") as f:
    # Traverse line by line
    for line in f:
      # Check if the current char is in answers. If not, add to list.
      for c in line:
        if not c in group_answers and c != '\n':
          group_answers.append(c)
      # If you hit a singular newline, a new group is next.
      # At this point, flush all values into the totals list.
      if line == '\n':
        for i in group_answers:
          answer_list.append(i)
        group_answers = []
    # For some reason at the very last newline, it simply exits loop.
    # Due to this, one last run executes to flush the list into totals.
    if group_answers != []:
      for i in group_answers:
        answer_list.append(i)
  print("The total of answers is", len(answer_list))

main()
