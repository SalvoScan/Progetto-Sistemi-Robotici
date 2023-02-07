import math

class Multirotore:
	def __init__(self, massa, lunghezza, attrito):
		self.massa = massa
		self.lunghezza = lunghezza
		self.attrito = attrito
		self.inerzia = (1/12.0)*self.massa*4.0*(self.lunghezza**2)
		self.grv = 9.81
		
		self.theta = 0.0
		self.omega = 0.0

		self.x = 0.0
		self.vx = 0.0
	
		self.z = 0.0
		self.vz = 0.0
	def evaluate(self, delta_t, f1, f2):
		theta_tmp = self.theta + delta_t*self.omega
		omega_tmp = self.omega + delta_t*self.lunghezza/self.inerzia*(f2 - f1)

		x_tmp = self.x + delta_t*self.vx
		vx_tmp = self.vx*(1 - delta_t*self.attrito/self.massa) + delta_t*(math.sin(-self.theta))*(f1 + f2)

		z_tmp = self.z + delta_t*self.vz
		vz_tmp = self.vz*(1 - delta_t*self.attrito/self.massa) - delta_t*self.grv + delta_t/self.massa*(math.cos(self.theta))*(f1 + f2)	
	
		self.theta = theta_tmp
		self.omega = omega_tmp

		self.x = x_tmp
		self.vx = vx_tmp

		self.z = z_tmp
		self.vz = vz_tmp







