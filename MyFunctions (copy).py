#MyFunctions.py
import os
from os import path
import json


def set_fields(data):
	#fix the error of left spaces in "     Course" field
	os.system("sed -i -e '1s: 	Course:Course:g' " + data) 
	os.system("sed -i -e '1s: Course:Course:g' " + data) 


def read_previous_settings():
	with open('settings.json', 'r') as openfile:
		settings = json.load(openfile)
		return settings

def write_settings(settings):
	with open('settings.json', 'w') as outfile:
		json.dump(settings, outfile)

def add_examdate_and_session_if_not_present(tmp_folder):

	fileName = tmp_folder + '/1.csv'
	myfile = open(fileName, "r")
	FirstLine = myfile.readline()
	if FirstLine.find("Exam Date") == -1:
		ReplacementLine = FirstLine.rstrip('\n') + ',Exam Date,Session'
		myfile.close()

		#os.system('echo "' + ReplacementLine + '">' + tmp_folder + '/2.csv')
		os.system('echo "' + ReplacementLine + '">' + tmp_folder + '/2.csv')
		#os.system('echo "$(tail -n +2 ' + fileName + ')" >> ' + tmp_folder + '/2.csv')
		os.system('echo "$(tail -n +2 ' + fileName + ')" >> ' + tmp_folder + '/2.csv')
	else:
		input('\n\n"' +tmp_folder + '/2.csv" ready with field names... \n')
		
		
def sort_on_date(tmp_folder):
	with open(tmp_folder + '/2.csv', "r") as csvFile, open(tmp_folder + '/3.csv',"w") as tmpFile:
		csvReader = csv.DictReader(csvFile)
		writer = csv.DictWriter(tmpFile, fieldnames = ["111Name","111RegNo","111Paper","111Slot","111ExamDate","111Session"]) 
		writer.writeheader()
	    
		for row in csvReader:
			Name,RegNo=row["Student"].replace(")","").split("(")
			Subject,Paper=row["Course"].replace(")","").split("(")
			Slot = row["Slot"]
			
			#ExamDate = row["Exam Date"].right(2) + '/' + row["Exam Date"].
			dd,mm,yy = row["Exam Date"].split('/')
			ExamDate = yy + '/' + mm + '/' + dd
			 
			#Session = row["Session"]
			Session = "FN"
			
			if(ExamDate.strip() == ""):
				ExamDate = "xx/xx/xx"
				Session = "xxx"
			#writer.writerow({'111Name':Name,'111RegNo':RegNo,'111Paper':Paper,'111Slot':Slot,'111ExamDate':ExamDate,'111Session':Session})
		writer.writerow({'111Slot':Slot,'111ExamDate':ExamDate,'111Session':Session,'111Paper':Paper,'111RegNo':RegNo,'111Name':Name})
		    
#sort_key = "-k5,5 -k6,6 -k7,7 -k4,4 -k3,3"    #Slot, Date, Session, Paper, RegNo
sort_key = "-k1,6 "    #Slot, Date, Session, Paper, RegNo
#os.system('sort ' + tmp_folder + '/3.csv' + ' -t "," ' + sort_key + ' > ' + tmp_folder + '/3.csv')
input('sort ' + tmp_folder + '/3.csv' + ' -t "," ' + sort_key + ' > ' + tmp_folder + '/3.csv')


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
