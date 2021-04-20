#Step 001 ------------------------------
import csv
import sys
import os
from collections import Counter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue, black, grey


Exam='B.Tech s4, Supplementary'
ExamDate="19/03/2021"
Session="FN"
no_of_records = 134
#no_of_records = int(input("Enter Number of records"))
#no_of_records=int(input("Enter no of Records"))
max_capacity = 28
#data=sys.argv[1] if len(sys.argv) > 0 else "tmp-003.csv"
fields=[]
no_of_rooms=0
candidates_per_room = 0
candidates_in_last_room = 0
first_time = True

if no_of_records < max_capacity:
    no_of_rooms = 1
    candidates_per_room = no_of_records
    candidates_in_last_room = no_of_records
    
else:
    
	for i in (25,26,27):
		if no_of_records % i == 0 and first_time==True:
			no_of_rooms = no_of_records/i
			candidates_per_room = i
			candidates_in_last_room = i
			first_time = False


if first_time :
	surplus = no_of_records % 26
	input("Surplus  = " + str(surplus) + ", no of records = " + str(no_of_records))
	if surplus/(no_of_records / 26) <=2:
		#input(surplus/int(no_of_records / 28))
		candidates_per_room = 28
		no_of_rooms = (no_of_records // 28) 
		candidates_in_last_room = no_of_records - (no_of_rooms * candidates_per_room)
	else:
		no_of_rooms = (no_of_records//26) + 1
		candidates_per_room = no_of_records // no_of_rooms
		candidates_in_last_room = no_of_records - ((no_of_rooms-1) * candidates_per_room) 



#if not first_time:
#	no_of_rooms = no_of_rooms + 1	
	
	
input("Capacity = "+str(candidates_per_room)+", Rooms "+str(no_of_rooms)+",  candidates_per_room x no_of_rooms = "+str(candidates_per_room * no_of_rooms)+",  candidates_in_last_room="+str(candidates_in_last_room) )

change_series = True
rooms=(201,210,211,301,309,310,311,312,314,315,409,410,509,510,511)
with open("a.csv", "r") as csvFile, open("tmp-004.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	
	
	writer = csv.DictWriter(tmpFile, fieldnames = ["111Room","111Seat","111Name","111RegNo","111Paper","111Slot","111ExamDate","111Session"]) 
	writer.writeheader()
	room_i = 0
	seat_i = 1
	i = 1
	
	a_nos = (candidates_per_room//2)
	a_series = no_of_rooms * a_nos + (candidates_in_last_room//2)
    #a_series = no_of_records//2

	for row in csvReader:
		#input("seat_i = " + str(seat_i) + "i=" +str(i))

		room = rooms[room_i]
		
		if i <= a_series:
			seat = f'A{seat_i:02}'
			writer.writerow({'111Room':room, '111Seat':seat, '111Paper':row['111Paper'], '111RegNo':row['111RegNo'], '111Name':row['111Name']})

		if i > a_series:
			seat = f'B{seat_i:02}'
			writer.writerow({'111Room':room, '111Seat':seat, '111Paper':row['111Paper'], '111RegNo':row['111RegNo'], '111Name':row['111Name']})

		
		
		#input("i = " + str(i) + ", seat_i" + str(seat_i) + ", candidates_per_room = " + str(candidates_per_room) + "Mod = " + str(seat_i % (candidates_per_room//2)))
	
		if seat_i % (candidates_per_room//2) == 0:
		
			seat_i =  0
			room_i = room_i + 1
			
		if i == a_series:
			room_i = 0
			seat_i = 0

		i = i + 1
		seat_i = seat_i + 1		
					
#os.system('cat tmp-004.csv')
sort_key = "-k1,2"
os.system('sort  tmp-004.csv -t "," ' + sort_key + ' > tmp-005.csv')



# printing Room No: as heading

first_time = True
page_i = 0
room_i = '201'

with open("tmp-005.csv", "r") as csvFile:
	csvReader = csv.DictReader(csvFile)
	
	for row in csvReader:

		if room_i != row['111Room']:
			x1 = 0.5 * inch		
			canvas.drawString(x1, 20, '           Invigillator_________________________   Sign________')
			canvas.save()
			first_time = True
			page_i = page_i+1
			room_i = row['111Room']
	
		if first_time:


		
		
			fileName = '/home/sujith/Documents/prg/' + ExamDate.replace('/', '.') + '.pdf'
			fileName = '/home/sujith/Documents/prg/aaa' + str(page_i) + '.pdf'
			canvas = Canvas(fileName, pagesize=A4)

			height, width = A4
	        
			y = width - 0.5 * inch
			x1 = 0.5 * inch


			i=0
		
	        #   Heading
			canvas.setFont("Courier-Bold", 18)
			canvas.setFillColor(blue)
			canvas.drawString(x1, y, Exam + ' - ' + ExamDate.replace('/', '.') + ', ' + row['111Session'] + ', Room:' + row['111Room'] + 'FN') 
			# + ', ' + row['111Session'])




			canvas.setFont("Courier-Bold", 12)
			canvas.setFillColor(grey)

	        
			x1 = 0.5 * inch
			x2 = x1 + 0.5 * inch
			x3 = x2 + 2.7 * inch
			x4 = x3 + 1.5 * inch
			x5 = x4 + 0.1 * inch
			x6 = x5 + 1 * inch
			x7 = x6 + 1 * inch
			#y = width - inch
			canvas.drawString(x1, y - .5*inch, 'Seat')
			canvas.drawString(x2, y - .5*inch, 'Name')
			canvas.drawString(x3, y - .5*inch, 'RegisterNo:')
			canvas.drawString(x4, y - .5*inch, 'Paper')
			canvas.drawString(x1, y - .5*inch, '__________________________________________________________________')
			y = width - 1.25 * inch
					


			first_time = False

		if i % 2 == 0:
			canvas.setFont("Courier", 14)
			canvas.setFillColor(black)
		else:
			canvas.setFont("Courier", 14)
			canvas.setFillColor(grey)
		
		
		
		canvas.drawString(x1, y, row['111Seat'])
		canvas.drawString(x2, y, row['111Name'][0:22])
		canvas.drawString(x3, y, row['111RegNo'])
		canvas.drawString(x4, y, row['111Paper'])
		canvas.drawString(x1, y, '__________________________________________________________________')

		x1 = 0.5 * inch
		x2 = x1 + 0.5 * inch
		x3 = x2 + 2.7 * inch
		x4 = x3 + 1.5 * inch
		x5 = x4 + 0.1 * inch
		x6 = x5 + 1 * inch
		x7 = x6 + 1 * inch
        
		i=i+1
		y = y - .3 * inch

x1 = 0.5 * inch		
canvas.drawString(x1, 20, '           Invigillator_________________________   Sign________')

canvas.save()
        
os.system('pdftk aaa*.pdf cat output Seating.pdf')

