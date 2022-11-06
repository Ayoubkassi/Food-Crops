from IndicatorGroup import IndicatorGroup
from CommodityGroup import CommodityGroup
from FoodCropFactory import FoodCropFactory
from Measurement import Measurement
from Unit import Unit
import pandas as pd
import math 

class FoodCropsDataset(object):
	def __init__(self):
		pass 

	@staticmethod
	def load(datasetPath:str="./data/FeedGrains.csv"):
		indicators = {}
		#units = {}
		commodities = {}
		measurements = {}

		itterate = 1

		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():

			#skip none values
			if math.isnan(row[2]) :
				continue


			


			# create unit
			# for unit we have : 
			# 4,5,12,14,31-> price
			# 2,10,44 -> surface
			# 1,3,17,18 -> volume
			# 6,11,13,45, -> ratio
			# 7,8,9,41 -> weight
			# 15,16,46 -> count 

			if row[11] in (4,5,12,14,31):
				unit = FoodCropFactory.createPrice(row[11])
			elif row[11] in (2,10,44):
				unit = FoodCropFactory.createSurface(row[11])
			elif row[11] in (1,3,17,18):
				unit = FoodCropFactory.createVolume(row[11])
			elif row[11] in (6,11,13,45):
				unit = FoodCropFactory.createRatio(row[11])
			elif row[11] in (7,8,9,41):
				unit = FoodCropFactory.createWeight(1000,row[11])
			else :
				unit = FoodCropFactory.createCount("count",row[11])


			

			# create indicator 
			indicator = FoodCropFactory.createIndicator(row[9],row[14],row[15],row[6],IndicatorGroup(row[0]),unit)
			indicators[row[9]] = indicator

			# create commodity

			commodity = FoodCropFactory.createCommodity(CommodityGroup(row[2]),row[7],row[8])
			commodities[row[7]] = commodity


			# craete measurement

			measurement = FoodCropFactory.createMeasurement(row[13],row[18],row[16],row[17],commodity,indicator)
			measurements[index] = measurement

			# column_value = row[3]
			# print(column_value)
		

	
	def findMeasurements(commodityGroup:CommodityGroup=None ,indicatorGroup:IndicatorGroup=None ,geoGraphicalLocation:str=None ,unit:Unit=None):
		pass



FoodCropsDataset.load()




