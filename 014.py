chainLength = {0: 0, 1: 1, 2: 2, 13: 10}

def nextItemInChain(chain):
	if 0 == chain[-1] % 2:
		return chain[-1] / 2
	else:
		return 3 * chain[-1] + 1

def getChainLength(number):
	if number in chainLength.keys():
		return chainLength[number]
	else:
		chainLength[number] = 1 + getChainLength(nextItemInChain([number]))
		return chainLength[number]

def chainLength(number):
	tmpChain = [number]
	while tmpChain[-1] != 1:
		if 0 == tmpChain[-1] % 2:
			tmpChain.append(tmpChain[-1] / 2)
		else:
			tmpChain.append(3 * tmpChain[-1] + 1)
	return len(tmpChain)

maxNumber = 0
for ci in range(3,1000000):
	#if getChainLength(ci) > maxNumber: maxNumber = getChainLength(ci)
	if chainLength(ci) > maxNumber:
		maxNumber = chainLength(ci)
		print ci, maxNumber
