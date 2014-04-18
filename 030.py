def fifthPowerSum(number):
	numberArr = list(str(number))
	sum = 0
	for ch in numberArr:
		sum += int(ch) ** 5
	return sum

def fourthPowerSum(number):
	numberArr = list(str(number))
	sum = 0
	for ch in numberArr:
		sum += int(ch) ** 4
	return sum

total = 0
for ci in range(2,1000000):
	if ci == fifthPowerSum(ci): total += ci

print total
