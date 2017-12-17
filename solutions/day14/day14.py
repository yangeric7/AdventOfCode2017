
# code from day 10 knot hash
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

def hash(key):
	second_list = [i for i in range(256)]
	skipSize = 0
	currentPos = 0

	input_len = [ord(char) for char in key.strip()]
	lengths = input_len + [17,31,73,47,23]


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

	return hexdecimal

def dfs(board, start, visited):
	i = start[0]
	j = start[1]
	if start in visited:
		return

	if board[i][j] == 0:
		return

	visited.add((i,j))
	if i > 0:
		dfs(board,(i-1,j), visited)
	if i < 127:
		dfs(board, (i+1,j), visited)
	if j > 0:
		dfs(board, (i,j-1), visited)
	if j < 127:
		dfs(board, (i,j+1), visited)

def main():
	key_input = 'ugkiagan'
	grid = []

	total = 0
	board = []
	for i in range(128):
		hexdecimal = hash('%s-%d' % (key_input,i))
		defrag = '{:0128b}'.format(int(hexdecimal,16))
		row = map(int,defrag)
		total += sum(row)
		board.append(row)

	regions = 0
	visited = set()

	for i in range(128):
		for j in range(128):
			if (i,j) in visited:
				continue

			if board[i][j] == 0:
				continue

			regions += 1
			dfs(board, (i,j), visited)

	print('Problem 1: ' + str(total))
	print('Problem 2: ' + str(regions))


if __name__ == '__main__':
	main()