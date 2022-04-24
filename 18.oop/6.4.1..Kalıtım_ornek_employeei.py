'''
---------------------------------------------------------tw:@tek_elo
Temel Employee sınıfı ve ondan kalıtılan Salary ve Male sınıfları
--------------------------------------------------------------------
'''
class Employee:
   def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Salary:
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
  def jump(self):
    print(self.name, self.salary)

class Male(Salary, Employee):
    def __init__(self, name, gender, occupation):
      self.occupation = occupation
      Employee.__init__(self, name, gender)
      Salary.__init__(self, name, gender)

employee1 = Male("Jim", "male", "technician")
print(employee1.name)