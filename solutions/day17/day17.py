

def main():
	jump = 356
	initial_state = [0]
	curIndex = 0

	for i in range(1,2018):
		if curIndex + jump >= len(initial_state):
			curIndex = (curIndex + jump) % len(initial_state) + 1
		else:
			curIndex += (jump + 1)
		initial_state.insert(curIndex, i)

	index2017 = initial_state.index(2017)
	print(initial_state[index2017-3:index2017+3])

	


if __name__ == '__main__':
	main()
