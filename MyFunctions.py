#MyFunctions.py
import os
from os import path
import json
import csv


def set_fields(tmp_folder):


	# Remove First row if unwanted
	#
	fileName_1 = tmp_folder + '/1.csv'
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
	if FirstLine.find("Exam Date") == -1:
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
	fileName_1 = tmp_folder + '/3.csv'
	fileName_2 = tmp_folder + '/4.csv'
	fileName_3 = tmp_folder + '/5.csv'

	with open(fileName_1, "r") as csvFile, open(fileName_2,"w") as tmpFile:
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
			
			Branch = RegNo.find(AdmYear)
			
			Session = row["111Session"]
			if first_time == True:
				first_time = False

				#tmp_slot = Slot
				tmp_paper = Paper

				tmp_date = ExamDate
				ExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
				ExamSession = input("Enter Exam Session :Forenoon? ")

				ExamDate = tmp_date if ExamDate == '' else ExamDate


				#   if  dd of dd/mm/yy is entered make complete dd/mm/yyyy			
				ExamDate = (f'{int(ExamDate):02}') + tmp_date[-8:]  if len(str(ExamDate)) <= 2 else ExamDate

				# if dd/mm is entered, make complete date dd/mm/yyyy
				ExamDate = ExamDate + tmp_date[-5:] if len(str(ExamDate)) == 5 else ExamDate
				NewExamDate = ExamDate
				NewExamSession = ExamSession
				#by default session is FORENOON otherwise 'a' for AFTERNOON and 'f' for FORENOON
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
				#timeTableWriter.writerow({'111Slot':Slot, '111ExamDate':NewExamDate, '111Session':NewExamSession, '111Paper':Paper})
		
			 	#RegNo[RegNo.find(AdmYear)+2:RegNo.find(AdmYear)+4]   
			if tmp_paper != Paper:	  

				#tmp_slot = Slot
				tmp_paper = Paper
				tmp_date = ExamDate

				NewExamDate = str(input("Enter Exam Date for Paper -" + Paper + "[ -" + Slot + "- ]  - " + tmp_date + " - ? "))
				NewExamSession = input("Enter Exam Session :Forenoon? ")

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
					
				#timeTableWriter.writerow({'111Slot':Slot, '111ExamDate':NewExamDate, '111Session':NewExamSession, '111Paper':Paper})

			#FormattedExamDate=ExamDate[-2:] + "/" + ExamDate[3:5] + "/" + ExamDate[:2]			

			writer.writerow({'111Slot':Slot, '111ExamDate':NewExamDate, '111Session':NewExamSession, '111Paper':Paper, '111AdmYear':AdmYear, '111RegNo':RegNo, '111Name':Name})
	#os.system('uniq -c -w 20 ' + fileName_2 + ' >> ' + tmp_folder + '/timeTable.csv')
	os.system('uniq -c -w 20 ' + fileName_2 + '|cut -d"," -f1-4|tr "," "-"  >> ' + tmp_folder + '/timeTable.csv')

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
