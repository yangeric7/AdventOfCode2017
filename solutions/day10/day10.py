

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

	if (start + length) >= len(input_list):
		reverse1 = input_list[start:len(input_list)][::-1]
		reverse2 = input_list[0:(start + length - len(input_list))][::-1]
		reverse_list = reverse2 + reverse1
	else:
		reverse_list = input_list[start:(start+length)][::-1]
	return reverse_list

def main():
	with open('input.txt','r') as input_text:
		line = input_text.readline()
		input_nums= [int(num) for num in line.strip().split(',')]
		input_len = [ord(char) for char in line.strip()]

	lengths = input_len + [17,31,73,47,23]

	input_list = []
	for i in range(256):
		input_list.append(i)
	
	print('Problem 1: ' + str(decrypt(input_nums, list(input_list))))

	second_list = list(input_list)
	skipSize = 0
	currentPos = 0

	for i in range(64):
		for length in lengths:
			currentPos = knothash(length, currentPos, skipSize, second_list)
			skipSize += 1

	dense_hash = []
	for i in range(0,len(second_list),16):
		sparse_hash = second_list[i:i+16]
		output = reduce(lambda x,y: x^y, sparse_hash)
		dense_hash.append(output)

	hexdecimal = ''
	for num in dense_hash:
		hexhash = hex(num).replace('0x','')
		if len(hexhash) == 1:
			hexhash = '0' + hexhash
		hexdecimal += hexhash

	print('Problem 2: '+ str(hexdecimal))

if __name__ == '__main__':
	main()

