from IndicatorGroup import IndicatorGroup

class Indicator(object):
	def __init__(self,id:str,frequency:int,frequencyDesc:str,geoLocation:str,indicatorGroup:IndicatorGroup):
		self.id = id 
		self.indicatorGroup = indicatorGroup
		self.__frequency = frequency
		self.__frequencyDesc = frequencyDesc
		self.__geoLocation = geoLocation