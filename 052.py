number = 100
while True:
	number += 1
	largest = 6 * number
	if len(str(largest)) > len(str(number)):
		continue
	so1 = list(str(number))
	so2 = list(str(2 * number))
	so3 = list(str(3 * number))
	so4 = list(str(4 * number))
	so5 = list(str(5 * number))
	so6 = list(str(largest))
	so1.sort()
	so2.sort()
	so3.sort()
	so4.sort()
	so5.sort()
	so6.sort()
	if so1 == so2 == so3 == so4 == so5 == so6:
		print number
		break
