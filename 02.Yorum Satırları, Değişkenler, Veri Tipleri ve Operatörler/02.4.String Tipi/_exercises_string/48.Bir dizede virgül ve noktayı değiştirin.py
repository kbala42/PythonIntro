"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizede virgül ve noktayı değiştirin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
