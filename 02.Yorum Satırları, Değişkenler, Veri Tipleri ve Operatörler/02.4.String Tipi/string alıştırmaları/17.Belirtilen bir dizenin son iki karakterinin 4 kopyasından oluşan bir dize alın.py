"""
-------------------------------------------------------------------tw:@tek_elo
Belirtilen bir dizenin son iki karakterinin 4 kopyasından oluşan bir dize alın


-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))
