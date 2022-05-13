"""
-------------------------------------------------------------------tw:@tek_elo

Bir tamsayı listesini, bir dize listesindeki tamsayı demetini dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
nums_list = [1,2,3,4]
nums_tuple = (0, 1, 2, 3) 
print("Original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = tuple(map(str,nums_tuple))
print("\nList of strings:")
print(result_list)
print("\nTuple of strings:")
print(result_tuple)

