def kareAl():
    for i in range(1,6):
        yield i ** 2

generator = kareAl()
print(*generator)