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

import inspect

class Major(object):
	def __init__(self,name):
		self.name = name 


class Student(object):
	def __init__(self,name:str,age:int,major:Major):
		self.name = name
		self.age = age
		self.major = major


major1 = Major("CS")
major2 = Major("ME")

std1 = Student("Ayoub",18,major1)
std2 = Student("Yassine", 19,major1)
std3 = Student("Amine",17,major2)


students = {1 : std1 , 2: std2, 3 : std3 }

def find(name:str=None, age:int=None, major:Major=None):
	k = 0
	filtered_dict = students
	if name is not None :
		#filter of name 
		filtered_dict = (dict(filter(lambda x : x[1].name == name , students.items())))


	
	if age is not None :
		#filter of age
		filtered_dict = (dict(filter(lambda x : x[1].age == age , filtered_dict.items())))
		

				
	if major is not None :
		# filter of major
		filtered_dict = (dict(filter(lambda x : x[1].major == major , filtered_dict.items())))

	# for (key,val) in filtered_dict.items():
	# 	print(f'key -> {key} --- val -> {val.name}, {val.major.name}')

	return filtered_dict

#find(None,18,major1)






