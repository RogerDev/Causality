# ----------------------------------------------------------------------------
# SEM Definitions
#

testDescript = 'Diamond Pattern Test (5 level)'

varNames = ['R11',
			'R21', 'R22',
			'R31', 'R32', 'R33',
			'R41', 'R42',
			'R51',
			]

varEquations = [
				'R11 = logistic(0,1)',
				'R21 = R11 + logistic(0,1)',
				'R22 = R11 + logistic(0,1)',
				'R31 = R21 + logistic(0,1)',
				'R32 = .5 * R21 + .5 * R22 + logistic(0,1)',
				'R33 = R22 + logistic(0,1)',
				'R41 = .5 * R31 + .5 * R32 + logistic(0,1)',
				'R42 = .5 * R32 + .5 * R33 + logistic(0,1)',
				'R51 = .5 * R41 + .5 * R42 + logistic(0,1)',
				]
				
validation =  [
				('R11', []), ('R21', ['R11']), ('R22', ['R11']), ('R31', ['R21']), ('R32', ['R21','R22']), ('R33', ['R22']), 
				('R41', ['R31','R32']), ('R42', ['R32','R33']), ('R51', ['R41','R42']), 
				]
# -----------------------------------------------------------------------------