from sys import argv

script, filename = argv

print("Let's open that file and load its content:")
file = open(filename)
print(file.read())