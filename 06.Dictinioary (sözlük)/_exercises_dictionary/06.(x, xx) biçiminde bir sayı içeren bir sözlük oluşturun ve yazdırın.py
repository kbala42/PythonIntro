"""
-------------------------------------------------------------------tw:@tek_elo

(x, xx) biçiminde bir sayı içeren bir sözlük oluşturun ve yazdırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""


n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 

