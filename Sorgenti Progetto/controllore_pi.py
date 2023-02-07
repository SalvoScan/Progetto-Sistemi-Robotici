class Controllore_PI:
	def __init__(self, kp, ki, sat):
		self.kp = kp
		self.ki = ki
		self.sat = sat

		self.g = 0.0
		self.windup = 0
	def evaluate(self, delta_t, errore):
		if(self.windup == 0):
			self.g = self.g + delta_t*errore
		out = self.kp*errore + self.ki*self.g
		if(out >= self.sat):
			out = self.sat
			self.windup = 1
		elif(out <= (-1)*self.sat):
			out = (-1)*self.sat
			self.windup = 1
		else:
			self.windup = 0
		return out
