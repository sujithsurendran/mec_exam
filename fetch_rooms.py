def input_papers(source_file):
	paper="XXX"
	grep_str = "Student|"
	dt = input("Date(dd-mm-FN/AN)?")
	while paper != "":
		paper = input("Enter paper...")
		grep_str = grep_str + "|" + paper
	os.system("egrep " + grep_str[:-1] + " " + source_file + " > " + dt + ".csv")
	return len(open(dt + ".csv").readlines(  ))
	

def fetch_rooms(students=0):
	if students == "" or students == "0":
		return nil
	
	alter = input("Alteration?")
	if alter == "":
		alter = 0
	else:
		alter = int(alter)
		
	details=[]
	rooms=[]
	capacities=[]
	max_capacities=[]
	current_capacities=[]

	total = 0
	with open("./rooms.txt") as file1:
		for line in file1:
			line_i = line.rstrip()
			details = line_i.split(",")
			rooms.append(details[0])
			
			max_capacities.append(details[2])
			current_capacities.append(details[3])

			capacity = int(details[3]) + alter
			
			if capacity >= students:
				capacities.append(students)
				return capacities,rooms
				#for room1, capacity1 in zip(rooms,capacities):
				#	print(room1 + "=>" + str(capacity1))
				exit()
			else:

				students = students - capacity
				if students>0:
					capacities.append(capacity)


	

students = input_papers("s6.csv")
print("Student Count = " + str(students))
exit()

capacities,rooms = fetch_rooms(students)
for room1, capacity1 in zip(rooms,capacities):
	print(room1 + "=>" + str(capacity1))








"""

while True:
	students = 30
	students = input("Students")
	if students == "" or students == "0":
		exit()
	else:
		students = int(students)	
	
	alter = input("Alteration?")
	if alter == "":
		alter = 0
	else:
		alter = int(alter)
		
	details=[]
	rooms=[]
	capacities=[]
	max_capacities=[]
	current_capacities=[]

	total = 0
	with open("./rooms.txt") as file1:
		for line in file1:
			line_i = line.rstrip()
			details = line_i.split(",")
			rooms.append(details[0])
			
			max_capacities.append(details[2])
			current_capacities.append(details[3])

			capacity = int(details[3]) + alter
			
			if capacity >= students:
				capacities.append(students)
				for room1, capacity1 in zip(rooms,capacities):
					print(room1 + "=>" + str(capacity1))
				exit()
			else:

				students = students - capacity
				if students>0:
					capacities.append(capacity)


	for room1, capacity1 in zip(rooms,capacities):
		print(room1 + "=>" + str(capacity1))	
			
	
		


"""	
