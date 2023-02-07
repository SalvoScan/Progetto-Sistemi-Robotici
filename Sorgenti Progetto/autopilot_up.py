from angle_controller import *
from x_controller import *
from z_controller import *
from multirotore import *

class Autopilot:
	def __init__(self):
		self.drone = Multirotore(1.0, 0.25, 7.0*(10.0**(-5)))
		self.angle_controller = Angle_Controller(4.0, 1.57, 2.0, 0.2, 15.0)
		self.x_controller = X_Controller(0.4, 2.0, 0.5, 0.2, 0.52)
		self.z_controller = Z_Controller(4.0, 2.0, 20.0, 40.0, 15.0)

		self.x_target = 0.0
		self.z_target = 0.0

		self.threshold = 0.2
		self.flag = 0		
			
		self.tmp = 0

		self.path = []
	def addPoint(self, x_target, z_target):
		self.path.append((x_target, z_target))
	
		if(self.tmp == 0):
			(x, z) = self.path[0]
			self.x_target = x
			self.z_target = z
			self.tmp = 1
	def showPath(self):
		print("Path Impostato:\n")
		for tmp in self.path:
			print("Point: " + str(tmp))
		print("------------------------------")
	def evaluate(self, delta_t):
		distance = math.sqrt(((self.x_target - self.drone.x)**2) + (self.z_target - self.drone.z)**2)
		if(self.flag == 0 and distance <= self.threshold):
			self.showPath()
			print("Punto " + str(self.path[0]) + " raggiunto")
			print("------------------------------")
			self.path.pop(0)
			if(len(self.path) == 0):
				print("Il Path e' stato completato con successo  :)")
				self.flag = 1
				return 
			self.showPath()
			(x, z) = self.path[0]
			self.x_target = x
			self.z_target = z
			print("Nuovo Target: " + str((x,z)))
			print("------------------------------")
			print("------------------------------")
		theta_target = (-1)*self.x_controller.evaluate(delta_t, self.x_target, self.drone.x, self.drone.vx)
		out_1 = self.angle_controller.evaluate(delta_t, theta_target, self.drone.theta, self.drone.omega)

		out_2 = self.z_controller.evaluate(delta_t, self.z_target, self.drone.z, self.drone.vz)

		f1 = out_2 - out_1
		f2 = out_2 + out_1

		self.drone.evaluate(delta_t, f1, f2)
