from controllore_p import *
from controllore_pi import *

class Angle_Controller:
	def __init__(self, p_kp, p_sat, pi_kp, pi_ki, pi_sat):
		self.p_controller = Controllore_P(p_kp, p_sat)
		self.pi_controller = Controllore_PI(pi_kp, pi_ki, pi_sat)
	def evaluate(self, delta_t, theta_target, theta_current, omega_current):
		theta_error = theta_target - theta_current
		omega_target = self.p_controller.evaluate(theta_error)
		omega_error = omega_target - omega_current
		out = self.pi_controller.evaluate(delta_t, omega_error)

		return out
