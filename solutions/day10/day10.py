

def decrypt(input_file,input_list):
	skipSize = 0
	currentPos = 0
	for length in input_file:
		currentPos = knothash(length, currentPos, skipSize, input_list)
		skipSize += 1
	return input_list[0] * input_list[1]



def knothash(length,currentPos, skipSize, curList):
	reverse_list = reverse(curList,currentPos, length)
	curIndex = currentPos
	for i in range(0,len(reverse_list)):
		curList[curIndex] = reverse_list[i]
		curIndex += 1
		if curIndex >= len(curList):
			curIndex = 0

	currentPos = currentPos + length + skipSize
	if currentPos >= len(curList):
		currentPos = currentPos % len(curList)

	return currentPos

def reverse(input_list, start, length):
	reverse_list = []
	#print(input_list)
	if (start + length) >= len(input_list):
		reverse1 = input_list[start:len(input_list)][::-1]
		reverse2 = input_list[0:(start + length - len(input_list))][::-1]
		reverse_list = reverse2 + reverse1
	else:
		reverse_list = input_list[start:(start+length)][::-1]
	return reverse_list



def main():
	input_file = [int(num) for num in open('input.txt','r').read().strip().split(',')]
	input_list = []
	for i in range(0,256):
		input_list.append(i)
	
	print('Problem 1: ' + str(decrypt(input_file, input_list)))
	#print(decrypt([3,4,1,5],[0,1,2,3,4]))

if __name__ == '__main__':
	main()

#16256 too low
