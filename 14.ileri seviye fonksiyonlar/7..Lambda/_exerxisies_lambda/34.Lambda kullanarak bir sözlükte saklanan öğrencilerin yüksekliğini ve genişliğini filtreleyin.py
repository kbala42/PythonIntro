"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir sözlükte saklanan öğrencilerin yüksekliğini ve 
genişliğini filtreleyin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary:")
print(students)
print("\nHeight> 6ft and Weight> 70kg:")
print(filter_data(students))

