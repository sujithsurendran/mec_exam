#format_file
#from MyFunctions_001 import *


def calculate_rooms(students):

	MAX_CAPACITY_IF_ONLY_ONE_ROOM = 30
	ROOM_CAPACITY = 18
	ROOM_MIN_CAPACITY = 15
	NO_OF_FLEXIBLE_ROOMS = 5
	#dt=format_exam_date(input("Enter Date"))
	#students = sum(1 for line in open(dt + '.csv'))


	if students < MAX_CAPACITY_IF_ONLY_ONE_ROOM:
		rooms = 1
		print(111)
		return rooms,MAX_CAPACITY_IF_ONLY_ONE_ROOM,0

	if students < ROOM_CAPACITY*2 and students > MAX_CAPACITY_IF_ONLY_ONE_ROOM:
		rooms = 2
		print(111)
		return rooms,students//2,0

	
	if students % ROOM_CAPACITY == 0:		#18
		rooms = (students/ROOM_CAPACITY) 
		print(222)
		return rooms,ROOM_CAPACITY,0
		
	if students % (ROOM_CAPACITY - 1) == 0:		#17
		rooms =  (students/(ROOM_CAPACITY-1)) 
		print(333)
		return rooms,ROOM_CAPACITY - 1,0

	if students % (ROOM_CAPACITY - 2) == 0 and students < (ROOM_CAPACITY)*2:		#16
		rooms =  2 
		print(444)
		return rooms,ROOM_CAPACITY - 2,0


		
	if students % (ROOM_CAPACITY - 3) == 0 and students < (ROOM_CAPACITY)*2:		#15
		rooms =  2 
		print(555)
		return rooms,ROOM_CAPACITY - 3,0


	if (students % ROOM_CAPACITY) < NO_OF_FLEXIBLE_ROOMS:
		rooms = (students % ROOM_CAPACITY)
		return rooms,ROOM_CAPACITY,1


	if (students % ROOM_CAPACITY) < NO_OF_FLEXIBLE_ROOMS*2:
		rooms = (students % ROOM_CAPACITY)
		return rooms,ROOM_CAPACITY,2
		 
		
		
	"""if students % (ROOM_CAPACITY + 1) == 0:		#19
		rooms =  (students/(ROOM_CAPACITY + 1)) 
		return rooms,ROOM_CAPACITY + 1"""

	if students % ROOM_CAPACITY >= int(ROOM_CAPACITY * 0.8):	# 18 and Reminder > 14
		print(444)
		rooms =  int(students/ROOM_CAPACITY) + 1 
		return rooms, ROOM_CAPACITY + 1 

	if students % ROOM_CAPACITY >= int((ROOM_CAPACITY-1) * 0.82):	# 17 and Reminder > 14
		rooms =  int(students/(ROOM_CAPACITY-1)) + 1 
		print(555)
		return rooms, ROOM_CAPACITY - 1 

	"""if students % ROOM_CAPACITY >= INT((ROOM_CAPACITY+1) * 0.8):	# 19 and Reminder > 14
		rooms =  int(students/(ROOM_CAPACITY+1)) + 1 
		return rooms, ROOM_CAPACITY + 1 """
		
	print("No way	")	
	if students - (rooms*ROOM_CAPACITY) < 4:
		
	rooms = (students // ROOM_CAPACITY) + 1
	return rooms, ROOM_CAPACITY

while True:
	students = int(input("No. of students? "))
	rooms, capacity,one_or_two = calculate_rooms(students)

	if rooms == 1:
		print("xxxRooms = "+str(rooms) + ", Capacityxx = " + str(students))
	
	else:
		if rooms*capacity == students:
			print("yyyRooms = "+str(rooms) + ", Capacityyy = " + str(capacity) + ", Total = " + str(rooms*capacity))
		else:
			print("zzzRooms = "+str(rooms) + ", Capacityzz = " + str(capacity) + " + " + str(students - (rooms-1)*capacity)) 
	
	
	
	


