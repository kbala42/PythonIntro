"""
-------------------------------------------------------------------tw:@tek_elo

Birden çok harita argümanı kullanın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def addition_subtrction(x, y):
    return x + y, x - y
 
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))

