"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak verilen iki dizinin kesişimini bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the said arrays: ",result)

