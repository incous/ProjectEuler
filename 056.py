maxnum = 0
for a in range(2, 100):
	for b in range(2, 100):
		number = list(str(a ** b))
		sigma = 0
		for ci in number: sigma += int(ci)
		if maxnum < sigma: maxnum = sigma
