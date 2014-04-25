# 28433 * 2^7830457 + 1
# find base n that 2^n > 10^10
n = 2
while 2 ** n < 10 ** 10:
	n += 1

tenDigits = int(str(2 ** n)[-10:])

# 2^7830457 = (2^34)^(7830457/34 + 7830457%34) = tenDigits^(230307 + 19) => binary tree

def productTenDigits(number, x): # return tenDigits^(2^x)
	lastTenDigist = number
	for ci in range(0,x):
		lastTenDigist = int(str(lastTenDigist ** 2)[-10:])
	return lastTenDigist

product = 1
for cj in range(0,len(bin(230307)[2:])):
	if 1 == int(bin(230307)[2+cj]): product = int(str(product * productTenDigits(tenDigits, len(bin(230307)[2:]) - 1 - cj))[-10:])


print str(product * 28433 * (2**19) + 1)[-10:]
