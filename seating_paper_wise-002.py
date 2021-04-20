#Step 001 ------------------------------
import csv
import sys
import os
from collections import Counter

rooms=(201,210,310,312,314)
ExamStartDate="01/03/2021"

data=sys.argv[1] if len(sys.argv) > 0 else "data.csv"
fields=[]





with open(data, "r") as csvFile, open("tmp-001.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	writer = csv.DictWriter(tmpFile, fieldnames = ["111Name","111RegNo","111Paper","111Slot"]) 
	writer.writeheader()
	
	for row in csvReader:
		Name,RegNo=row["Student"].replace(")","").split("(")
		Subject,Paper=row["Course"].replace(")","").split("(")
		Slot = row["Slot"]
		writer.writerow({'111Name':Name,'111RegNo':RegNo,'111Paper':Paper,'111Slot':Slot})

sort_key = "-k4,4 -k3,3"
os.system('sort  tmp-001.csv -t "," ' + sort_key + ' > tmp-002.csv')

#--------------------------
#Step 002 ------------------------------

ExamDate="01/03/2021"
first_time = True
with open('tmp-002.csv', "r") as csvFile, open("tmp-003.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	#fields = next(csvReader)
	writer = csv.DictWriter(tmpFile, fieldnames = ["111Name","111RegNo","111Paper","111Slot","111ExamDate","111Session"]) 
	writer.writeheader()
	
	
	for row in csvReader:
	
		Name = (row["111Name"].strip()).title()
		RegNo = (row["111RegNo"].upper()).strip()
		Paper = (row["111Paper"].upper()).strip()
		Slot = (row["111Slot"].upper()).strip()
		

		if first_time == True:
			first_time = False
		
			#tmp_slot = Slot
			tmp_paper = Paper
			
			tmp_date = ExamDate
		
			ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
			ExamSession = input("Enter Exam Session :Forenoon? ")
		
			ExamDate = tmp_date if ExamDate == '' else ExamDate
			
			
			ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate
			
			ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
			ExamSession = "Forenoon" if ExamSession == '' else ExamSession
			ExamSession = "Afternoon" if ExamSession == 'a' else ExamSession
			ExamSession = "Forenoon" if ExamSession == 'f' else ExamSession			
			

							
			
		if tmp_paper != Paper:	  

			#tmp_slot = Slot
			tmp_paper = Paper
			tmp_date = ExamDate

			ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
			ExamSession = input("Enter Exam Session :Forenoon? ")
		
			ExamDate = tmp_date if ExamDate == '' else ExamDate
			ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate
			
			ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
			ExamSession = "Forenoon" if ExamSession == '' else ExamSession
			ExamSession = "Afternoon" if ExamSession == 'a' else ExamSession
			ExamSession = "Forenoon" if ExamSession == 'f' else ExamSession			

		FormattedExamDate=ExamDate[-2:] + "/" + ExamDate[3:5] + "/" + ExamDate[:2]
		
		writer.writerow({'111Slot':Slot, '111ExamDate':FormattedExamDate, '111Session':ExamSession, '111Paper':Paper, '111RegNo':RegNo, '111Name':Name})


#--------------------------
#Step 003 ------------------------------
"""
first_time = True
no_of_records = 0
with open('tmp-003.csv', "r") as csvFile, open("tmp-004-date-count.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	writer = csv.DictWriter(tmpFile, fieldnames = ["111ExamDate","111Session","111Count","111Paper"]) 
	writer.writeheader()
	tmp_paper = ""
	
	for row in csvReader:
		
		if first_time == True:
		
			tmp_date = row['111ExamDate']
			tmp_session = row['111Session']
			tmp_paper = row['111Paper']			
							
		if tmp_date != row["111ExamDate"] or tmp_session != row['111Session']:	  
			tmp_paper = tmp_paper + ", " + row['111Paper']
			writer.writerow({'111ExamDate':tmp_date, '111Session':tmp_session, '111Count':no_of_records, '111Paper':tmp_paper})				 
			first_time = True   
			no_of_records = 1
			tmp_paper = ""

		else:
			first_time = False
			no_of_records = no_of_records +1



with open("tmp-004-date-count.csv","a") as tmpFile:		   
	writer = csv.DictWriter(tmpFile, fieldnames = ["111ExamDate","111Session","111Count","111Paper"]) 
	writer.writerow({'111ExamDate':tmp_date, '111Session':tmp_session, '111Count':no_of_records,'111Paper':tmp_paper})	 
# -------------------------


"""
"""			

first_time = True
no_of_records = 0
with open('tmp-003.csv', "r") as csvFile, open("tmp-004-date-count.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	writer = csv.DictWriter(tmpFile, fieldnames = ["111ExamDate","111Session","111Count"]) 
	writer.writeheader()

	tmp_date=""
	tmp_session=""
	tmp_slot=""
	i=1
	for row in csvReader:
	
		input("Record No:" + str(i))	

		if first_time == True:

			tmp_date = row['111ExamDate']
			tmp_session = row['111Session']
			tmp_slot = row['111Slot']
			input("First time: date = " +  tmp_date + ",   Session =" + tmp_session)
						
								   
		if tmp_date == row["111ExamDate"] and tmp_session == row['111Session']:	  

			first_time = False
			no_of_records = no_of_records + 1
			input("Only Incrementing count :" + str(no_of_records))

		else:

			input("Writing .. ." +  tmp_date + "--- " + tmp_session + " -- " + str(no_of_records) + " - Slot " + tmp_slot)
			writer.writerow({'111ExamDate':tmp_date, '111Session':tmp_session, '111Count':no_of_records})				 

			first_time = True   
			no_of_records = 1
			
		i = i+1
		tmp_date = row['111ExamDate']
		tmp_session = row['111Session']


with open("tmp-004-date-count.csv","a") as tmpFile:		   
	writer = csv.DictWriter(tmpFile, fieldnames = ["111ExamDate","111Session","111Count"]) 
	writer.writerow({'111ExamDate':tmp_date, '111Session':tmp_session, '111Count':no_of_records})	 


"""
exit()

# Find Candidates for a day ---
with open('tmp-003.csv', "r") as csvFile:
#, open("tmp-004-date-count.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	#writer = csv.DictWriter(tmpFile, fieldnames = ["111ExamDate","111Session","111Count"]) 
	#writer.writeheader()


	summary = []
	for row in csvReader:
		summary.append(row['111ExamDate'] + "-" +  row['111Session'])
		

	

with open('tmp-003.csv', "r") as csvFile:
#, open("tmp-004.csv","w") as tmpFile:
	csvReader = csv.DictReader(csvFile)
	
	# Grouped by Date & Session
	for date_session in Counter(summary):
		#print(subject,Counter(summary)[subject])
		no_of_students = Counter(summary)[date_session]


			
	
