import math

def digitFactorial(number):
	numberArr = list(str(number))
	sum = 0
	for ch in numberArr:
		sum += math.factorial(int(ch))
	return sum

total = 0
for ci in range(3, math.factorial(9) * 7):
	if ci == digitFactorial(ci): total += ci

print total
