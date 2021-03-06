import math

primeNumbers = [2,3,5,7,11,13,17]

def nextPrime(primeNumbers): # return next prime number of primeNumbers
	ci = primeNumbers[-1]
	while True:
		ci += 2;
		for prime in primeNumbers:
			if 0 == ci % prime: break
			if prime > math.sqrt(ci): return ci

def prime(number): # return True if number is prime
	if 1 == number: return True
	# build up list of prime numbers for range (2,sqrt(number))
	while primeNumbers[-1] <= math.sqrt(number):
		newPrime = nextPrime(primeNumbers)
		primeNumbers.append(newPrime)
	# check if number is prime
	for ci in primeNumbers:
		if ci > math.sqrt(number): return True
		if 0 == number % ci: return False

def numFactor(dest): # return list of factors
	factors = []
	if prime(dest): 
		return 1
	while dest != 1:
		for ci in primeNumbers:
			if 0 == dest % ci:
				factors.append(ci)
				dest /= ci
				break
	return len(set(factors))

num = 4
while True:
	if 4 == numFactor(num):
		if 4 == numFactor(num+1) and 4 == numFactor(num+2) and 4 == numFactor(num+3):
			print num
			break
	num += 1

print num
