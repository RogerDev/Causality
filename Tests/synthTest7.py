# ----------------------------------------------------------------------------
# 
# SEM Definitions

varNames = ['X', 'Y']

varEquations = ['X= data()',
				'Y = noise() + coef() * X',
				]
				
validation =  [('Y', ['X']),
				]

# -----------------------------------------------------------------------------
