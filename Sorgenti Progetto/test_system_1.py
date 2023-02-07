from angle_controller import *
from multirotore import *
import pylab
import math

delta_t = 1.0*(10.0**(-3))
t = 0.0

p_kp = 100.0
p_sat = 0.52 
pi_kp = 100.0 
pi_ki = 10.0 
pi_sat = 1.57
angle_controller = Angle_Controller(p_kp, p_sat, pi_kp, pi_ki, pi_sat)

massa = 1.0
lunghezza = 0.25
attrito = 7.0*(10.0**(-5))
drone = Multirotore(massa, lunghezza, attrito)

vett_theta = []
vett_theta_target = []
vett_t = []

theta_target = math.radians(40.0) # Inclinazione di 40.0 GRADI
f_motori = 15.0

while t <= 20.0:
	out = angle_controller.evaluate(delta_t, theta_target, drone.theta, drone.omega)
	f1 = f_motori - out
	f2 = f_motori + out
	drone.evaluate(delta_t, f1, f2)

	vett_theta.append(math.degrees(drone.theta))
	vett_theta_target.append(math.degrees(theta_target))
	vett_t.append(t)

	t = t + delta_t

pylab.figure(1)
pylab.plot(vett_t, vett_theta, 'r-', label = "theta")
pylab.plot(vett_t, vett_theta_target, 'y-', label = "theta_target")
pylab.legend()

pylab.show()










