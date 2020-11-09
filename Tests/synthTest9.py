# ----------------------------------------------------------------------------
# Simplified version of Test1
# SEM Definitions

varNames = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I']

varEquations = [
		'A=  1.0 + logistic(940.469,0.913)',
		'B =  1.0 + logistic(943.831,1.602)',
		'C = 1.0 + logistic(986.48,1.006)',
		'D = 1.0 + logistic(1029.192,0.929)',
		'E = -10.678 * A + -10.642 * B + 10.348 * C + 10.602 * D + logistic(933.052,80)',
		'F = 14.458 * E + logistic(1028.798,300.0)',
		'G = -10.064 * F + logistic(986.545,8000)',
		'H = 12.26 * F + logistic(1028.672,8000)',
		'I = 11.69 * F + logistic(1013.819,8000)',
				]
				
validation =  [('A', []), ('B', []), ('C', []), ('D', []), ('E', ['A','B','C','D']),
				('F', ['E']), ('G', ['F']), ('H',['F']), ('I', ['F']), 
				]

# -----------------------------------------------------------------------------