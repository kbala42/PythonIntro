"""
-------------------------------------------------------------------tw:@tek_elo

    Sezar şifrelemesi oluşturun

Kriptografide, Caesar's cipher, shift cipher, Caesar's code veya Caesar shift 
olarak da bilinen bir Sezar şifresi, en basit ve en yaygın olarak bilinen 
şifreleme tekniklerinden biridir. Düz metindeki her harfin, alfabenin 
aşağısındaki sabit sayıdaki bir harfle değiştirildiği bir tür değiştirme 
şifresidir. Örneğin, 3'lük bir sola kaydırma ile D, A ile değiştirilir, 
E, B olur ve bu böyle devam eder. Yöntem, adını özel yazışmalarında kullanan 
Julius Caesar'dan almıştır.

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

#https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525

def caesar_encrypt(realText, step):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return outText

code = caesar_encrypt('abc', 2)
print()
print(code)
print()

