from IndicatorGroup import IndicatorGroup
from CommodityGroup import CommodityGroup
from Unit import Unit
import pandas as pd

class FoodCropsDataset(object):
	def __init__(self):
		pass 

	@staticmethod
	def load(datasetPath:str="./data/FeedGrains.csv"):
		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():
			column_value = row[3]
			print(column_value)
		

	def findMeasurements(commodityGroup:CommodityGroup=None ,indicatorGroup:IndicatorGroup=None ,geoGraphicalLocation:str=None ,unit:Unit=None):
		pass



FoodCropsDataset.load()
