# http://learnpythonthehardway.org/book/ex36.html

import ex36v as v
from sys import exit


def start():
	answer = v.intro()
	if "blue" in answer:
		blue()
	elif "red" in answer:
		red()
	else:
		nopill()

		
def dead():
	answer = input("You may not like the answer. Want to start again?")
	while answer not in "nope yes yep":
		answer = input("I can take only 'yes' or 'no'. ")
	if answer in "yes yep":
		start()
	if answer in "nope":
		exit(0)


def red():
	answer = v.red_pill()
	while answer not in '01':
		answer = input("I can only take '0' or '1'.")
	if "0" in answer:
		print(v.zero)
		dead()
	elif "1" in answer:
		print(v.one)
		dead()
		
		
def blue():
	print(v.blue_pill)
	dead()

	
def nopill():
	print(v.no_pill)
	dead()
	

start()