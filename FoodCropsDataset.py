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
		units = {}
		commodities = {}
		measurements = {}

		itterate = 1

		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():
			print(index)

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

			if row[11] in units:
				unit = units[row[11]]
			else :

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

				units[row[11]] = unit


			# create indicator 
			#check for existence before create
			if row[9] in indicators : 
				indicator = indicators[row[9]]
			else :
			    indicator = FoodCropFactory.createIndicator(row[9],row[14],row[15],row[6].strip(),IndicatorGroup(row[0]),unit)
			    #add desription
			    indicator.description = row[10]
			    indicators[row[9]] = indicator

			# print(indicator.get_geoLocation())
			# if(indicator.get_geoLocation() == "World"):
			# 	break

			# create commodity
			#check for existence before
			if row[7] in commodities:
				commodity = commodities[row[7]]
			else :
			    commodity = FoodCropFactory.createCommodity(CommodityGroup(row[2]),row[7],row[8])
			    commodities[row[7]] = commodity


			# craete measurement

			measurement = FoodCropFactory.createMeasurement(row[13],row[18],row[16],row[17],commodity,indicator)
			measurements[index] = measurement


		return measurements

			# column_value = row[3]
			# print(column_value)
		
	
	def findMeasurements(commodityGroup:CommodityGroup=None ,indicatorGroup:IndicatorGroup=None ,geoGraphicalLocation:str=None ,unit:Unit=None):
		filtered_measurements = FoodCropsDataset.load()
		if commodityGroup is not None:
			filtered_measurements = (dict(filter(lambda x : x[1].commodity.group == commodityGroup, filtered_measurements.items()))) 

		if indicatorGroup is not None :
			filtered_measurements = (dict(filter(lambda x : x[1].indicator.indicatorGroup == indicatorGroup, filtered_measurements.items()))) 

		if geoGraphicalLocation is not None :
			filtered_measurements = (dict(filter(lambda x : x[1].indicator.get_geoLocation() == geoGraphicalLocation, filtered_measurements.items()))) 

		if unit is not None :
			filtered_measurements = (dict(filter(lambda x : x[1].indicator.unit == unit, filtered_measurements.items()))) 

		return filtered_measurements


print(f' data size is : {len(FoodCropsDataset.findMeasurements(None,None,"World",None))}')





