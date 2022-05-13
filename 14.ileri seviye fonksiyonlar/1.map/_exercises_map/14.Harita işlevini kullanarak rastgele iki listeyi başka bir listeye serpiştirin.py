"""
-------------------------------------------------------------------tw:@tek_elo

Harita işlevini kullanarak rastgele iki listeyi başka bir listeye serpiştirin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
import random
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result
nums1 = [1,2,7,8,3,7]
nums2 = [4,3,8,9,4,3,8,9]
print("Original lists:")
print(nums1)
print(nums2)
print("\nInterleave two given list into another list randomly:")
print(randomly_interleave(nums1, nums2))

