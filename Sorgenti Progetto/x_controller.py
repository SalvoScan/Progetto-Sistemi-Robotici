from controllore_p import *
from controllore_pi import *

class X_Controller:
	def __init__(self, p_kp, p_sat, pi_kp, pi_ki, pi_sat):
		self.p_controller = Controllore_P(p_kp, p_sat)
		self.pi_controller = Controllore_PI(pi_kp, pi_ki, pi_sat)
	def evaluate(self, delta_t, x_target, x_current, vx_current):
		x_error = x_target - x_current
		vx_target = self.p_controller.evaluate(x_error)
		vx_error = vx_target - vx_current
		theta_target = self.pi_controller.evaluate(delta_t, vx_error)

		return theta_target
