

def calc_severity(size, down, loc, delay):
	packet = -1 - delay
	severity = 0

	while packet <= max(size.keys()):
		packet += 1
		if packet in loc.keys() and loc[packet] == 1:
			severity += (packet * size[packet])

		for key in loc.keys():
			if down[key]:
				loc[key] -= 1
				if loc[key] == 1:
					down[key] = False
			else:
				loc[key] += 1
				if loc[key] >= size[key]:
					down[key] = True

	return severity

def undetected(delay, size):

	return [((delay + key) % (2*(val - 1)) ) for key,val in size.items()]

def main():
	with open('input.txt','r') as input_file:
		input_wall = [wall.strip().split(':') for wall in input_file]

	wall_size = {}
	for wall in input_wall:
		wall_size[int(wall[0])] = int(wall[1])

	scanner_down = {}
	scanner_loc = {}
	for key in wall_size.keys():
		scanner_down[key] = False
		scanner_loc[key] = 1

	print('Problem 1: ' + str(calc_severity(wall_size, scanner_down, scanner_loc, 0)))

	delay = 0
	while 0 in undetected(delay, wall_size):
		delay += 1

	print('Problem 2: ' + str(delay))

if __name__ == '__main__':
	main()

