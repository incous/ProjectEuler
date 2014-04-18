fiboChain = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144}

def doubleFibo(source):
	a, b = source
	x = a * (2 * b - a)
	y = b ** 2 + a ** 2
	return x, y

def fibo(ci):
	if 0 == ci: return 1
	elif 1 == ci: return 2
	else:
		fiboChain[ci] = fiboChain[ci - 2] + fiboChain[ci - 1]
		return fiboChain[ci - 2] + fiboChain[ci - 1]

i = 9
while True:
	source = (fiboChain[i], fiboChain[i+1])
	dest = doubleFibo(source)
	i *= 2
	fiboChain[i] = dest[0]
	fiboChain[i + 1] = dest[1]
	if len(str(fiboChain[i])) > 1000: break

i = i / 2 + 2 # 4608
while True:
	number = fibo(i)
	if len(str(number)) >= 1000: break
	i += 1

print i
