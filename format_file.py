#format_file
#from MyFunctions_001 import *


def calculate_rooms():
	students = int(input("No. of students? "))
	room_capacity = 18
	#dt=format_exam_date(input("Enter Date"))
	#students = sum(1 for line in open(dt + '.csv'))

	reminder =  students % room_capacity
	if reminder == 0 or room_capacity-reminder < 3:
		rooms = students/room_capacity
		return 		 
	else:
		room_capacity = room_capacity -1
		reminder =  students % room_capacity
		if reminder == 0 or room_capacity-reminder < 2:
			rooms = students/room_capacity
		else:
			room_capacity = room_capacity -1
			reminder =  students % room_capacity
			if reminder == 0 or room_capacity-reminder < 2:
				rooms = students/room_capacity

	room_1 = int(students/room_capacity)
	print("Total = " + str(students))
	print(str(room_capacity) + " x " + str(room_1) + " = " + str(room_1 * room_capacity) )
	print("\t"+ str(students-room_capacity*room_1))


while True:
	calculate_rooms()


