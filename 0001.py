sum = 0
for number in range (3,1000):
	if 0 == number % 3 or 0 == number % 5: sum += number
print sum