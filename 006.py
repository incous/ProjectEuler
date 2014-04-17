def sumSquare(maxNumber):
	sum = 0
	for ci in range(1, maxNumber + 1):
		sum += ci ** 2
	return sum

def squareSum(maxNumber):
	if 0 == maxNumber % 2:
		sum = (1 + maxNumber) * (maxNumber / 2)
	else:
		sum = (1 + maxNumber) * (maxNumber / 2) + (maxNumber / 2) + 1
	return sum ** 2

print squareSum(100) - sumSquare(100)
