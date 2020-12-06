import csv
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
  #Part I: Normalize information
  # Open file to read disorganized and incomplete values
  f = open(os.path.join(__location__, 'puzzle_input.txt'), "r")
  # Open file to write values into csv format
  csv_to_write = open(os.path.join(__location__, 'data.csv'), "w", newline='',
    encoding='utf-8')
  # Dictionary structure with easily comparable defaults
  fields = { 'byr': False, 'iyr': False, 'eyr': False, 'hgt': False,
    'hcl': False, 'ecl': False, 'pid': False, 'cid': False}
  # csv DictWriter for the normalization of data into a proper csv file.
  csv_writer = csv.DictWriter(csv_to_write, fieldnames=fields)
  # Writes the headers for when rereading the values of the new file.
  csv_writer.writeheader()
  # EOF is necessary or last item isn't read.
  # First, go to end of file.
  f.seek(0, os.SEEK_END)
  # Save location of EOF.
  eof = f.tell()
  # Reset position to the beginning of the file.
  f.seek(0)
  # Navigate lines in disorganized file.
  for line in f:
    # If we reach a lone newline, write collected values to csv file.
    # A lone newline separates cohesive items from each other.
    # EOF wraps up the write of the last element.
    if line == '\n' or line == '':
      # Incomplete values written as False for an easily testable value.
      csv_writer.writerow(fields)
      # Reset dictionary for next item validation
      fields = { 'byr': False, 'iyr': False, 'eyr': False, 'hgt': False,
        'hcl': False, 'ecl': False, 'pid': False, 'cid': False }
      continue
    # Extract relevant information from each line.
    # All lines must be tested for each field.
    if line.__contains__('byr'):
      fields['byr'] = re.search(r'byr:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('iyr'):
      fields['iyr'] = re.search(r'iyr:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('eyr'):
      fields['eyr'] = re.search(r'eyr:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('hgt'):
      fields['hgt'] = re.search(r'hgt:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('hcl'):
      fields['hcl'] = re.search(r'hcl:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('ecl'):
      fields['ecl'] = re.search(r'ecl:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('pid'):
      fields['pid'] = re.search(r'pid:(#|\w+|\d+)*', line).group()[4:]
    if line.__contains__('cid'):
      fields['cid'] = re.search(r'cid:(#|\w+|\d+)*', line).group()[4:]
  # Close both files which are no longer needed.
  f.close()
  csv_to_write.close()
  # Part II: Process Normalized Data
  # Open csv file
  csv_to_read = open(os.path.join(__location__, 'data.csv'), "r")
  # Configure csv reader as a DictReader
  csv_reader = csv.DictReader(csv_to_read)
  valid = 0
  index = 0
  for index, row in enumerate(csv_reader):
    if index == 0: continue
    if (row['byr'] != 'False' and row['iyr'] != 'False' and row['eyr']
      != 'False' and row['hgt'] != 'False' and row['hcl'] != 'False' and
      row['ecl'] != 'False' and row['pid'] != 'False'):
        valid += 1
  csv_to_read.close()
  print("The number of valid passports is: " + str(valid))


main()
