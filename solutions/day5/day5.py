


def part1(arr):
	steps = 0
	curIndex = 0

	while curIndex < len(arr):
		jump = arr[curIndex]
		arr[curIndex] += 1
		curIndex = curIndex + jump
		steps += 1

	return steps

def part2(arr):
	steps = 0
	curIndex = 0

	while curIndex < len(arr) and curIndex >= 0:
		jump = arr[curIndex]
		if jump >= 3:
			arr[curIndex] -= 1
		else:
			arr[curIndex] += 1

		curIndex += jump
		steps += 1

	return steps

def main():
	#need two instructions because part 1 modifies the list passed in
	with open('input.txt','r') as input_file:
		instructions = [int(line.strip()) for line in input_file]
		instructions2 = list(instructions)
	
	print('Problem 1: ' + str(part1(instructions)))
	print('Problem 2: ' + str(part2(instructions2)))

if __name__ == '__main__':
	main()