from CommodityGroup import CommodityGroup

class Commodity(object):
	def __init__(self,group:CommodityGroup, id:int,name:str):
		self.id     = id 
		self.group  = group
		self.__name = name


