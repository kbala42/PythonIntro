"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir dize değerleri listesindeki dizeleri

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def reverse_strings_list(string_list):
    result = list(map(lambda x: "".join(reversed(x)), string_list))
    return result

colors_list = ["Red", "Green", "Blue", "White", "Black"]
print("\nOriginal lists:")
print(colors_list)
print("\nReverse strings of the said given list:")
print(reverse_strings_list(colors_list))
