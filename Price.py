from Unit import Unit
import pandas as pd


class Price(Unit):
	def __init__(self,id:int , name:str="Price"):
		super().__init__(id,str)

	def describe(self):
		datasetPath = "./data/FeedGrains.csv"
		dataframe = pd.read_csv(datasetPath)
		for index, row in dataframe.iterrows():
			if index == self.id :
				return row[12]
		


