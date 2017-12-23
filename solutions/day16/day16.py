
def partner(programs, a, b):
	aIndex = programs.index(a)
	bIndex = programs.index(b)

	programs[aIndex], programs[bIndex] = programs[bIndex], programs[aIndex]

def exchange(programs, a, b):
	programs[int(a)], programs[int(b)] = programs[int(b)], programs[int(a)]

def spin(programs, amt):
	return programs[-1*int(amt):] + programs[:-1*int(amt)]


def main():
	with open('input.txt','r') as input_file:
		moves = input_file.read().strip().split(',')

	programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']


	for move in moves:
		direction = move[1:].split('/')
		if move[0] == 's':
			programs = spin(programs, direction[0])
		elif move[0] == 'x':
			exchange(programs, direction[0], direction[1])
		elif move[0] == 'p':
			partner(programs, direction[0], direction[1])
		else:
			print('invalid input')

	print(programs)

if __name__ == '__main__':
	main()