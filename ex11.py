# http://learnpythonthehardway.org/book/ex11.html

print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

name = input("What is your name?")
origin = input("Where do you come from?")
destination = input("Where are you going?")

print("Welcome %r of %r,\nHave a safe journey towards %r!" % (name, origin, destination))
print()
print("Allow me to do some math for you:")
number_one = int(input("Give me your first number: "))
number_two = int(input("Give me your second number: "))
print()
print("So, the sum of the given numbers is %r and the multiplication \
of them is %r" % ((number_one + number_two), (number_one * number_two)))