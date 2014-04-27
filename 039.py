def rightAngleTriangle(a,b,c):
	if a ** 2 + b ** 2 == c ** 2: return True
	else: return False

def numRightAngleTrianglePerimeter(p):
	counting = 0
	for a in range(1, p/3):
		for b in range(a, (p - a) / 2):
			c = p - a - b
			if 0 < c and rightAngleTriangle(a, b, c): counting += 1
	return counting

maxSol = 0
ret = 3
for p in range(3, 1001):
	numSol = numRightAngleTrianglePerimeter(p)
	if numSol > maxSol:
		maxSol = numSol
		ret = p

print p
