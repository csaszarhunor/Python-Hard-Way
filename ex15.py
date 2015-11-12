# http://learnpythonthehardway.org/book/ex15.html

# imports argument variable
from sys import argv

# unpack argv into the given variables
script, filename = argv

# opens file and store in variable txt
txt = open(filename)

print("Here's your file %r: " % filename)
# reads the opened file
print(txt.read())

txt = close(filename)

# ask the user the file name given before and store it in another variable
#print("Type the filename again:")
#file_again = input("> ")

# opens the file
#txt_again = open(file_again)

# read the file and prints its content in the console
#print(txt_again.read())

#txt_again = close(file_again)