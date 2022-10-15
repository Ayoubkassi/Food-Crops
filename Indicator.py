from IndicatorGroup import IndicatorGroup
from Unit import Unit

class Indicator(object):
	def __init__(self,id:str,frequency:int,frequencyDesc:str,geoLocation:str,indicatorGroup:IndicatorGroup, unit:Unit):
		self.id = id 
		self.unit = unit
		self.indicatorGroup = indicatorGroup
		self.__frequency = frequency
		self.__frequencyDesc = frequencyDesc
		self.__geoLocation = geoLocation