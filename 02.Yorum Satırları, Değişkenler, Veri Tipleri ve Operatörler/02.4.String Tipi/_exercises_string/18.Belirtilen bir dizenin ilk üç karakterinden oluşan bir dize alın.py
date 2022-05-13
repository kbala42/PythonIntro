"""
-------------------------------------------------------------------tw:@tek_elo

Belirtilen bir dizenin ilk üç karakterinden oluşan bir dize alın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

