#format_file
#from MyFunctions_001 import *


def calculate_rooms(students):

	MAX_CAPACITY_IF_ONLY_ONE_ROOM = 30
	ROOM_CAPACITY = 18
	
	
	room_capacity = 18
	#dt=format_exam_date(input("Enter Date"))
	#students = sum(1 for line in open(dt + '.csv'))


	if students < MAX_CAPACITY_IF_ONLY_ONE_ROOM:
		rooms = 1
		return rooms
	
	if students % ROOM_CAPACITY == 0:		#18
		rooms = (students/ROOM_CAPACITY) 
		return rooms,ROOM_CAPACITY
		
	if students % (ROOM_CAPACITY - 1) == 0:		#17
		rooms =  (students/(ROOM_CAPACITY-1)) 
		return rooms,ROOM_CAPACITY - 1

	"""if students % (ROOM_CAPACITY + 1) == 0:		#19
		rooms =  (students/(ROOM_CAPACITY + 1)) 
		return rooms,ROOM_CAPACITY + 1"""

	if students % ROOM_CAPACITY >= INT(ROOM_CAPACITY * 0.8):	# 18 and Reminder > 14
		rooms =  int(students/ROOM_CAPACITY) + 1 
		return rooms, ROOM_CAPACITY + 1 

	if students % ROOM_CAPACITY >= INT((ROOM_CAPACITY-1) * 0.8):	# 17 and Reminder > 14
		rooms =  int(students/(ROOM_CAPACITY-1)) + 1 
		return rooms, ROOM_CAPACITY - 1 

	"""if students % ROOM_CAPACITY >= INT((ROOM_CAPACITY+1) * 0.8):	# 19 and Reminder > 14
		rooms =  int(students/(ROOM_CAPACITY+1)) + 1 
		return rooms, ROOM_CAPACITY + 1 """
		
		
	rooms = (students // ROOM_CAPACITY) + 1
	return rooms, ROOM_CAPACITY

while True:
	students = int(input("No. of students? "))
	rooms, capacity = calculate_rooms(students)
	
	if rooms*capacity == students:
		print("Rooms = "+str(rooms) + ", Capacity = " + str(capacity) + "=" + str(rooms*capacity))
	else:
		print("Rooms = "+str(rooms-1) + ", Capacity = " + str(capacity) + str(students - (rooms-1)*capacity)) 
	
	
	
	


