from autopilot import *
import pylab
import math

delta_t = 1.0*(10.0**(-3))
t = 0

x_target = -2.0
z_target = 3.0
pilota = Autopilot(x_target, z_target)

vett_x = []
vett_z = []

while t <= 20.0:
	pilota.evaluate(delta_t)
	
	vett_x.append(pilota.drone.x)
	vett_z.append(pilota.drone.z)

	t = t + delta_t

pylab.figure(1)
pylab.plot(vett_x, vett_z, 'b-', label = "target")
pylab.legend()

pylab.show()










