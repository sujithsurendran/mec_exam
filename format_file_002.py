#format_file
#from MyFunctions_001 import *



#def fetch_rooms():
students = 71
details=[]
rooms=[]
capacities=[]
max_capacities=[]
current_capacities=[]
i=1
with open("./rooms.txt") as file1:
	for line in file1:
		line_i = line.rstrip()
		details = line_i.split(",")
		rooms.append(details[0])
		capacities.append(details[1])
		max_capacities.append(details[2])
		current_capacities.append(details[3])
		
		i = i + 1
	#return rooms, capacities, max_capacities, current_capacities

#rooms, capacities,max_capacities,current_capacities = fetch_rooms()

i=0
total=0
for room,capacity,max_capacity,current_capacity in zip(rooms,capacities,max_capacities,current_capacities):
		print(str(room) + "=>" + str(capacity) )
		total = total + int(capacity)
		if total>=students:
			print("Total = " + str(total))	
		#print(capacity)
		#print(max_capacity)
		#print(current_capacity)

		
		
		
