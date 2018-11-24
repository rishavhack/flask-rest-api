lottery_player_dict = {
	'name':'Rolf',
	'numbers':(5,9,12,3,1,21)
}

class LotterPlayer():
	def __init__(self):
		self.name = "Rolf"
		self.numbers = (5,9,12,3,1,21)


	def total(self):
		return sum(self.numbers)

player = LotterPlayer()
print player.name
print player.total()
player_one = LotterPlayer()
print player == player_one


class Student:
	"""docstring for Student"""
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)
    
    @staticmethod #if you are not passing self.    Now we can call like className.go_to_school1()
	def go_to_school1():
		print "I'm going to school"

	@classmethod
	def go_to_school(cls):
		print "I'm going to school"
		print "I'm a {}".format(cls)

anna = Student("Rishav","DAV")
anna.marks.append(88)
anna.marks.append(88)
anna.marks.append(88)
print anna.marks
print anna.average()
print Student.go_to_school1() #staticmethod
print anna.go_to_school()
