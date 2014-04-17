def palindrome(number):
	tmpArray = list(str(number))
	for ci in range(0,len(tmpArray) / 2):
		if tmpArray[ci] != tmpArray[-1 - ci]: return False
	return True

results = []
for x in range(100, 1000):
	for y in range(x, 1000):
		results.append(x * y)

results.sort(reverse=True)
for number in results:
	if palindrome(number):
		print number
		break