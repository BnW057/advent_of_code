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
  # Navigate lines in disorganized file.
  for count, line in enumerate(f):
    count += 1
    # If we reach a lone newline, write collected values to csv file.
    # A lone newline separates cohesive items from each other.
    # EOF wraps up the write of the last element.
    if line == '\n' or line == b'':
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
  # One last write for the item stored in buffer.
  csv_writer.writerow(fields)
  # Close both files which are no longer needed.
  f.close()
  csv_to_write.close()

  # Part II: Process Normalized Data
  # Open csv file
  csv_to_read = open(os.path.join(__location__, 'data.csv'), "r")
  # Configure csv reader as a DictReader
  csv_reader = csv.DictReader(csv_to_read)
  valid = 0
  legit = 0
  eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
  for row in csv_reader:
    if (row['byr'] != 'False' and row['iyr'] != 'False' and row['eyr']
      != 'False' and row['hgt'] != 'False' and row['hcl'] != 'False' and
      row['ecl'] != 'False' and row['pid'] != 'False'):
      valid += 1
      # Checking for values to actually comply with some limitations.
      if (len(row['byr']) == 4 and 1920 <= int(row['byr']) <= 2002
        and len(row['iyr']) == 4 and 2010 <= int(row['iyr']) <= 2020
        and len(row['eyr']) == 4 and 2020 <= int(row['eyr']) <= 2030
        and (str(row['hgt']).__contains__("in")
          and 59 <= int(re.search(r'\d+', row['hgt']).group()) <= 76 or
        (str(row['hgt']).__contains__("cm")
          and 150 <= int(re.search(r'\d+', row['hgt']).group()) <= 193))
        and (re.search(r'#[0-9a-f]{6}', row['hcl']) != None)
        and str(row['ecl']) in eye_colors and
        re.search(r'[0-9]{9}', row['pid']) != None):
        legit += 1
  csv_to_read.close()
  # Part one
  print("The number of valid passports is: " + str(valid))
  print("With additional validation checks, the number is: " + str(legit))


main()
