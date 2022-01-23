'''
---------------------------------------------------------tw:@tek_elo
Program girdiğiniz kenar sayısına bağlı olarak şekiller çizer
rastgele renkler belirler
--------------------------------------------------------------------
'''

import turtle
import time
import random

kenarSayisi = input("Çizmek istediğiniz şeklin kenar sayısı: ")
if kenarSayisi.isdigit():
	kareler = int(kenarSayisi)

angle = 180 - 180*(kareler-2)/kareler

turtle.up

x = 0
y = 0
turtle.setpos(x, y)


sekilSayisi = 8
for x in range(sekilSayisi):

	turtle.color(random.random(), random.random(), random.random())

	x += 10
	y += 10

	turtle.forward(x)
	turtle.left(y)

	for i in range(kareler):
		turtle.begin_fill()
		turtle.down()
		turtle.forward(40)
		turtle.left(angle)
		turtle.forward(40)
		print (turtle.pos())
		turtle.up()
		turtle.end_fill()

time.sleep(11)

turtle.bye()

