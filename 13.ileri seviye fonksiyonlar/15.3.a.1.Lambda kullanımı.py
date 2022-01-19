hesapla=lambda a:a+5
print(hesapla(3))

hipotenus1=lambda x,y:(x**2+y**2)**0.5
print(hipotenus1(3,4))

import math
hipotenus2=lambda x,y:math.sqrt(x*x+y*y)
print(hipotenus2(3,4))

print((lambda  x,y:(x**2+y**2)**0.5) (3,4))