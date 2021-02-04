# ----------------------------------------------------------------------------
# Model Definition
# ----------------------------------------------------------------------------

# Initialize any variables here
t = 0

# Describe the test
testDescript = 'Reference Model M3'

# Define the causal model.
# Each random variable has the following fields:
# - Name
# - List of Parents
# - isObserved (Optional, default True)
# - Data Type (Optional, default 'Numeric')
model =    [('B', []),
			('A' , ['B']),
            ('D', ['A']),
			('C', ['B', 'D']),
			] 

# Structural Equation Model for data generation
varEquations = [
			    'B = noise()',
			    'A = coef() * B + noise()',
                'D = coef() * A*A + noise()',
			    'C = coef() * B + coef() * D + noise()',
                't = t + 1'
		        ]