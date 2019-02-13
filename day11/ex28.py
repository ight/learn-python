print True and True
print "True and True expected: True"

print False and True
print "False and True expected: False"

print 1 == 1 and 2 == 1
print "1 == 1 and 2 == 1 expected: False"

print "test" == "test"
print " \"test\" == \"test\" expected: True"

print 1 == 1 or 2 != 1
print "1 == 1 or 2 != 1 expected: True"

print True and 1 == 1
print "True and 1 == 1 expected: True"

print False and 0 != 0
print "False and 0 != 0 expected: False"

print True or 1 == 1
print "True or 1 == 1 expected: True"

print "test" == "testing"
print " \"test\" == \"testing\" expected: False"

print 1 != 0 and 2 == 1
print "1 != 0 and 2 == 1 expected: False"

print "test" != "testing"
print " \"test\" != \"testing\" expected: True"

print "test" == 1
print "\"test\" == 1 expected: False"

print not (True and False)
print "not (True and False) expected: True"

print not (10 == 1 or 0 != 1)
print "not (1 == 1 or 0 != 1) expected: False"

print not (10 == 1 or 1000 == 1000)
print "not (10 == 1 or 1000 == 1000) expected: False"

print not (1 != 10 or 3 == 4)
print "not (1 != 10 or 3 == 4) expected: True"

print not ("testing" == "testing" and "Zed" == "Cool Guy")
print "not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\") expected: True"

print 1 == 1 and not ("testing" == 1 or 1 == 0)
print "1 == 1 and not (\"testing\" == 1 or 1 == 0) expected: True"

print "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print "\"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3) expected: False"

print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print "3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\") expected: False"