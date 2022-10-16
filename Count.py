from Unit import Unit

class Count(Unit):
	def __init__(self,id:int , what:str, name:str = "Count"):
		super().__init__(id,str)
		self.__what = what
