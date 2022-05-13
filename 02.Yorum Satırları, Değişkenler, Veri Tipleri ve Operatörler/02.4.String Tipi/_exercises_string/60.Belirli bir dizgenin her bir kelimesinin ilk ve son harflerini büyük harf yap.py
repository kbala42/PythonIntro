"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir dizgenin her bir kelimesinin ilk ve son harflerini büyük harf yap

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))
