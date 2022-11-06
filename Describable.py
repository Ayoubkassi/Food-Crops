from abc import ABC , abstractmethod

class Describable(ABC):
	def __init__(self):
		pass 

	@abstractmethod
	def describe(self):
		pass


