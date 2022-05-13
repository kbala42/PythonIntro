"""
-------------------------------------------------------------------tw:@tek_elo
ip adresinde sıfıla başlayanlardan sıfırları kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def remove_zeros_from_ip(ip_add):
  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
  return new_ip_add ;

print(remove_zeros_from_ip("255.024.01.01"))
print(remove_zeros_from_ip("127.0.0.01 "))
