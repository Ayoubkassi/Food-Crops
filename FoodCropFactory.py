from CommodityGroup import CommodityGroup
from Commodity import Commodity
from Volume import Volume
from Price import Price
from Weight import Weight
from Surface import Surface
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



# a = FoodCropFactory.createVolume(1)
# print(isinstance(a,Volume))





