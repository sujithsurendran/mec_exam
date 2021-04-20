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
		#print(settings['DataFolderName'])
		return settings

def write_settings(settings):
	#settings = {"DataFolderName":'aaa',"SourceFileName":'bbb' }
	with open('settings.json', 'w') as outfile:
		json.dump(settings, outfile)

def get_input_file():
	
	#settings = {}
	with open('settings.json', 'r') as openfile:
		settings = json.loads(openfile)
		print(settings)
		
	

	DataFolderName = input("Enter Data folder   :") 	# + settings[1])
	SourceFileName = input("Enter source filename   :")	# + settings[2])


	SourceFileName = DataFolderName + '/' + SourceFileName
	if SourceFileName.strip() == "/":
		SourceFileName = "data.csv"
		
	#write settings to json file	
	"""settings = {
		'SourceFileName': SourceFileName,
		'DataFolderName': DataFolderName
				}
	json_object = json.dumps(settings, indent=4)
	with open('settings.json', 'w') as outfile:
		json.dump(json_object, outfile)
		#outfile.write(settings)



	
	#create tmp folder if not present
	if not path.isdir(DataFolderName.strip() + '/tmp'):
		os.system('mkdir ' +  DataFolderName.strip() + '/tmp')

	"""
	#add Exam Date and Session fields if not present
	"""myfile = open(SourceFileName, "r")
	myline = myfile.readline()
	if myline.find("Exam Date") == -1:
		myline = myline + 'Exam Date, Session'
	myfile.close()
"""
	
	return SourceFileName		


def extract_data_and_name_fields(data):

	with open(data, "r") as csvFile, open("tmp/tmp-001.csv","w") as tmpFile:
		csvReader = csv.DictReader(csvFile)
		writer = csv.DictWriter(tmpFile, fieldnames = ["111Name","111RegNo","111Paper","111Slot","111ExamDate","111Session"]) 
		writer.writeheader()
	    
		for row in csvReader:
			Name,RegNo=row["Student"].replace(")","").split("(")
			Subject,Paper=row["Course"].replace(")","").split("(")
			Slot = row["Slot"]
			
			ExamDate = row["Exam Date"]
			 
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
