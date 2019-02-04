name = 'Gray Ponder'
age = 27
height = 65 # in inches
weight = 170 # lbs (in pound)
gender = 'Male'
eye_color = 'Black'
teeth_color = 'White'
hair_color = 'Black'
inches_to_cm = 2.54 * height
pound_to_kg = 0.453592 * weight


print "Let's talk about %s." % name
print "%s is a %d year %s." % (name, age, gender)
print "He is %d inches in height (%d cm)." % (height, inches_to_cm)
print "He weighs %d lbs (%d kg)." % (weight, pound_to_kg)
print "He has %s eyes %s hairs and %s teeth" %(eye_color, hair_color, teeth_color)
