def gcd(x, y):
	if 0 == y: 
		return x
	else: 
		return gcd(y, x % y)

def lcm(x, y):
	return x * y / gcd(x, y)

tmpLcm = 2
for ci in range(3,21):
	tmpLcm = lcm(tmpLcm, ci)

print tmpLcm
