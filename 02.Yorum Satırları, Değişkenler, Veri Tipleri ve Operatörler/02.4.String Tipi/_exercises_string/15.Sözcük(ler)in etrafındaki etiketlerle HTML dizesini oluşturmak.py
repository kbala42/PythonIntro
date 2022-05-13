"""
-------------------------------------------------------------------tw:@tek_elo
Sözcük(ler)in etrafındaki etiketlerle HTML dizesini oluşturmak için bir Python işlevi yazın.
Örnek fonksiyon ve sonuç :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Eğitimi') -> '<b>Python Eğitimi </b> '
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

