from graphics import *
from subprocess import call
import os

class Screen:

	def __init__(self,height=1000,width=2000):
		self.win = GraphWin('Screen Size Selector', width, height,autoflush=False)
		self.PointA = Point(width/2-480,height/2-240)
		self.PointB = Point(width/2+480,height/2+240)
		self.rect = Rectangle(self.PointA,self.PointB)
		self.rect.setFill("blue")
		self.rect.draw(self.win)



	def draw(self):
		self.rect.draw(self.win)

	def incrementA(self,dx=0,dy=0):
		self.rect.undraw()
		self.PointA.x -= dx
		self.PointA.y -= dy
		self.rect = Rectangle(self.PointA,self.PointB)
		self.rect.setFill("blue")
		self.draw()

	def incrementB(self,dx=0,dy=0):
		self.rect.undraw()
		self.PointB.x += dx
		self.PointB.y += dy
		self.rect = Rectangle(self.PointA,self.PointB)
		self.rect.setFill("blue")
		self.draw()

	def getHeight(self):
		return self.PointB.x - self.PointA.x

	def getWidth(self):
		return self.PointB.y - self.PointA.y

if not os.path.exists("/video"):
	os.makedirs("/video")
	Selector = Screen()
	if __name__ == "__main__":
		while True:
			key = Selector.win.getKey()
			if key == "Return":
				break
			elif key == "Up":
				Selector.incrementA(dy=5)
			elif key == "Down":
				Selector.incrementA(dy= -5)
			elif key == "Left":
				Selector.incrementA(dx=5)
			elif key == "Right":
				Selector.incrementA(dx=-5)

		while True:
			key = Selector.win.getKey()
			if key == "Return":
				break
			elif key == "Up":
				Selector.incrementB(dy=-5)
			elif key == "Down":
				Selector.incrementB(dy=5)
			elif key == "Left":
				Selector.incrementB(dx=-5)
			elif key == "Right":
				Selector.incrementB(dx=5)

		file = open("/video/dimensions", "w")

		file.write(str(Selector.getHeight()) + " " + str(Selector.getWidth()))


