"""
-------------------------------------------------------------------tw:@tek_elo

Sınırlayıcının son oluşumunda bir dize bölün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))

