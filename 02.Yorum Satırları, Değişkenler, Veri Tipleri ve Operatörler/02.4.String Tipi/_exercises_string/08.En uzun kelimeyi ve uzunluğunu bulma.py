"""
-------------------------------------------------------------------tw:@tek_elo
Sözcüklerin listesini alan ve en uzun sözcüğü ve en uzun sözcüğün uzunluğunu
döndüren bir Python işlevi yazın.
-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

