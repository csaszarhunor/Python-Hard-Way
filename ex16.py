# http://learnpythonthehardway.org/book/ex16.html

# import argv
from sys import argv

# unpacks the argument variables into script
script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that hit CTRL + C (^C).")
print("If you don't want that hit RETURN.")

input("?")

# opens file from argument variable and stores it in a variable called target
print("Opening the file...")
target = open(filename, 'w')

# erase the content of the file
print("Truncating the file...")
target.truncate()

print("Now I'm going to ask you three lines.")

# asks user for three lines and store them in variables
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

# writes the lines asked above in the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# close file
print("And finally, we close it.")
target.close()
