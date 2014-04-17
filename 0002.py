def fibo(ci):
	if 0 == ci: return 1
	elif 1 == ci: return 2
	else: return fibo(ci - 2) + fibo(ci - 1)

sum = 0
for ci in range (0,32):
	number = fibo(ci)
	if 0 == number % 2: sum += number
print sum