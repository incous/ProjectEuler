numberArr = []
for a in range(2, 101):
	for b in range(2, 101):
		numberArr.append(a ** b)

print len(set(numberArr))
