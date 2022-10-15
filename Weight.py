from Unit import Unit

class Weight(Unit):
	def __init__(self,id :int , name:str = "Weight",multiplier:float):
		self.id = id 
		self.name = name 
		self.__multiplier = multiplier

