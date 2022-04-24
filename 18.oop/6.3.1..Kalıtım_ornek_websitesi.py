'''
---------------------------------------------------------tw:@tek_elo
Temel Website sınıfı ve ondan kalıtılan Website1 ve Website2 sınıfları
--------------------------------------------------------------------
'''
class Website:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

    def loginInfo(self):
        print(self.name + " " + self.surname)

class Website1(Website):
    def __init__(self, name, surname, ids):
        # Website'den yalnızca name, surname kalıttığımızı belirtiyoruz
        Website.__init__(self,name,surname)
        self.ids = ids
    def login(self):
        print(self.name + " "+ self.surname+" "+ self.ids)

class Website2(Website):

    def __init__(self,name, surname, email):
        self.email = email
        Website.__init__(self, name, surname)


    def login(self):
        print(self.name + " " + self.surname + " " + self.email)

w = Website("name","surname")
w.loginInfo()

print('--------------------------------')

w1 = Website1("name","surname","KT85")
w1.login()

print('--------------------------------')

w2 = Website2("name","surname","kt85@a.com")
w2.login()