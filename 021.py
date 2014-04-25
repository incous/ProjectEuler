def sumDivisor(number):
	ret = 0
	for i in range(1, number):
		if 0 == number % i: ret += i
	return ret

total = 0
for num in range(1,10000):
	b = sumDivisor(num)
	if num == sumDivisor(b) and b != num:
		print num
		total += num

print total
