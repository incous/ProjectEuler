data = open('names.txt','r').read()
nameArr = data.split(',')
nameArr.sort()

def nameScore(name):
	score = 0
	for ch in list(name.strip('"')):
		score += ord(ch) - 64
	return score

totalScore = 0
for ci in range(0, len(nameArr)):
	totalScore += (ci + 1) * nameScore(nameArr[ci])

print totalScore 
