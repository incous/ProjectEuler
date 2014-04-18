wayNumber = 0
for p200 in range(0,2): # 2 pound
	for p100 in range(0, (200 - p200 * 200) / 100 + 1): # 1 pound
		for p50 in range(0, (200 - p200 * 200 - p100 * 100) / 50 + 1): # 50 cent
			for p20 in range(0, (200 - p200 * 200 - p100 * 100 - p50 * 50) / 20 + 1): # 20 cent
				for p10 in range(0, (200 - p200 * 200 - p100 * 100 - p50 * 50 - p20 * 20) / 10 + 1): # 10 cent
					for p5 in range(0, (200 - p200 * 200 - p100 * 100 - p50 * 50 - p20 * 20 - p10 * 10) / 5 + 1): # 5 cent
						for p2 in range(0, (200 - p200 * 200 - p100 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5) / 2 + 1): # 2 cent
							for p1 in range(0, (200 - p200 * 200 - p100 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5 - p2 * 2) + 1): # 10 cent
								if 200 == p200 * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2 + p1: wayNumber += 1

print wayNumber
