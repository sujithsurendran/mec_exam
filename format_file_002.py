#format_file
#from MyFunctions_001 import *

#def fetch_rooms():
while True:
	students = 30
	students = int(input("Students"))
	alter = int(input("Alteration?"))
	if alter == "":
		alter = 0
		
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

			capacity = int(details[1]) + alter
			
			if capacity >= students:
				capacities.append(students)
				for room1, capacity1 in zip(rooms,capacities):
					print(room1 + "=>" + str(capacity1))

				exit()
			else:
				#print(capacities)
				#print(rooms)
				if students>=0:
					students = students - capacity 
					capacities.append(capacity)
					print(students)
				else:
					exit()

		
			
		
		



	#for room,capacity,max_capacity,current_capacity in zip(rooms,capacities,max_capacities,current_capacities):
	
