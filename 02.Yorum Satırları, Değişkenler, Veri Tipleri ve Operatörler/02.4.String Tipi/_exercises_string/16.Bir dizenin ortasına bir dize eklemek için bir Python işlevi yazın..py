"""
-------------------------------------------------------------------tw:@tek_elo
Bir dizenin ortasına bir dize eklemek için bir Python işlevi yazın.
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

