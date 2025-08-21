import numpy as numpy

def cardinal_counter(pos, direction_vec, n, grid, grid_m):
	card_list = []
	for i in range(n):
		if((not(pos[0]+i*direction_vec[0] < 0) and not(pos[1]+i*direction_vec[1] < 0)) and (not(pos[0]+i*direction_vec[0] > grid_m-n) and not(pos[1]+i*direction_vec[1] > grid_m-n))):
			card_list.append(grid[pos[0]+i*direction_vec[0]][pos[1]+i*direction_vec[1]])
		else:
			return card_list
	return card_list

def read_sdf(file_path):
	read_arr = []
	read_stream = open(file_path)

	line = []
	val = []

	for i in read_stream.read():
		if(i == ' '):
			val = val[0]*10+val[1]
			line.append(val)
			val = []
		elif(i == '\n'):
			read_arr.append(line)
			line = []
		else:
			val.append(int(i))
	read_stream.close()
	return read_arr



arr = read_sdf("_grid_count_data.sdf")
dir_arr = []

for i in range (3):
	for j in range(3):
		dir_vec = [i%3-1,j-1]
		if(dir_vec != [0,0]):
			dir_arr.append(dir_vec)
pos = [0,0]

max_val = 0

for i in arr:
	for j in i:
		for k in dir_arr:
			cur_arr = cardinal_counter(pos, k, 4, arr, len(arr))
			cur_prod = 1
			for h in cur_arr:
				cur_prod = cur_prod*h
			if(cur_prod > max_val):
				max_val = cur_prod
		pos[1] += 1
	pos[0] += 1
	pos[1] = 0

print(max_val)