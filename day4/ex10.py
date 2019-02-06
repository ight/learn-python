# Note: """ some multiline text with escape charater """
# """ allow user to have multiple line without using \n

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll da list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# This was fun code prints like /-|\| looks cool in 
# terminal.
while True:
  for i in ["/","- ","|","\\","|"]:
    print "%s\r" % i,