"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir tuble listesini sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nTuples küçükten büyüğe sıralaması:")
print(subject_marks)

