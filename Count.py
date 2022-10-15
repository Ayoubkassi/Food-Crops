from Unit import Unit

class Count(Unit):
	def __init__(self,id:int , what:str, name:str = "Count"):
		self.id = id 
		self.name = name 
		self.__what = what
