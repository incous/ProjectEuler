result = 1
for ci in range(2,101):
	result = long(ci * result)

total = 0
for number in list(str(result)):
	total += int(number)

print total