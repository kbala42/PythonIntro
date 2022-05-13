"""
-------------------------------------------------------------------tw:@tek_elo

Küçük harfle başlayan isimleri çıkardıktan sonra verilen bir isim 
listesinin isimlerinin uzunluğunu toplayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))
