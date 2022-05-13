"""
-------------------------------------------------------------------tw:@tek_elo

Bir tamsayı dizisinde pozitif sayıların, negatif sayıların ve sıfırların oranını bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
from array import array

def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
            
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)

nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)

