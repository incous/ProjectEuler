import math

primeNumbers = [2,3,5,7,11]

def nextPrime(primeNumbers): # return next prime number of primeNumbers
	ci = primeNumbers[-1]
	while True:
		ci += 1;
		for prime in primeNumbers:
			if 0 == ci % prime: break
			if prime > math.sqrt(ci): return ci

def truncatablePrime(number):
	tmpArr = list(str(number))
	for i in range(0,len(tmpArr)):
		if not int(''.join(tmpArr[0:i+1])) in primeNumbers: return False
		if not int(''.join(tmpArr[i:])) in primeNumbers: return False
	return True

count = 0
results = []
while primeNumbers[-1] > 10:
	nextNumber = nextPrime(primeNumbers)
	primeNumbers.append(nextPrime(primeNumbers))
	if truncatablePrime(nextNumber):
		count += 1
		results.append(nextNumber)
		print nextNumber
		if 11 == count: break

print sum(results)
