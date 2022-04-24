'''
---------------------------------------------------------tw:@tek_elo
Shape sınıfı örneği
--------------------------------------------------------------------
'''
from abc import ABC, abstractmethod

class Shape(ABC):
	"""
		Shape: super class /abstract class
	"""

	@abstractmethod
	def area(selfself):pass
	@abstractmethod
	def perimeter(self):pass

	#overriding and polymorphism
	def toString(selfself):pass

#child
class Square(Shape):
	"sub class"
	def __init__(self, edge):
		self.__edge = edge  #encapsulation private attribute

	def area(self):
		result=self.__edge**2
		print("Square area:",result)

	def perimeter(self):
		result=self.__edge*4

	# overriding and polymorphism
	def toString(self):
		print("Square edge: ", self.__edge)

class Circle(Shape):
	"Cicrle class"

	PI=3.14

	def __init__(self,radius):
		self.__radius = radius

	def area(self):
		result = self.PI*self.__radius**2
		print("Circle area: ", result)

	def perimeter(self):
		result=2*self.PI*self.__radius
		print("Circle perimeter: ", result)

	def toString(self):
		print("Circle radius. ",self.__radius)

circle = Circle(5)
circle.area()
circle.perimeter()
circle.toString()

square = Square(5)
square.area()
square.perimeter()
square.toString()
