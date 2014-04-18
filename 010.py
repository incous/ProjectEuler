import math

primeNumbers = [2,3,5,7,11,13,17]

def nextPrime(primeNumbers): # return next prime number of primeNumbers
	ci = primeNumbers[-1]
	while True:
		ci += 1;
		for prime in primeNumbers:
			if 0 == ci % prime: break
			if prime > math.sqrt(ci): return ci

while primeNumbers[-1] < 2000000:
	primeNumbers.append(nextPrime(primeNumbers))

total = 0
for number in primeNumbers[0:-1]:
	total += number

print total