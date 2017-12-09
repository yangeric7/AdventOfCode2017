

def part1(arr):
	valid = 0

	for passphrase in arr:
		if len(passphrase) == len(set(passphrase)):
			valid = valid + 1

	return valid

def part2(arr):
	valid = 0

	for passphrase in arr:
		unique = []
		for word in passphrase:
			anagram = sorted(list(word))
			if anagram in unique:
				pass
			else:
				unique.append(anagram)
		if len(unique) == len(passphrase):
			valid = valid + 1
			
	return valid


def main():
	with open('input.txt','r') as input_file:
		lines = [line.split() for line in input_file]

	print('Problem 1: ' + str(part1(lines)))
	print('Probelm 2: ' + str(part2(lines)))

if __name__ == '__main__':
	main()