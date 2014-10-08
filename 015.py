def tinhduong(ax, ay, bx, by):
	ret = 0
	if ax == bx or ay == by:
		return 1
	else:
		return tinhduong(ax + 1, ay, bx, by) + tinhduong(ax, ay + 1, bx, by)

total = 0
for i in range(0, 10):
	total += 2 * (tinhduong(0, 0, i, 20 - i) ** 2)

total += tinhduong(0, 0, 10, 10) ** 2
print total
