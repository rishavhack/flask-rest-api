class Student:
	"""docstring for Student"""
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	def friend(self,friend_name):
		return Student(friend_name,self.school)

	@classmethod
	def friend(self,friend_name,salary):
		return Student(friend_name,self.school,salary)

anna = Student("Rishav","Oxford")

friend = anna.friend("Greg")
print friend.name
print friend.school


#class WorkingStudent(Student):
#	anna = WorkingStudent("Rishav","Oxford")
#
#	friend = anna.friend("Greg")
#	print friend.name
#	print friend.school
#This will give same result that above one will give		

class WorkingStudent(Student):
	def __init__(self,name,school,salary):
		super().__init__(name,school)
		self.salary = salary

anna1 = WorkingStudent("Saumya","Oxford",20.0)
print anna1.salary

#This below work when  @classmethod we appplied
friend = WorkingStudent.friend(anna,"grf",192)
print friend.name
print friend.school
print friend.salary