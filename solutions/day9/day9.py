

def answer(input_str):
	total_score = 0
	garbage_count = 0
	score_stack = [0]

	inGarbage = False
	skipChar = False

	for i in range(0,len(input_str)):
		char = input_str[i]

		if skipChar:
			skipChar = False
			continue
		elif char == '!':
			skipChar = True
			continue

		if inGarbage:
			if char == '>':
				inGarbage = False
			else:
				garbage_count += 1
		else:
			if char == '<':
				inGarbage = True
			elif char == '{':
				score_stack.append((score_stack[-1] + 1))
			elif char == '}':
				total_score += score_stack.pop()

	return total_score, garbage_count
def main():
	input_string = open('input.txt','r').read()

	print('Problem 1: ' + str(answer(input_string)[0]))
	print('Problem 2: ' + str(answer(input_string)[1]))
	#print(part1('{{<a!>},{<a!>},{<a!>},{<ab>}}'))

if __name__ == '__main__':
	main()