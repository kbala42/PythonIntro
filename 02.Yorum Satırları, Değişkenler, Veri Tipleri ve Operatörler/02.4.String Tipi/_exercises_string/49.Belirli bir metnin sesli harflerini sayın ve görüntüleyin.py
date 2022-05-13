"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir metnin sesli harflerini sayın ve görüntüleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
vowel('w3resource');

