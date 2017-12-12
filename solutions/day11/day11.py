
# here we essentially calculate the "fewest steps from the start" as the child walks the path
# for each direction taken, we calc the number of steps to the current spot
def furthestStep(steps):
	stepsTaken = []
	maxSteps = 0

	for step in steps:
		stepsTaken.append(step)
		numSteps = fewSteps(stepsTaken)
		if numSteps > maxSteps:
			maxSteps = numSteps

	return maxSteps

def fewSteps(steps):
	directions = {'n':0, 'ne':0, 'se':0, 's':0, 'sw':0,'nw':0}

	for step in steps:
		directions[step] += 1

	prev_dir = {}
	while directions != prev_dir:
		directions = trim(directions)
		simplify(directions)
		prev_dir = dict(directions)

	return sum(directions.values())

# here we trim directions by cancelation. ex one step n and one step s is the same as 0 steps
def trim(directions):
	temp_direct = dict(directions)
	directions['n'] = (temp_direct['n'] - temp_direct['s'])
	directions['s'] = (temp_direct['s'] - temp_direct['n'])
	directions['ne'] = (temp_direct['ne'] - temp_direct['sw'])
	directions['sw'] = (temp_direct['sw'] - temp_direct['ne'])
	directions['nw'] = (temp_direct['nw'] - temp_direct['se'])
	directions['se'] = (temp_direct['se'] - temp_direct['nw'])

	return {key:(0 if value < 0 else value) for key,value in directions.items()}

# here we simplify directions. ex one step n and one step se is the same as one step ne
def simplify(directions):
	
	consolidate(directions,'ne','n','se')
	consolidate(directions,'se','ne','s')
	consolidate(directions,'s','se','sw')
	consolidate(directions,'sw','s','nw')
	consolidate(directions,'nw','sw','n')
	consolidate(directions,'n','nw','ne')

# method to perform such simplifications
def consolidate(directions, final, path1, path2):
	temp_dict = {path1:directions[path1], path2:directions[path2]}
	min_key = min(temp_dict, key=temp_dict.get)
	min_val = temp_dict[min_key]

	directions[final] += min_val

	for key in temp_dict.keys():
		if key == min_key:
			directions[key] = 0
		else:
			directions[key] = directions[key] - min_val


# i believe there is a more efficent solution out there to determine the steps it takes to 
# a certain point in the path
def main():
	steps = open('input.txt','r').read().strip().split(',')
	
	print('Problem 1: ' + str(fewSteps(steps)))
	print('Problem 2: ' + str(furthestStep(steps)))


if __name__ == '__main__':
	main()