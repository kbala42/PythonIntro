'''
---------------------------------------------------------tw:@tek_elo
*args keyfi parametresi; fonksiyon tanımında
önceden gireceğimiz parametre miktarı belli değilse
--------------------------------------------------------------------
'''
def yazdir(*args):
    for i in args:
        print(i)
yazdir(1,2,3,4,5)
