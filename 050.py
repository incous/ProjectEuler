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

while primeNumbers[-1] < 1000000:
	primeNumbers.append(nextPrime(primeNumbers))

primeNumbers.pop()

longest = 21
largest = 943
for length in range (longest + 1, len(primeNumbers) - longest):
	if sum(primeNumbers[0:length]) > 1000000:
		break
	for i in range(0, len(primeNumbers) - longest):
		if sum(primeNumbers[i:i+length]) > 1000000:
			break
		elif prime(sum(primeNumbers[i:i+length])):
			longest = length
			largest = sum(primeNumbers[i:i+length])
			break

print 'The longest sum of consecutive primes below one-thousand that adds to a prime, contains %d terms, and is equal to %d.' % (longest, largest)
