import math

primeNumbers = [2,3,5,7,11,13,17]

def nextPrime(primeNumbers): # return next prime number of primeNumbers
	ci = primeNumbers[-1]
	while True:
		ci += 1;
		for prime in primeNumbers:
			if 0 == ci % prime: break
			if prime > math.sqrt(ci): return ci

def permutationsThree(number):
	a = list(str(number))
	a.sort()
	b = list(str(number + 3330))
	b.sort()
	c = list(str(number + 6660))
	c.sort()
	if a == b == c: return True
	else: return False

while primeNumbers[-1] < 10000:
	primeNumbers.append(nextPrime(primeNumbers))

for number in primeNumbers:
	if number > 1000 and (number + 3330) in primeNumbers and (number + 6660) in primeNumbers and permutationsThree(number): print ''.join([str(number), str(number + 3330), str(number + 6660)])

