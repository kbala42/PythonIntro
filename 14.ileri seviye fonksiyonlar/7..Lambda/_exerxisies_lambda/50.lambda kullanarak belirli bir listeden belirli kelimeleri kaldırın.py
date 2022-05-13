"""
-------------------------------------------------------------------tw:@tek_elo

lambda kullanarak belirli bir listeden belirli kelimeleri kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
        
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange','black']
print("Original list:")
print(colors)
print("\nRemove words:")
print(remove_colors)
print("\nAfter removing the specified words from the said list:")
print(remove_words(colors, remove_colors))


