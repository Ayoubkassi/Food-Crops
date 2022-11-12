from Unit import Unit

class Weight(Unit):
	def __init__(self,id :int ,multiplier:float, name:str = "Weight"):
		super().__init__(id,str)
		self.__multiplier = multiplier



