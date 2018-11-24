my_Variable = "Hello"

for chara in my_Variable:
	print chara

my_list = [1,2,3,4,5,8]
for num in my_list:
	print num**2

user_wants = True
while user_wants == True:
	print 10
	user_input = raw_input("Should we print again ? (y/n)")
	if user_input == 'n':
		user_wants = False