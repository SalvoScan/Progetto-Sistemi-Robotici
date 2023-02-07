from autopilot_up import *
import pylab
import math

delta_t = 1.0*(10.0**(-3))
t = 0

pilota = Autopilot()

#--------------------------
# PATH 1
pilota.addPoint(0.0, 1.0)
pilota.addPoint(2.0, 1.0)
pilota.addPoint(2.0, 3.0)
pilota.addPoint(0.0, 3.0)
pilota.addPoint(-2.0, 3.0)
pilota.addPoint(-2.0, 1.0)

#--------------------------
# PATH 2
#pilota.addPoint(-2.0, 1.0)
#pilota.addPoint(2.0, 1.0)
#pilota.addPoint(0.0, 0.8)

#--------------------------
# PATH 3
#pilota.addPoint(2.0, 2.0)
#pilota.addPoint(-2.0, 0.0)
#pilota.addPoint(-2.0, 3.0)

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










