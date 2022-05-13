"""
-------------------------------------------------------------------tw:@tek_elo

 Verilen iki küçük harf dizesinden sözlük sırasına göre tüm ortak 
 karakterleri bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from collections import Counter 
def common_chars(str1,str2): 	
	d1 = Counter(str1) 
	d2 = Counter(str2) 
	common_dict = d1 & d2 
	if len(common_dict) == 0: 
		return "No common characters."

	# list of common elements 
	common_chars = list(common_dict.elements()) 
	common_chars = sorted(common_chars) 

	return ''.join(common_chars) 

str1 = 'Python'
str2 = 'PHP'
print("Two strings: "+str1+' : '+str2)
print(common_chars(str1, str2))
str1 = 'Java'
str2 = 'PHP'
print("Two strings: "+str1+' : '+str2)
print(common_chars(str1, str2))

