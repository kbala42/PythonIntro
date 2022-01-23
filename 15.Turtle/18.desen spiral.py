'''
---------------------------------------------------------tw:@tek_elo
spiral desen çizme
--------------------------------------------------------------------
'''
import turtle

tuval = turtle.Screen()

turtle.speed(10)

for i in range(50):
	turtle.circle(5 * i)
	turtle.circle(-5 * i)
	turtle.left(i)

turtle.exitonclick()

