from controllore_p import *
from controllore_pi import *

class Z_Controller:
	def __init__(self, p_kp, p_sat, pi_kp, pi_ki, pi_sat):
		self.p_controller = Controllore_P(p_kp, p_sat)
		self.pi_controller = Controllore_PI(pi_kp, pi_ki, pi_sat)
	def evaluate(self, delta_t, z_target, z_current, vz_current):
		z_error = z_target - z_current
		vz_target = self.p_controller.evaluate(z_error)
		vz_error = vz_target - vz_current
		spinta_motori = self.pi_controller.evaluate(delta_t, vz_error)

		return spinta_motori
