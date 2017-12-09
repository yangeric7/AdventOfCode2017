
'''
bottom right of each "square" is an odd perfect square. A number will be in that "square"
if it's less than that perfect square. We then find the numbers in the that "square"
in the cardinal directions from 1. Then take the absolute value of the difference between
given number and the cardinal direction numbers. The minimum difference + the sqrt of the perfect
square is the answer
'''
def part1(num):
	index = 1
	while num > index**2:
		index = index + 2

	square = index**2
	square_index = index - 1
	cardinal = []
	for i in range(0,4):
		direction = (square - int(square_index/2)) - (square_index*i)
		cardinal.append(direction)

	return min(abs(direction - num) for direction in cardinal) + int((index - 1)/2)

def testCase1(num,ans):
	if part1(num) == ans:
		return True
	else:
		return False

def main():

	print(testCase1(1,0))
	print(testCase1(12,3))
	print(testCase1(23,2))
	print(testCase1(1024,31))

	print(part1(312051))

if __name__ == '__main__':
	main()