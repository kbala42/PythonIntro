'''
---------------------------------------------------------tw:@tek_elo
Ekkulanım (overloading) örneği
--------------------------------------------------------------------
'''
class Rectangle():

	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth

	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")

# Rectangle sınıfından kalıtıyoruz
class Square(Rectangle):

	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)# Rectangle init metodunu kullanmak istediğimiz şekil

	# Alan hesaplayan methot farklı
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()