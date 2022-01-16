print('--------------------------------------------------------------tw:@tek_elo')
print('Üçgen çizme Örnekleri')
print('------------------------------------------------------------------------')
print()

print('------------------')
print('Soldan üçgen çizme')
print('------------------')
for i in range(10):
    print("* "*i)
print()

print('------------------')
print('Sağdan üçgen çizme')
print('------------------')
for i in range(10):
    print((10-i)*' '," *"*i)
print()

print('------------------------')
print('Soldan aşağı üçgen çizme')
print('------------------------')
for i in range(10):
    print("* "*(10-i))
print()

print('------------------------')
print('Sağdan aşağı üçgen çizme')
print('------------------------')
for i in range(10):
    print((i*' '),'*'*(10-i))
print()