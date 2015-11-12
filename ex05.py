# http://learnpythonthehardway.org/book/ex5.html

name = 'Hunor T. Csaszar'
age = 25 # not a lie
height = 176 # in cm
weight = 80 # in kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

cm_to_inch = height * 0.393700787
kg_to_pound = weight * 2.20462262

print("Let's talk about %s." % name)
print("He's %d cm (%d inches) tall." % (height, cm_to_inch))
print("He's %d kg (%d pounds) heavy." % (weight, kg_to_pound))
print("Actually that's quite heavy, considering his height.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s, depending on the coca leaves he chews." % teeth)

# this line, the tricky one, I should be careful with it.
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))


print("Different kind of datas: %r, %r, %r, %r" % (eyes, age, hair, cm_to_inch))
print("Different kinds of data: %f, %F, %e, %E, %g" % (age, age, age, age, age))
print(round(3.14159265359), round(3.9))