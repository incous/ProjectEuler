def readNumber(number):
	numberArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 71, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
	readableArr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred', 'one thousand']
	readableDict = dict(zip(numberArr, readableArr))
	if number in numberArr: return readableDict[number]
	if 20 < number < 100:
		return readableDict[numberArr[17 + (number / 10)]] + " " + readableDict[numberArr[(number % 10) - 1]]
	if 100 < number < 1000:
		return readableDict[numberArr[(number / 100) - 1]] + " hundred and " + readNumber(number % 100)

totalLength = 0
for ci in range(1, 1001):
	print ci
	print readNumber(ci)
	print len(readNumber(ci).replace(' ', ''))
	totalLength += len(readNumber(ci).replace(' ', ''))

print totalLength
