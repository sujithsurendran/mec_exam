#MyFunctions.py
import os
from os import path
import json
import csv
import datetime

def set_fields(tmp_folder, copy_of_source_file):
	""" 
		Remove merged first line
		Add Exam Date Field
		Remove space before Course

	"""

	# Remove First row if unwanted
	#
	#fileName_1 = tmp_folder + '/1.csv'
	fileName_1 = copy_of_source_file
	
	fileName_2 = tmp_folder + '/2.csv'
	os.system('rm -rf ' + fileName_2)
	myfile = open(fileName_1, "r")
	FirstLine = myfile.readline()
	if FirstLine.find("Appearing Student") >= 0:
		myfile.close()

		os.system('echo "$(tail -n +2 ' + fileName_1 + ')" >> ' + fileName_2)
	else:
		os.system('cp ' + fileName_1 + ' ' + fileName_2 )



	# Add Exam Date field if not present
	#
	fileName_1 = tmp_folder + '/2.csv'
	fileName_2 = tmp_folder + '/3.csv'
	myfile = open(fileName_1, "r")
	FirstLine = myfile.readline()
	if FirstLine.find("Exam Date") == -1:		# if Exam Date is not present, add Exam Date
		ReplacementLine = FirstLine.rstrip('\n') + ',Exam Date,Session'
		myfile.close()

		os.system('echo "' + ReplacementLine + '">' + fileName_2 )
		os.system('echo "$(tail -n +2 ' + fileName_1 + ')" >> ' + fileName_2 )
	else:
		os.system('cp ' + fileName_1 + ' ' + fileName_2 )

		

	#fix the error of left spaces in "     Course" field
	#
	os.system("sed -i -e '1s: 	Course:Course:g' " + fileName_2) 
	os.system("sed -i -e '1s: Course:Course:g' " + fileName_2) 



def read_previous_settings():
	with open('settings.json', 'r') as openfile:
		settings = json.load(openfile)
		return settings

def write_settings(settings):
	with open('settings.json', 'w') as outfile:
		json.dump(settings, outfile)

#def add_examdate_and_session_if_not_present(tmp_folder):





		
def sort_on_date(tmp_folder):
	#sort on date if available else stuff xx-xx-xx

	fileName_1 = tmp_folder + '/3.csv'
	fileName_2 = tmp_folder + '/4.csv'
	fileName_3 = tmp_folder + '/5_sorted.csv'

	with open(fileName_1, "r") as csvFile, open(fileName_2,"w") as tmpFile:
		csvReader = csv.DictReader(csvFile)
		writer = csv.DictWriter(tmpFile, fieldnames = ["111Slot","111ExamDate","111Session","111Paper","111AdmYear","111Branch","111RegNo","111Name"]) 
		writer.writeheader()
	    
	    
		i=0
		for row in csvReader:
			i=i+1

			# 1 .Extract RegNo
			Name,RegNo=row["Student"].replace(")","").split("(")

			# 2. Extract Year of Admission
			correct_year_of_admission = False
			AdmYear = RegNo[3:5]
			for yr in (16,17,18,19,20,21,22,23,24,25,26):
				if str(yr) == AdmYear:
					correct_year_of_admission = True
					break
			if not correct_year_of_admission:
				AdmYear = RegNo[4:6]
				
			# 3. Extract Paper Code
			
			try:
				Subject,Paper=row["Course"].replace(")","").split("(")
			except ValueError:
				Subject,SubjectSpec,Paper=row["Course"].replace(")","").split("(")
				Subject = Subject + "[" + SubjectSpec + "]"
			except:
				print("Error in record of : '" + Name + ", Regno: " + RegNo + " .. " +  +". Please correct it to continue.\n " )
				exit()
				
			Slot = row["Slot"]
				
			# 4. Change date format to YYMMDD for sorting
			if len(row["Exam Date"].split('-')) == 3:
				dd,mm,yy = row["Exam Date"].split('-')
				ExamDate = yy + '-' + mm + '-' + dd
				Session = row["Session"]
			else:
				ExamDate = "xx/xx/xx"
				Session = "XX"			
			
			Branch = row["Branch Name"]
			
			
			writer.writerow({
				'111Slot':Slot,
				'111ExamDate':ExamDate,
				'111Session':Session,
				'111Paper':Paper,
				'111AdmYear':AdmYear,
				'111Branch':Branch,
				'111RegNo':RegNo,
				'111Name':Name.title()})
		    
	sort_key = "-k1,7 "    #Slot, Date, Session, Paper, RegNo
	os.system('sort ' + fileName_2 + ' -t "," ' + sort_key + ' > ' + fileName_3)		#5_sorted.csv generated
	print('\n\n\n\t' + '{:,}'.format(i) + ' records processed.')

def set_record_date(tmp_folder, fileName_1, fileName_2):


	fileName_1 = tmp_folder + fileName_1
	fileName_2 = tmp_folder + fileName_2
	#fileName_3 = tmp_folder + '/7.csv'
	timeTable = tmp_folder + '/timeTable.csv'
	ExamDate = format_exam_date()
	

	first_time = True
	with open(fileName_1, "r") as csvFile, open(fileName_2,"w") as tmpFile, open(timeTable,'w') as timeTable:
		csvReader = csv.DictReader(csvFile)

		writer = csv.DictWriter( tmpFile, fieldnames = ["111Slot","111ExamDate","111Session","111Paper","111AdmYear","111RegNo","111Name"] )
		#timeTableWriter = csv.DictWriter( timeTable, fieldnames = ["111Slot","111ExamDate","111Session","111Paper"] )
		
		writer.writeheader()
		#timeTableWriter.writeheader()
	    
		for row in csvReader:
			Name = (row["111Name"].strip()).title()
			RegNo = (row["111RegNo"].upper()).strip()
			Paper = (row["111Paper"].upper()).strip()
			Slot = (row["111Slot"].upper()).strip()
			ExamDate = (row["111ExamDate"]).strip()
			  
			AdmYear = row["111AdmYear"]
			
			Branch = RegNo.find(AdmYear)
			
			Session = row["111Session"]

			if first_time == True:
			
				first_time = False

				#tmp_slot = Slot
				tmp_paper = Paper


				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[-" + Slot + "-] -" + ExamDate + "?"))

				ExamSession = input("Enter Exam Session : " + Session + "?")

				ExamDate = format_exam_date(ExamDate)

				#NewExamDate = ExamDate
				#NewExamSession = ExamSession
				#by default session is FORENOON otherwise 'a' for AFTERNOON and 'f' for FORENOON

				ExamSession = format_session(ExamSession)

 
			if tmp_paper != Paper:	  

				#tmp_slot = Slot
				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + ExamDate + " - ? "))
				ExamSession = input("Enter Exam Session " + ExamSession + ':? ')

				ExamDate = format_exam_date(ExamDate)
				ExamSession = format_session(ExamSession)		

			writer.writerow({'111Slot':Slot, '111ExamDate':ExamDate, '111Session':ExamSession, '111Paper':Paper, '111AdmYear':AdmYear, '111RegNo':RegNo, '111Name':Name})
	#os.system('uniq -c -w 20 ' + fileName_2 + ' >> ' + tmp_folder + '/timeTable.csv')
	os.system('uniq -c -w 20 ' + fileName_2 + '|cut -d"," -f1-4|tr "," "-"  >> ' + tmp_folder + '/timeTable.csv')

"""
def set_record_date_111(tmp_folder, fileName_1, fileName_2):

	fileName_1 = tmp_folder + fileName_1
	fileName_2 = tmp_folder + fileName_2
	#fileName_3 = tmp_folder + '/7.csv'
	timeTable = tmp_folder + '/timeTable.csv'

	first_time = True
	with open(fileName_1, "r") as csvFile, open(fileName_2,"w") as tmpFile, open(timeTable,'w') as timeTable:
		csvReader = csv.DictReader(csvFile)

		writer = csv.DictWriter( tmpFile, fieldnames = ["111Slot","111ExamDate","111Session","111Paper","111AdmYear","111RegNo","111Name"] )
		#timeTableWriter = csv.DictWriter( timeTable, fieldnames = ["111Slot","111ExamDate","111Session","111Paper"] )
		
		writer.writeheader()
		#timeTableWriter.writeheader()
	    
		for row in csvReader:
			Name = (row["111Name"].strip()).title()
			RegNo = (row["111RegNo"].upper()).strip()
			Paper = (row["111Paper"].upper()).strip()
			Slot = (row["111Slot"].upper()).strip()
			ExamDate = (row["111ExamDate"]).strip()
			  
			AdmYear = row["111AdmYear"]
			
			Branch = RegNo.find(AdmYear)
			
			Session = row["111Session"]

			if first_time == True:
			
				first_time = False

				#tmp_slot = Slot
				tmp_paper = Paper


				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + ExamDate + " - ? "))

				ExamSession = input("Enter Exam Session :Forenoon? ")

				#   if  dd of dd/mm/yy is entered make complete dd/mm/yyyy			
				ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate

				# if dd/mm is entered, make complete date dd/mm/yyyy
				ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
				NewExamDate = ExamDate
				NewExamSession = ExamSession
				#by default session is FORENOON otherwise 'a' for AFTERNOON and 'f' for FORENOON

				ExamSession = format_session(NewExamSession)

 
			if tmp_paper != Paper:	  

				#tmp_slot = Slot
				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + ExamDate + " - ? "))
				ExamSession = input("Enter Exam Session " + ExamSession + ':? ')

				ExamDate = tmp_date if ExamDate == '' else ExamDate
				ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate

				ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
				ExamSession = format_session(ExamSession)		

			writer.writerow({'111Slot':Slot, '111ExamDate':NewExamDate, '111Session':NewExamSession, '111Paper':Paper, '111AdmYear':AdmYear, '111RegNo':RegNo, '111Name':Name})
	#os.system('uniq -c -w 20 ' + fileName_2 + ' >> ' + tmp_folder + '/timeTable.csv')
	os.system('uniq -c -w 20 ' + fileName_2 + '|cut -d"," -f1-4|tr "," "-"  >> ' + tmp_folder + '/timeTable.csv')
"""

def change_date(tmp_folder,source_file):
	timeTable = tmp_folder + '/' + source_file
	 
	timeTablecsv = open(timeTable,"r")
	for exam_record in timeTablecsv:
		newDate = input("Change " + exam_record[2:] + ' to => :?')
	
	timeTablecsv.close()
	
def format_session(NewExamSession = "FN"):
	if NewExamSession == "":
		NewExamSession = "FN"
	elif NewExamSession.upper() == "A" or NewExamSession.upper() == "AN":
		NewExamSession = "AN"
	elif NewExamSession.upper() == "F" or NewExamSession.upper() == "FN":
		NewExamSession = "FN"
	elif NewExamSession.upper() == "FORENOON":
		NewExamSession = "FN"
	elif NewExamSession.upper() == "AFTERNOON":
		NewExamSession = "AN"

	return NewExamSession



def format_exam_date(dt=datetime.datetime.now().strftime("%d-%m-%y")):

	print(">>" + dt)

	#   if  dd of dd-mm-yy is entered make complete dd-mm-yyyy
	if len(str(dt)) == 2 or len(str(dt)) == 1:
		
		dt = (f'{int(dt):02}') + datetime.datetime.now().strftime("%d-%m-%y")[-6:]  
		
	elif len(str(dt)) == 5:

		# if dd/mm is entered, make complete date dd-mm-yyyy
		dt = dt + prev_dt[-3:]
	elif len(str(dt)) > 8:
		print("Invalid date - dd-mm-yy is the expected date format")

	print(dt)
	
	if valid_date_string(dt):
		return dt
	else:
		print("Invalid date")
		exit()


def valid_date_string(dt):

	format = "%d-%m-%y"
	try:
		datetime.datetime.strptime(dt, format)
		return True
	except ValueError:
		return False
		

def get_exams_on_a_date(tmp_folder, source_file):
	source_file = tmp_folder + source_file
	current_slot = input("Enter Slot(regEx allowed): ")
	current_exam_date = input("Enter Date:(dd-mm-yy) ")
	current_exam_date = format_exam_date(current_exam_date)
	input(current_exam_date)
	current_filter = input("Any filter format for Paper(like MAT102 or just 102 regex) ? ")
	
	
	# field 4 = Paper
	# field 1 = Slot

	os.system('egrep "^' + current_slot + '" ' + source_file + '| cut -d "," -f 4 |egrep "' + current_filter + '"|uniq > ' + current_exam_date + '_papers.csv' )
	
	prepare_candidates_for_the_date(current_exam_date, source_file)

def prepare_candidates_for_the_date(current_exam_date, source_file):
	os.system("paste -s -d '|' " + current_exam_date + '_papers.csv | tr -d " "> ' + current_exam_date + '_papers.txt')
	PaperFile = current_exam_date + '_papers.txt'
	myfile = open(PaperFile, "r")
	exams = myfile.readline()
	#os.system('echo "' + current_exam_date + '\n Seating Arrangement" >' + current_exam_date + '.csv')
	os.system('egrep "' + exams[:-1]  + '" '+ source_file + '>> ' + current_exam_date + '.csv')




