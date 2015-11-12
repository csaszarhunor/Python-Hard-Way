# http://learnpythonthehardway.org/book/ex19.html

# wefine a function called cheese_and_crackers which takes two arguments


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print out strings using digit placeholders to insert the arguments
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
	
# print an introduction line then call the function cheese_and_crackers with two numeric arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# print an introduction line
print("OR, we can use variables from our script:")
# creates two variables with numeric values and use them as arguments to call the function cheese_and_crackers
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# after an intro line use the function cheese_and_crackers with additions of numbers as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# after an intro line use the function cheese_and_crackers with additions of variables and numbers as arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)