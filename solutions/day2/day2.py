

def part1(arr):
	checksum = 0

	for row in arr:
		row = list(map(int, row))
		maxNum = max(row)
		minNum = min(row)

		checksum = checksum + (maxNum - minNum)

	return checksum

def part2(arr):
	rowSum = 0

	#refactor here to make prettier, perhaps use list comprehension
	for row in arr:
		row = list(map(int,row))
		for i in range(0,len(row)):
			for j in range(0,len(row)):
				if i != j and row[i] % row[j] == 0:
					rowSum = rowSum + int(row[i]/row[j])
					break;

	return rowSum

def main():
	with open('input.txt','r') as input_file:
		lines = [line.split() for line in input_file]

	print('Problem 1: ' + str(part1(lines)))
	print('Probelm 2: ' + str(part2(lines)))


if __name__ == '__main__':
	main()