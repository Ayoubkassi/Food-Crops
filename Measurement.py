from Commodity import Commodity
from Indicator import Indicator

class Measurement(object):
	"""docstring for Measurement"""
	id = 1
	def __init__(self,year:int,value:float,timeperiodId:int,timeperiodDescr:str,commodity:Commodity,indicator:Indicator):
		self.__year = year
		self.__value = value
		self.__timeperiodId = timeperiodId
		self.__timeperiodDescr = timeperiodDescr
		self.commidity = commodity
		self.indicator = indicator
		# static generated id 
		Measurement.id += 1
		self.id = Measurement.id 




		