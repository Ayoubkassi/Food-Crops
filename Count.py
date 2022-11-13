from Unit import Unit
import pandas as pd


class Count(Unit):
	def __init__(self,id:int , what:str, name:str = "Count"):
		super().__init__(id,str)
		self.__what = what

	def describe(self):
		datasetPath = "./data/FeedGrains.csv"
		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():
			if index == self.id :
				return row[12]
