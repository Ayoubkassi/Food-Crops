from abc import ABC

class Unit(ABC):
	def __init__(self,id:int,name:str):
		self.id   = id 
		self.name = name
