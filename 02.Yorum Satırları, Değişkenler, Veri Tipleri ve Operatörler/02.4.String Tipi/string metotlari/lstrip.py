'''
--------------------------------------------------------------tw:@tek_elo

    lstrip() metodu sagda ki boşluğu siler

--------------------------------------------------------------- -------
'''

txt = ' Python       '
x = txt.lstrip()
print('Merhaba', x, ' Dili')
print()

'''
------------------------------------------------------------------------------
        Syntax
                 string.lstrip(characters)

        Parametre	        Tanım
        characters	        Opsiyonel. Kaldırılması düşünülen karakter seti

------------------------------------------------------------------------------
'''

print('-------------------------------------------')
print('Sol baş dışında ki harfler sonucu etkilemez')
print('-------------------------------------------')
txt2 = 'Merhaba,    Python,  Dili'
print(txt2.lstrip('  '))
print()

print('-------------------------------------------')
print('sol baştan yazılan metin kırpılır----------')
print('-------------------------------------------')
txt3='....***Merhaba, Python, Dili'
print(txt3.lstrip('.*'))
print()