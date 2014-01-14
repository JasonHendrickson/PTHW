#Learn Python the Hard Way
#Example 5

#Initiate variables
name = 'Zed A. Shaw'
age = 35 	#not a lie
height = 74 	#inches
weight = 180   #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_europe = height * 2.54/100
weight_in_europe = weight / 2.2

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "In Europe, Zed would weight %f kilos and stand %f meters tall" % (weight_in_europe, height_in_europe)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
