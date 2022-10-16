from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Measurement import Measurement
from Commodity import Commodity
from Indicator import Indicator
from Surface import Surface
from Volume import Volume
from Weight import Weight
from Price import Price
from Count import Count
from Ratio import Ratio
from Unit import Unit

class FoodCropFactory(object):


	@staticmethod
	def createVolume(id:int):
		return Volume(id)

	@staticmethod
	def createPrice(id:int):
		return Price(id)

	@staticmethod
	def createWeight(id:int,weight:float):
		return Weight(id,weight)

	@staticmethod
	def createSurface(id:int):
		return Surface(id)

	@staticmethod
	def createCount(id:int,what:str):
		return Price(id,what)

	@staticmethod
	def createRatio(id:int):
		return Ratio(id)

	@staticmethod
	def createCommodity(group:CommodityGroup,id:int,name:str):
		return Commodity(group,id,name)

	@staticmethod
	def createIndicator(id:int,frequency:int,freqDesc:str,geoLocation:str,indicatorGroup:IndicatorGroup,unit:Unit):
		return Indicator(id,frequency,freqDesc,geoLocation,indicatorGroup,unit)

	@staticmethod
	def createMeasurement(id:int,year:int,value:float,timeperiodId:int,timeperiodDescr:str,commodity:Commodity,indicator:Indicator):
		return Measurement(id,year,value,timeperiodId,timeperiodDescr,commodity,indicator)




# a = FoodCropFactory.createVolume(1)
# print(isinstance(a,Volume))





