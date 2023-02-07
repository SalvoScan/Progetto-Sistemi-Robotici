class Controllore_P:
	def __init__(self, kp, sat):
		self.kp = kp
		self.sat = sat
	def evaluate(self, errore):
		out = self.kp*errore
		if(out >= self.sat):
			out = self.sat
		elif(out <= (-1)*self.sat):
			out = (-1)*self.sat
		else:
			out = out
		return out
