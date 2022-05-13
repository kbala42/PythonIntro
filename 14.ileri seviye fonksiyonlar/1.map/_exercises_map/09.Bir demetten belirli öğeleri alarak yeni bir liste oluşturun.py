"""
-------------------------------------------------------------------tw:@tek_elo

Bir demetten belirli öğeleri alarak yeni bir liste oluşturun ve bir dize değerini tamsayıya dönüştürün

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)

