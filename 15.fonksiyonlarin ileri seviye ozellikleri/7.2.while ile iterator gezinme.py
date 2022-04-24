'''
---------------------------------------------------------tw:@tek_elo
while döngüsü ile elemanlar arasında gezilebilir
--------------------------------------------------------------------
'''
# Normal şekilde liste içinde gzeinme
liste = [1,2,3,4,5]
for i in liste:
    print(i)

print("---for döngüsünün iterator karşılığı----")
iterator= iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break