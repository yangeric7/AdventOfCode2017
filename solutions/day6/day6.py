
def part1(mem):
	config = []
	cycles = 0

	while mem not in config:
		config.append(list(mem))

		max_num = max(mem)
		max_index = mem.index(max_num)
		curIndex = max_index
		mem[max_index] = 0
		for counter in range(0,max_num):
			curIndex += 1
			if curIndex >= len(mem):
				curIndex = 0
			mem[curIndex] += 1

		cycles += 1

	#add duplicate to final config list for problem 2
	config.append(list(mem))
	
	return cycles, config

def part2(config):
	dupBlock = config[len(config)-1]
	
	#returns first location of block which would be the first appearance since duplicate is last index
	loc = config.index(dupBlock)
	return (len(config) - 1) - loc


def main():
	with open('input.txt','r') as input_file:
		memory = [int(block) for block in input_file.read().strip().split('\t')]

	#print(str(part1([0,2,7,0])))
	res,config = part1(memory)
	print('Problem 1: ' + str(res))
	print('Problem 2: ' + str(part2(config)))
if __name__ == '__main__':
	main()