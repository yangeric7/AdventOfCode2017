

def part1(program_dict):

	while len(program_dict.keys()) > 1:
		print(list(program_dict.keys()))
		keys = list(program_dict.keys())
		remove(program_dict,keys[0])

	return list(program_dict.keys())[0]

def remove(program_dict,program_key):
	if program_key not in program_dict:
		return

	else:
		#print(program_dict[program_key])
		for program in program_dict[program_key]:
			remove(program_dict, program)
		
		program_dict.pop(program_key, None)

def main():
	program_dict = {}
	with open('input.txt','r') as input_file:
		#sample line: dosteiu (262) -> vliyv, rfxmk, nulxd, tckql
		for line in input_file:
			line = line.replace(',','')
			clean_line = line.strip('\n').split(' ')
			if len(clean_line) >= 4:
				program_dict[clean_line[0]] = clean_line[3:]

	print('Problem 1: ' + part1(program_dict))

if __name__ == '__main__':
	main()