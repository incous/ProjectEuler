import sys

total = 0
n = 1
while True:
	for a in range(1, 10):
		if len(str(a ** n)) == n: total += 1
		if len(str(9 ** n)) < n:
			print total
			sys.exit()
	n += 1
