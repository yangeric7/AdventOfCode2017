

def part1(instructions):
	register_dict = {}
	maxvalue = 0
	for instr in instructions:
		if instr[0] not in register_dict:
			register_dict[instr[0]] = 0
		if instr[4] not in register_dict:
			register_dict[instr[4]] = 0
		operation(register_dict, instr[0], instr[1], instr[2], instr[4], instr[5], instr[6])

		largestVal = register_dict[max(register_dict,key=register_dict.get)]
		if largestVal > maxvalue:
			maxvalue = largestVal

	return register_dict[max(register_dict,key=register_dict.get)], maxvalue


def operation(register_dict, registerA, operator, increment, registerB, comparator, value):
	valueB = register_dict[registerB]
	if operator == 'inc' and compare(valueB, int(value), comparator):
		register_dict[registerA] += int(increment)
	elif operator == 'dec' and compare(valueB, int(value), comparator):
		register_dict[registerA] -= int(increment)
	else:
		pass

def compare(register_value, value, comparator):
		
	if comparator == '>':
		return (register_value > value)
	elif comparator == '<':
		return (register_value < value)
	elif comparator == '==':
		return (register_value == value)
	elif comparator == '>=':
		return (register_value >= value)
	elif comparator == '<=':
		return (register_value <= value)
	elif comparator == '!=':
		return (register_value != value)
	else:
		print('unknown comparator')

def main():
	
	with open('input.txt','r') as input_file:
		instructions = [line.split() for line in input_file]

	print('Problem 1: ' + str(part1(instructions)[0]))
	print('Problem 2: ' + str(part1(instructions)[1]))

if __name__ == '__main__':
	main()
