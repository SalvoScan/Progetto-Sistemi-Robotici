import sys
import math

from PyQt4 import QtGui, QtCore

from autopilot import *

class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(0, 0, 800, 600)
		self.setWindowTitle('Simulatore Quadrirotore 2D')
		self.show()
		
		self.drone = QtGui.QPixmap("drone.jpeg")

		self.delta_t = 1.0*(10.0**(-3))

		self._timer_painter = QtCore.QTimer(self)
		self._timer_painter.start(self.delta_t*1000)
		self._timer_painter.timeout.connect(self.go)

		self.x_target = 2.0
		self.z_target = 2.0
		self.pilota = Autopilot(self.x_target, self.z_target)

	def go(self):
		self.pilota.evaluate(self.delta_t)
		
		self.update()

	def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setPen(QtGui.QColor(255, 255, 255))
		qp.setBrush(QtGui.QColor(255, 255, 255))
		qp.drawRect(event.rect())

		qp.setPen(QtGui.QColor(0, 0, 0))
		qp.drawText(650, 20, "X = %6.3f m" % (self.pilota.drone.x))
		qp.drawText(650, 40, "Vx = %6.3f m/s" % (self.pilota.drone.vx))
		qp.drawText(650, 60, "Z = %6.3f m" % (self.pilota.drone.z))
		qp.drawText(650, 80, "Vz = %6.3f m/s" % (self.pilota.drone.vz))
		qp.drawText(650, 100, "Theta = %6.3f deg" % (math.degrees(self.pilota.drone.theta)))
		qp.drawText(650, 120, "Omega = %6.3f rad/s" % (self.pilota.drone.omega))		

		x_pos = 336 + (self.pilota.drone.x*100)
		y_pos = 500 - (self.pilota.drone.z*100)

		t = QtGui.QTransform()
		s = self.drone.size()
		t.translate(x_pos + s.height()/2, y_pos + s.width()/2)
		t.rotate(-math.degrees(self.pilota.drone.theta))
		t.translate(-(x_pos + s.height()/2), -(y_pos + s.width()/2))

		qp.setTransform(t)
		qp.drawPixmap(x_pos, y_pos, self.drone)

		qp.end()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = MainWindow()

	sys.exit(app.exec_())		

if __name__ == '__main__':
	main()







