from CommodityGroup import CommodityGroup

class Commodity(object):
	def __init__(self,id:int,name:str,group:CommodityGroup):
		self.id     = id 
		self.group  = group
		self.__name = name


