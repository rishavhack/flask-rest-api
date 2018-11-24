know_people = ['Rishav','abc','Mary']
person = raw_input("Enter name")

if person in know_people:
	print "You know {}!".format(person)
else:
	print "You don't {}!".format(person)