
#!/usr/bin/python3
#Name: Takanori Ohashi

import sys
import random

def open_file(file_name):
	file = open(file_name, "r")
	disk_location = file.readlines()
	newlist = []
	output = []
	for i in disk_location:
		 i = i.replace('\n', '')
		 newlist.append(i)
	for i in newlist:
		dist = int(i)
		output.append(dist)
	return output

def create_rand():
	f = open("in2.txt", "w")
	for i in range(100):
		r = random.randint(0, 5000)
		f.write(str(r))
		f.write("\n")
	f.close()

def distance_traveled(disk1, disk2):
	return abs(disk2 - disk1)

def FCFS(file_content, init_pos):
	init_pos = abs(init_pos)
	total = 0
	idx = 0
	while idx < len(file_content):
		if idx == 0:
			d = distance_traveled(init_pos, file_content[idx])
			total += d
		else:
			prev_disk = file_content[idx - 1]
			current = file_content[idx]
			d = distance_traveled(prev_disk, current)
			total += d
		idx += 1
	print("FCFS", total)

def SSTF(file_content, init_pos):
	init_pos = abs(init_pos)
	total = 0
	flag = 0
	while len(file_content) > 0:
		if flag == 0:
			prev_disk = init_pos
			closest = file_content[0]
			d = distance_traveled(prev_disk, closest)
			for disk in file_content:
				if distance_traveled(prev_disk, disk) < d:
					closest = disk
			d = distance_traveled(prev_disk, closest)
			file_content.remove(closest)
			total += d
			flag = 1
		else:
			prev_disk = closest
			closest = file_content[0]
			for disk in file_content:
				if distance_traveled(prev_disk, disk) < distance_traveled(prev_disk, closest):
					closest = disk
			d = distance_traveled(prev_disk, closest)
			file_content.remove(closest)
			total += d
	print("SSTF", total)

def SCAN(file_content, init_pos):
	total = 0
	direction = "out"
	if int(init_pos) < 0:
		direction = "in"
	else:
		direction = "out"
	flag = 0
	current = abs(init_pos)
	while len(file_content) > 0:
		if flag == 0:
			if current in file_content:
				file_content.remove(current)
			if direction == "in":
				current -= 1
			else: #out
				if current == 4999:
					direction = "in"
					current -= 1
				else:
					current += 1
			flag = 1
		else:
			if current in file_content:
				file_content.remove(current)
			if direction == "in":
				if current == 0:
					current += 1
					direction = "out"
					total += 1
				else:
					current -= 1
					total += 1
			else: #out
				if current == 4999:
					current -= 1
					direction = "in"
					total += 1
				else:
					current += 1
					total += 1
	print("SCAN", total)

def CSCAN(file_content, init_pos):
	total = 0
	direction = "out"
	if int(init_pos) < 0:
		direction = "in"
	else:
		direction = "out"
	flag = 0
	current = abs(init_pos)
	if direction == "out":
		while len(file_content) > 0:
			if flag == 0:
				if current in file_content:
					file_content.remove(current)
				if current == 4999:
					current = 0
				flag = 1
			else:
				if current in file_content:
					file_content.remove(current)
				if current == 4999:
					current = 0
					total += 4998
				else:
					current += 1
					total += 1
	else:
		while len(file_content) > 0:
			if flag == 0:
				if current in file_content:
					file_content.remove(current)
				if current == 0:
					current = 4999
				flag = 1
			else:
				if current in file_content:
					file_content.remove(current)
				if current == 0:
					current = 4999
					total += 4998
				else:
					current += 1
					total += 1
	print("C-SCAN", total)

def LOOK(file_content, init_pos):
	total = 0
	direction = "out"
	if int(init_pos) < 0:
		direction = "in"
	else:
		direction = "out"
	flag = 0
	current = abs(init_pos)
	max1 = file_content[0]
	for item in file_content:
		if item > max1:
			max1 = item
	max1 = int(max1)
	min1 = file_content[0]
	for item in file_content:
		if item < min1:
			min1 = item
	min1 = int(min1)
	while len(file_content) > 0:
		if flag == 0:
			if current in file_content:
				file_content.remove(current)
			if direction == "in":
				current -= 1
			else: #out
				if current == max1:
					direction = "in"
					current -= 1
				else:
					current += 1
			flag = 1
		else:
			if current in file_content:
				file_content.remove(current)
			if direction == "in":
				if current == min1:
					current += 1
					direction = "out"
					total += 1
				else:
					current -= 1
					total += 1
			else: #out
				if current == max1:
					current -= 1
					direction = "in"
					total += 1
				else:
					current += 1
					total += 1
	print("LOOK", total)

def CLOOK(file_content, init_pos):
	total = 0
	direction = "out"
	if int(init_pos) < 0:
		direction = "in"
	else:
		direction = "out"
	flag = 0
	current = abs(init_pos)
	max1 = file_content[0]
	for item in file_content:
		if item > max1:
			max1 = item
	max1 = int(max1)
	min1 = file_content[0]
	for item in file_content:
		if item < min1:
			min1 = item
	min1 = int(min1)
	if direction == "out":
		while len(file_content) > 0:
			if flag == 0:
				if current in file_content:
					file_content.remove(current)
				if current == max1:
					current = min1
				flag = 1
			else:
				if current in file_content:
					file_content.remove(current)
				if current == max1:
					current = min1
					total += (max1 - min1 - 1)
				else:
					current += 1
					total += 1
	else:
		while len(file_content) > 0:
			if flag == 0:
				if current in file_content:
					file_content.remove(current)
				if current == min1:
					current = max1
				flag = 1
			else:
				if current in file_content:
					file_content.remove(current)
				if current == min1:
					current = max1
					total += (max1 - min1 - 1)
				else:
					current += 1
					total += 1
	print("C-LOOK", total)


def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print("usage: diskSim INITIAL_POSITION [ACCESS_SEQUENCE_FILE")
		sys.exit()
	init_pos = int(sys.argv[1])
	if len(sys.argv) == 2:
		create_rand()
		filename = "in2.txt"
	else:
		filename = sys.argv[2]
	fcfs_content = open_file(filename)
	sstf_content = open_file(filename)
	scan_content = open_file(filename)
	cscan_content = open_file(filename)
	look_content = open_file(filename)
	clook_content = open_file(filename)

	FCFS(fcfs_content, init_pos)
	SSTF(sstf_content, init_pos)
	SCAN(scan_content, init_pos)
	CSCAN(cscan_content, init_pos)
	LOOK(look_content, init_pos)
	CLOOK(clook_content, init_pos)


if __name__ == "__main__":
	main()




