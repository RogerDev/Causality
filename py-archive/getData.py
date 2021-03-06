inputFileName = '..\data\synthData4.csv'
#inputFileName = '..\data\experiment1.csv'
import numpy as np
import random


class DataReader():
	def __init__(self, input = inputFileName, limit=100000000):
		self.limit = limit
		self.varData = {}
		self.vars = []
		self.varIndex = {}
		self.sampleCount = 0
		f = open(input, 'r')
		lines = f.readlines()
		varNames = lines[0]
		data = lines[1:]
		tokens = varNames[:-1].split(',')
		for varName in tokens:
			self.vars.append(varName)
			self.varData[varName] = []
			self.varIndex[varName] = len(self.vars) - 1
		if len(data) < limit:
			print('*** Number of datapoints is less than requested limit (', len(data), ' vs ', self.limit, ') -- Using data length')
		# If limit is less than length of data, select a random starting point that will produce enough (i.e. limit) datapoints
		if len(data) > limit:
			datalen = len(lines)
			dataslack = datalen - limit
			datastart = random.choice(range(dataslack))
			data = data[datastart:]
		for line in data:
			if line[-1] == '\n':
				line = line[:-1]
			tokens = line.split(',')
			for i in range(len(self.vars)):
				try:
					val = float(tokens[i])
				except:
					val = 0
				self.varData[self.vars[i]].append(val)
		self.sampleCount = len(self.varData[self.vars[0]])
		np.random.shuffle(self.vars)
		return
		
	def getSeriesNames(self):
		return self.vars[:]
		
	def getSeries(self, varName):
		return self.varData[varName][:self.limit]
		
	def getIndexForSeries(self, varName):
		return self.varIndex[varName]
			
	

				
		