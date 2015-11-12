# http://learnpythonthehardway.org/book/ex6.html

# a variable called x equals a string containing a decimal placeholder
# after the string is given the decimal value for the placeholder
x = "There are %d types of peaople." % 10
# a variable which contains a string value
binary = "binary"
# a variable which contains a string value
do_not = "don't"
# a variable called y equals a string containing two string placeholders
# after the string is given the strings for the placeholders in parenthesis
y = "Those who know %s and those who %s." % (binary, do_not)

# prints out the content of the variable x
print(x)
# prints out the content of the variable y
print(y)

# prints out a string with a repr() placeholder which refers to the variable x
print("I said: %r." % x)
# prints out a string with a repr() placeholder which refers to the variable y
print("I also said: '%s'." % y)

# variable contains a boolean value
hilarious = False
# variable contains a string with a %r placeholder
joke_evaluation = "Isn't that joke so funny?! %r"

# prints a variable containing a string with a placeholder in it which will call the next variable
print(joke_evaluation % hilarious)

# variable with a string
w = "This is the left side of..."
# variable with a string
e = "a string with a right side."

# prints the sum of two variables containing strings
print(w + e)
