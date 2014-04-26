triangleNumbers = []
for ci in range(1, 30):
	triangleNumbers.append(ci * (ci + 1) / 2)
f = open('words.txt', 'r')
words = f.read().split(',')
f.close()
counting = 0
for word in words:
	score = sum(map(ord,list(word.strip('"')))) - 64 * len(word.strip('"'))
	if score in triangleNumbers: counting += 1

print counting
