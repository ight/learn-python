# function with not fixed parameter count
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)


# function with fixed parameter count
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)


# function with one argument
def print_one(arg1):
  print "arg1: %r" % arg1

# function with ni arguments
def print_none():
  print "'I got nothing'."


# calling functions
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()