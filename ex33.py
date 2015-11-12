# http://learnpythonthehardway.org/book/ex33.html


def list_creator(incrementor):
	i = 0
	numbers = []
	top = 15
	
	while not(incrementor.isdigit() and int(incrementor) > 0):
		print("Enter a positive integer.")
	
	while i < top:
		print("At the top i is %d" % i)
		numbers.append(i)
		
		i += int(incrementor)
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)
		
	print("The numbers: ")

	for num in numbers:
		print(num)
			

print("I am going to create a list of integers for you starting with 0 to 15.")
print("Please enter a positive integer to determine how much will be the distance between two numbers.")
list_creator(input("> "))
