def kareAl():
    for i in range(1,6):
        yield i ** 2

generator = kareAl()

iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
