# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. 
# Here's what you should do for each type:

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" 
# If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." 
# If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" 
# If the list has fewer than 10 values print "Short list."


def filter(input):
	if int == type(input):
		if input >= 100:
			print "That's a big number!"
		else: 
			print "That's a small number"

	elif str == type(input):
		if len(input) >= 50:
			print "Long sentence."
		else:
			print "Short sentence."

	elif list == type(input):
		if len(input) >= 10:
			print "Big list!"
		else: 
			print "Short list."

filter(5)
filter(109)
filter("fiten sdklfjsdfsjdfjsdk jfslakdjflksajfjsadkfjsld jflkdsjfksjdfkjsdklfjsdkljfskdjfkdsf")
filter("dfdfdf")
filter([0, 10])
filter([1,2,3,4,5,6,7,8,9,10,11])