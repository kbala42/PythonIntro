"""
-------------------------------------------------------------------tw:@tek_elo

İlk N Fibonacci sayısının karesini hesaplayın, harita işlevini kullanın ve sayıların bir listesini oluşturun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
square = lambda x: x * x 
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))

