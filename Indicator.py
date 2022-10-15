class Indicator(object):
	def __init__(self,id:str,frequency:int,frequencyDesc:str,geoLocation:str):
		self.id = id 
		self.__frequency = frequency
		self.__frequencyDesc = frequencyDesc
		self.__geoLocation = geoLocation