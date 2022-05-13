"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir listede uzunluk altı değerlerini bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)
