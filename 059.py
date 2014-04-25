def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    from itertools import izip, cycle
    import base64
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

ciphertext = ''
content = open('cipher1.txt','r').read()
charArr = content.split(',')
for ch in charArr:
	ciphertext += chr(int(ch))

decryptContent = xor_crypt_string(ciphertext, 'god')
total = 0
for ch in decryptContent:
	total += ord(ch)

print total

# for a in range(ord('a'), ord('z') + 1):
# 	for b in range(ord('a'), ord('z') + 1):
# 		for c in range(ord('a'), ord('z') + 1):
# 			decryptKey = ''.join([chr(a), chr(b), chr(c)])
# 			text = xor_crypt_string(ciphertext[:20], decryptKey)
			# if text.count(' ') > 2: print text
			# if text == '(The Gospel of John,': print decryptKey # key = 'god'

