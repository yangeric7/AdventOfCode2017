
def contains(connections, startKey):
	groupList = []
	findConnections(connections, groupList, startKey)
	return len(groupList)

def findConnections(connections, groupList, program):
	if program in groupList:
		return

	groupList.append(program)
	for conn in connections[program]:
		findConnections(connections, groupList, conn)
		connections.pop(conn,None)


def main():
	with open('input.txt','r') as input_file:
		programs = [line.strip().replace(',','').split(' ') for line in input_file]

	connections = {}
	for program in programs:
		connections[program[0]] = program[2:]

	print('Problem 1: ' + str(contains(dict(connections),'0')))

	groupCount = 0
	while len(connections) > 0:
		contains(connections,connections.keys()[0])
		groupCount += 1

	
	print('Problem 2: ' + str(groupCount))

if __name__ == '__main__':
	main()