

def generate(start, multi, mod):
	while True:
		start *= multi
		start %= 2147483647
		if start % mod == 0:
			yield start

def compare(genA, genB):
	return '{0:b}'.format(genA)[-16:] == '{0:b}'.format(genB)[-16:]

# saw online to use bitwise ops to speed things up
# explanation for me to understand - 0xFFFF is last 16 bits
# we & our number to it to get our last 16 bits to compare
def compare2(genA, genB):
	return genA & 0xFFFF == genB & 0xFFFF

def main():
	with open('input.txt','r') as input_file:
		#curVal = [int(line.strip().split()[-1]) for line in input_file]
		curVal = [65,8921]

	counter = 0
	A = generate(curVal[0], 16807,1)
	B = generate(curVal[1], 48271,1)
	for i in range(40000000):
		counter += int(compare2(next(A),next(B)))

	counter2 = 0
	A2 = generate(curVal[0], 16807, 4)
	B2 = generate(curVal[1], 48271, 8)
	for i in range(5000000):
		counter2 += int(compare2(next(A),next(B)))
			

	print('Problem 1: ' + str(counter))
	print('Problem 2: ' + str(counter2))

if __name__ == '__main__':
	main()

#283 too low