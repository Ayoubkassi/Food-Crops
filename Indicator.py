from IndicatorGroup import IndicatorGroup
from Unit import Unit
from Describable import Describable

class Indicator(Describable):
	def __init__(self,id:str,frequency:int,frequencyDesc:str,geoLocation:str,indicatorGroup:IndicatorGroup, unit:Unit):
		self.id = id 
		self.unit = unit
		self.indicatorGroup = indicatorGroup
		self.__frequency = frequency
		self.__frequencyDesc = frequencyDesc
		self.__geoLocation = geoLocation

	def get_geoLocation(self): 
		return self.__geoLocation

	def set_description(self,description):
		self.description = description

	def describe(self):
		return self.description+self.unit.describe() 
