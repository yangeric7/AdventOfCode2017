
def part1(num):
	sumOfSeq = 0

	prevNum = num[len(num)-1]
	for i in range(0,len(num)):
		curNum = num[i]
		if prevNum == curNum:
			sumOfSeq = sumOfSeq + int(prevNum)

		prevNum = curNum

	return sumOfSeq

def part2(num):
	sumOfSeq = 0
	mid = int(len(num)/2)
	for i in range(0,mid):
		if num[i] == num[mid+i]:
			sumOfSeq = sumOfSeq + int(num[i])

	return sumOfSeq*2 #multiply by two since the numbers that are "halfway" are pairs

def main():
	with open('input.txt','r') as input_file:
		input_num = input_file.read().replace('\n','')

	print('Problem 1: ' + str(part1(input_num)))
	print('Problem 2: ' + str(part2(input_num)))


if __name__ == '__main__':
	main()