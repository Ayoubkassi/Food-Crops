# class Student(object):
# 	id = 0
# 	def __init__(self,name:str):
# 		self.name = name
# 		Student.id += 1
# 		self.id = Student.id



# std = Student("Ayoub")
# print(std.name)
# print(std.id)


# std = Student("Amine")
# print(std.name)
# print(std.id)

class Student(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age



std1 = Student("Ayoub",18)
std2 = Student("Yassine", 19)
std3 = Student("Amine",17)


names = {1 : std1 , 2: std2, 3 : std3}

print(dict(filter(lambda x : (x[1].name , x[1].age ) == ("Ayoub",19) , names.items())))



