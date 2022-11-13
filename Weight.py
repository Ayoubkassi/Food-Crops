from Unit import Unit
import pandas as pd


class Weight(Unit):
	def __init__(self,id :int ,multiplier:float, name:str = "Weight"):
		super().__init__(id,str)
		self.__multiplier = multiplier

	def describe(self):
		datasetPath = "./data/FeedGrains.csv"
		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():
			if index == self.id :
				return row[12]



