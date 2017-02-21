from multiprocessing import Queue
from graphics import *

class Canvas:
		def __init__(self,center,width = 400, height = 400, mode = 'not visible'): # center is a touple (x,y)
			self.win = GraphWin('Canvas', width, height, autoflush=False)
			self.width = width
			self.height = height
			self.center = center
			self.mode = mode
			#self.drawPlane()
			self.win.setCoords(0,0,width,height)

			self.pixMap = Image(Point(center[0] + width/2,center[1] + height/2), width, height)
			for x in range(width):
				for y in range(height):
					self.pixMap.setPixel(x,y,"blue")
			self.pixMap.draw(self.win)
			self.printBuffer()

		def compColors(self, color1, color2):
			if color1[0] != color2[0]:
				return False
			if color1[1] != color2[1]:
				return False 
			if color1[2] != color2[2]:
				return False
			return True

		def is_Inside(self, x, y):
			if x < 0 or y < 0:
				return False
			if x >= self.width or y >= self.width:
				return False
			return True


		def fill(self, color, struct):
			clickPoint = self.win.getMouse()
			print(str(clickPoint.getX()) + " " + str(clickPoint.getY()))
			PrevColor = self.pixMap.getPixel( int(clickPoint.getX()), int(clickPoint.getY()) )

			if struct == "List":
				self.dfs( (int(clickPoint.getX()), int(clickPoint.getY())) , color, PrevColor )
			else:
				self.bfs( (int(clickPoint.getX()), int(clickPoint.getY())) , color, PrevColor )

		def dfs(self, center, setColor, PrevColor):
			self.serch([] ,center, setColor, PrevColor)

		def bfs(self, center, setColor, PrevColor):
			self.serch(Queue() ,center, setColor, PrevColor)

		def append(self, data, val):
			if type(data) is type(Queue()):
				data.put(val)
			else:
				data.append(val)

		def pop(self, data):
			if type(data) is type(Queue()):
				return data.get()
			else:
				return data.pop()

		def serch(self, lista, center, setColor, PrevColor):
			self.append(lista,center)
			cont = 0
			while lista:
				center = self.pop(lista)
				x = center[0]
				y = center[1]
				self.pixMap.setPixel(x, y, setColor)
				if self.is_Inside(x-1, y) and self.compColors(PrevColor, self.pixMap.getPixel(x-1, y)):
					self.append(lista, ( (x-1, y) ) )
				if self.is_Inside(x, y-1) and self.compColors(PrevColor, self.pixMap.getPixel(x, y-1)):
					self.append(lista, ( (x, y-1) ) )
				if self.is_Inside(x+1, y) and self.compColors(PrevColor, self.pixMap.getPixel(x+1, y)):
					self.append(lista, ( (x+1, y) ) )
				if self.is_Inside(x, y+1) and self.compColors(PrevColor, self.pixMap.getPixel(x, y+1)):
					self.append(lista, ( (x, y+1) ) )

				if cont % 1000 is 0:
					self.printBuffer()
				cont +=1

			

		def printBuffer(self):
			self.win.update()

		def circle(x,y):
			pass


if __name__ == "__main__":
	window = Canvas((0, 0))

	window.fill("green", "Queue")
	window.fill("green", "List")


