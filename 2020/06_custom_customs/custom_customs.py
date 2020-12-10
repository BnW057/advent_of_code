from array import *
import os

__location__ = os.path.realpath(
  os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  # One list for tracking answers within a same group
  group_answers = []
  # One list for tracking all least occurrences from all groups
  answer_list = []
  # Lists for the second part of the problem.
  temp_list = []
  corrected_totals = []
  group_member_total = 0
  # Get file contents
  with open(os.path.join(__location__, 'puzzle_input.txt'), "r") as f:
    # Traverse line by line
    for line in f:
      # If you hit a singular newline, a new group is next.
      # At this point, flush all values into the totals list.
      if line == '\n':
        for i in group_answers:
          answer_list.append(i)
        group_answers = []
        # Check if the total appearances of a char equals group total
        temp_list = sorted(temp_list)
        # List to isolate unique shared answers per group
        shared_answers = []
        for j in temp_list:
          # If pass validation, only add letter once.
          if (temp_list.count(j) == group_member_total and
          not j in shared_answers):
            shared_answers.append(j)
        if shared_answers != []:
          for a in shared_answers:
            corrected_totals.append(a)
        group_member_total = 0
        temp_list = []
        continue
      # Check if the current char is in answers. If not, add to list.
      for c in line:
        if not c in group_answers and c != '\n':
          group_answers.append(c)
        if c != '\n':
          temp_list.append(c)
      group_member_total += 1
    # For some reason at the very last newline, it simply exits loop.
    # Due to this, one last run executes to flush the list into totals.
    # The same happens with the solution of the second half.
    if group_answers != []:
      for i in group_answers:
        answer_list.append(i)
    if temp_list != []:
      # List to isolate unique shared answers per group
      shared_answers = []
      for j in temp_list:
        # If pass validation, only add letter once.
        if (temp_list.count(j) == group_member_total and
        not j in shared_answers):
          shared_answers.append(j)
      if shared_answers != []:
        for a in shared_answers:
            corrected_totals.append(a)

  print("The total of answers for the first part is", len(answer_list))
  print("The total of answers for the second part is", len(corrected_totals))

main()
