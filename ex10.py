# http://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# endless loop, be careful:
#while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#	    print("%s\r" % i,)

print("\a this was \\a and this is \\b \b word")
print("next is \\f\f\n and \\r \r something \n\t*")
print("vertical tab \\v\vdid it work?")