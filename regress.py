from parse import parse

class data:
	def __init__(self,filename):
		self.data = parse(filename)
	def single_regression(y,x):
		meanX = 0
		total_X = 0
		meanY = 0
		total_Y = 0
		for instance in self.data:
			total_X += instance[x]
			total_Y += instance[y]
		meanX = float(total_X)/len(self.data)
		meanY = float(total_Y)/len(self.data)

		beta_num = 0
		beta_denom = 0

		for instance in self.data:
			Xi_meanX = instance[x] - meanX
			Yi_meanY = instance[y] - meanY
			beta_num += Xi_meanX*Yi_meanY
			beta_denom += Xi_meanX**2

		beta = beta_num/beta_denom
		constant = meanY - beta*meanX

		return constant, beta