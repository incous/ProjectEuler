def pythagorean(a,b,c):
	return a**2 + b**2 == c**2

for a in range(1,998):
	for b in range(a + 1, 500):
		c = 1000 - a - b
		if pythagorean(a,b,c): print a * b * c
