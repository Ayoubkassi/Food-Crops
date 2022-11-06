class Student(object):
	id = 0
	def __init__(self,name:str):
		self.name = name
		Student.id += 1
		self.id = Student.id



std = Student("Ayoub")
print(std.name)
print(std.id)


std = Student("Amine")
print(std.name)
print(std.id)