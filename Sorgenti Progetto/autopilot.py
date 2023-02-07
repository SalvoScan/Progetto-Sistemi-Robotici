from angle_controller import *
from x_controller import *
from z_controller import *
from multirotore import *

class Autopilot:
	def __init__(self, x_target, z_target):
		self.drone = Multirotore(1.0, 0.25, 7.0*(10.0**(-5)))
		self.angle_controller = Angle_Controller(4.0, 1.57, 2.0, 0.2, 15.0)
		self.x_controller = X_Controller(0.4, 2.0, 0.5, 0.2, 0.52)
		self.z_controller = Z_Controller(4.0, 2.0, 20.0, 40.0, 15.0)

		self.x_target = x_target
		self.z_target = z_target
	def evaluate(self, delta_t):
		theta_target = (-1)*self.x_controller.evaluate(delta_t, self.x_target, self.drone.x, self.drone.vx)
		out_1 = self.angle_controller.evaluate(delta_t, theta_target, self.drone.theta, self.drone.omega)

		out_2 = self.z_controller.evaluate(delta_t, self.z_target, self.drone.z, self.drone.vz)

		f1 = out_2 - out_1
		f2 = out_2 + out_1

		self.drone.evaluate(delta_t, f1, f2)
