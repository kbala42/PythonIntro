"""
-------------------------------------------------------------------tw:@tek_elo

Bir dizedeki kelimeleri ters çevirin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

