'''
Andrew Newton
Winter 2021
01/05/21
Point mini-project
'''

class Point(object):
	"""Creates a Point object and has functionality for moving and comparing two points"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def __str__(self):
		return f"({self.x}, {self.y})"





		
		