import numpy as np

def standardize(series):
	# Recenter at zero mean, and rescale to unit variance
	a = np.array(series)
	mu = a.mean()
	aCentered = a - mu
	sigma = aCentered.std()
	#print ('sigma= ', sigma)
	aScaled = aCentered / sigma
	#print('aScaled = ', aScaled.mean(), aScaled.std())
	#print('ac=', aScaled)
	return aScaled