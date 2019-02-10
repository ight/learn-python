from sys import argv

srcipt, input_file = argv

def print_all(f):
  print f.read()

def rewind(f):
  # this sets the file postion to starting of the file.
  f.seek(0)

def print_a_line(line_count, f):
  # f.tell the current file postion, file are read char by char. so
  # if return value is 30 that is 30 char from 0 or starting of the
  # file.
  current_file_postion = f.tell()
  print "Tell me the current_file_postion %r" % current_file_postion
  print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines one by one:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)