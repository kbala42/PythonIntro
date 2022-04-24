'''
---------------------------------------------------------tw:@tek_elo
*args yine sabit parametrelerle tanımlanabilir
--------------------------------------------------------------------
'''
# okul sabit parametre
def yazdir(okul,*args):
    print(okul)
    print("-------------")
    for i in args:
        print(i)
yazdir("Anaokulu","Anasınıfı")
yazdir("ilkokul",1,2,3,4)
yazdir("ortaokul",5,6,7,8)
