#MyFunctions.py
import os
from os import path
import json
import csv
import datetime

def set_fields(tmp_folder, copy_of_source_file):


	# Remove First row if unwanted
	#

	heading_removed_file = tmp_folder + '/heading_removed_file.csv'
	os.system('rm -rf ' + heading_removed_file)
	myfile = open(copy_of_source_file, "r")
	FirstLine = myfile.readline()
	if FirstLine.find("Appearing Student") >= 0:
		myfile.close()

		os.system('echo "$(tail -n +2 ' + copy_of_source_file + ')" >> ' + heading_removed_file)
	else:
		os.system('cp ' + copy_of_source_file + ' ' + heading_removed_file )



	# Add Exam Date field if not present
	#
	#fileName_1 = tmp_folder + '/2.csv'
	ExamDateAndSessionAdded = tmp_folder + '/exam_date_and_session_added.csv'
	
	
	
	myfile = open(heading_removed_file, "r")
	FirstLine = myfile.readline()
	if FirstLine.find("Exam Date") == -1:
		ReplacementLine = FirstLine.rstrip('\n') + ',Exam Date,Session'
		myfile.close()

		os.system('echo "' + ReplacementLine + '">' + ExamDateAndSessionAdded )
		os.system('echo "$(tail -n +2 ' + heading_removed_file + ')" >> ' + ExamDateAndSessionAdded )
	else:
		os.system('cp ' + heading_removed_file + ' ' + ExamDateAndSessionAdded )

		

	#fix the error of left spaces in "     Course" field
	#
	os.system("sed -i -e '1s: 	Course:Course:g' " + ExamDateAndSessionAdded) 
	os.system("sed -i -e '1s: Course:Course:g' " + ExamDateAndSessionAdded) 



def read_previous_settings():
	with open('settings.json', 'r') as openfile:
		settings = json.load(openfile)
		return settings

def write_settings(settings):
	with open('settings.json', 'w') as outfile:
		json.dump(settings, outfile)

#def add_examdate_and_session_if_not_present(tmp_folder):





		
def sort_on_date(tmp_folder):
	fileName_1 = tmp_folder + '/3.csv'
	exam_date_and_session_added_file = tmp_folder + '/exam_date_and_session_added.csv' 
	fileName_2 = tmp_folder + '/4.csv'
	fileName_3 = tmp_folder + '/5.csv'

	with open(exam_date_and_session_added_file, "r") as csvFile, open(fileName_2,"w") as tmpFile:
		csvReader = csv.DictReader(csvFile)
		writer = csv.DictWriter(tmpFile, fieldnames = ["111Slot","111ExamDate","111Session","111Paper","111AdmYear","111RegNo","111Name"]) 
		writer.writeheader()
	    
	    
		i=0
		for row in csvReader:
			i=i+1
			#print('=>' + row["Student"] + '<=')
			Name,RegNo=row["Student"].replace(")","").split("(")
			correct_year_of_admission = False
			AdmYear = RegNo[3:5]
			for yr in (16,17,18,19,20,21,22,23,24,25,26):
				if str(yr) == AdmYear:
					correct_year_of_admission = True
					break
			if not correct_year_of_admission:
				AdmYear = RegNo[4:6]
			
			Subject,Paper=row["Course"].replace(")","").split("(")
			Slot = row["Slot"]
			
			if len(row["Exam Date"].split('-')) == 3:
				dd,mm,yy = row["Exam Date"].split('-')
				ExamDate = yy + '-' + mm + '-' + dd
				Session = row["Session"]
			else:
				ExamDate = "xx/xx/xx"
				Session = "XX"			
			
			
			writer.writerow({
				'111Slot':Slot,
				'111ExamDate':ExamDate,
				'111Session':Session,
				'111Paper':Paper,
				'111AdmYear':AdmYear,
				'111RegNo':RegNo,
				'111Name':Name.title()})
		    
	sort_key = "-k1,6 "    #Slot, Date, Session, Paper, RegNo
	os.system('sort ' + fileName_2 + ' -t "," ' + sort_key + ' > ' + fileName_3)
	print('\n\n\n\t' + '{:,}'.format(i) + ' records processed.')



def set_record_date(tmp_folder, fileName_1, fileName_2):

	fileName_1 = tmp_folder + fileName_1
	fileName_2 = tmp_folder + fileName_2
	#fileName_3 = tmp_folder + '/7.csv'
	timeTable = tmp_folder + '/timeTable.csv'

	first_time = True

	tmp_date = ""
	tmp_session = ""



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
			ExamDate =  (row["111ExamDate"]).strip()
			AdmYear = row["111AdmYear"]
			
			pos = RegNo.find(AdmYear) + 2
			Branch = RegNo[pos:pos+2]
			Paper = Branch + '-' + Paper
			Session = row["111Session"]


			if ExamDate == "xx/xx/xx" or ExamDate == "":
				tmp_date = ExamDate
			else:
				i=0
				
			if Session.upper() != "XX":
				tmp_session = Session


			if first_time == True:
				first_time = False

				#tmp_slot = Slot
				tmp_paper = Paper
				
				ExamDate = str(input("first time => Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + ExamDate + " - ? "))
				ExamSession = input("Enter Exam Session :" + Session + "? ")
				ExamDate = format_exam_date(ExamDate)
				ExamSession = format_session(ExamSession)
				
		

			#input("next record : ExamDate = " + ExamDate + ", tmp_date = " + tmp_date)
			if tmp_paper != Paper:	  

				#input("Paper change" + "next record : ExamDate = " + ExamDate + ", tmp_date = " + tmp_date)
				tmp_paper = Paper
<<<<<<< HEAD

=======
				tmp_date = ExamDate
				tmp_session = Session

				NewExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
				NewExamSession = input("Enter Exam Session " + tmp_session + ':? ')

				ExamDate = tmp_date if ExamDate == '' else ExamDate
				ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate

				ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
				if NewExamSession == "":
					NewExamSession = "FN"
				elif NewExamSession.upper() == "A" or NewExamSession.upper() == "AN":
					NewExamSession = "AN"
				elif NewExamSession.upper() == "F" or NewExamSession.upper() == "FN":
					NewExamSession = "FN"
				elif NewExamSession.upper() == "FN":
					NewExamSession = "Forenoon"
				elif NewExamSession.upper() == "AN":
					NewExamSession = "AN"	
>>>>>>> 977b6db46a42f95fac400638ea7208561cfc88b2
					

				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
				ExamSession = input("Enter Exam Session :" +  tmp_session + "? ")
				
				if ExamDate == "":
					ExamDate = tmp_date
					
				if ExamSession == "":
					ExamSession = tmp_session

				ExamDate = format_exam_date(ExamDate)
				ExamSession = format_session(ExamSession)	
					
		

			writer.writerow({'111Slot':Slot, '111ExamDate':ExamDate, '111Session':ExamSession, '111Paper':Paper, '111AdmYear':AdmYear, '111RegNo':RegNo, '111Name':Name})
	#os.system('uniq -c -w 20 ' + fileName_2 + ' >> ' + tmp_folder + '/timeTable.csv')
	os.system('uniq -c -w 20 ' + fileName_2 + '|cut -d"," -f1-4|tr "," "-"  >> ' + tmp_folder + '/timeTable.csv')
<<<<<<< HEAD
	
	
def format_session(NewExamSession):
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
	
def format_exam_date(dt="", prev_dt=datetime.datetime.now().strftime("%d/%m/%y")):

	if dt == "":
		dt = prev_dt

	#   if  dd of dd/mm/yy is entered make complete dd/mm/yyyy			
	dt = (f'{int(dt):06}') + prev_dt[-6:]  if len(str(dt)) <= 2 else dt

	# if dd/mm is entered, make complete date dd/mm/yyyy
	dt = dt + prev_dt[-3:] if len(str(dt)) == 5 else dt
	return dt
	
=======


def change_date(tmp_folder,source_file):
	timeTable = tmp_folder + '/' + source_file
	 
	timeTablecsv = open(timeTable,"r")
	for exam_record in timeTablecsv:
		newDate = input("Change " + exam_record[2:] + ' to => :?')
	
	timeTablecsv.close()
	



"""

def extract_data_and_name_fields(data):



# -------------- - --------------
def fetch_fields_and_rename_cols(data):
    
	#os.system("sed -i -e '1s: ::g' " + data) #fix the error of left spaces in "     Course" field
	os.system("sed -i -e '1s: 	Course:Course:g' " + data) #fix the error of left spaces in "     Course" field

	#kkkk=input("This is th eone " + data)
	with open(data, "r") as csvFile, open("tmp/tmp-001.csv","w") as tmpFile:
		csvReader = csv.DictReader(csvFile)
		writer = csv.DictWriter(tmpFile, fieldnames = ["111Name","111RegNo","111Paper","111Slot","111ExamDate","111Session"]) 
		writer.writeheader()
	    
		for row in csvReader:
			#k = input(row["Course"])
			Name,RegNo=row["Student"].replace(")","").split("(")
			Subject,Paper=row["Course"].replace(")","").split("(")
			Slot = row["Slot"]
			
			#ExamDate = row["Exam Date"]
			ExamDate = "15/04/2021"
			 
			#Session = row["Session"]
			Session = "FN"
			
			if(ExamDate.strip() == ""):
				ExamDate = "xx-xx-xxxx"
				Session = "xxx"
			writer.writerow({'111Name':Name,'111RegNo':RegNo,'111Paper':Paper,'111Slot':Slot,'111ExamDate':ExamDate,'111Session':Session})
			#writer.writerow({'111Name':Name,'111RegNo':RegNo,'111Paper':Paper,'111Slot':Slot})
		    
		sort_key = "-k5,5 -k6,6 -k7,7 -k4,4 -k3,3"    #Slot, Date, Session, Paper, RegNo
		print('sort  tmp/tmp-001.csv -t "," ' + sort_key + ' > tmp/tmp-002.csv')
		os.system('sort  tmp/tmp-001.csv -t "," ' + sort_key + ' > tmp/tmp-002.csv')
		"""
>>>>>>> 977b6db46a42f95fac400638ea7208561cfc88b2
