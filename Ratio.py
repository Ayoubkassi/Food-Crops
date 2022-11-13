from Unit import Unit

class Ratio(Unit):
	def __init__(self,id:int , name:str = "Ratio"):
		super().__init__(id,str)
		 
	def describe(self):
		return self.name 