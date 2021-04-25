#try001
from MyFunctions import *



#   Set intial values
ROOMS = (201,210,211,301,309,310,311,312,314,315,409,410,509,510,511)

settings = read_previous_settings()
DataFolderName = input("Data Folder " + settings['DataFolderName'] + "?")
SourceFileName = input("Source File Name " + settings['SourceFileName'] + "?")
ExamName = input("Enter ExamName :" + settings['ExamName'] + "?")


settings['DataFolderName'] = DataFolderName if DataFolderName != "" else  settings['DataFolderName']
settings['SourceFileName'] = SourceFileName if SourceFileName != "" else  settings['SourceFileName']
settings['ExamName'] = SourceFileName if ExamName != "" else  settings['ExamName']

DataFolderName = settings['DataFolderName']
SourceFileName = settings['SourceFileName']
ExamName = settings['ExamName']

write_settings(settings)	
tmp_folder = DataFolderName.strip() + '/tmp_' + ExamName.replace(' ','_')
#create tmp folder if not present
if not path.isdir(tmp_folder):
	os.system('mkdir ' +  tmp_folder)

FileName = DataFolderName + "/" + SourceFileName
working_file_001 = tmp_folder + '/1.csv'

if not path.isfile(working_file_001):
	os.system('cp ' +  FileName + ' ' + working_file_001)
else:
	choice = input("Overwrite " + working_file_001 + ' ?(Y/n)')
	if choice == 'n':
		#Do nothing
		i=0
	else:
		os.system('cp ' +  FileName + ' ' + working_file_001)


set_fields(tmp_folder)

#add_examdate_and_session_if_not_present(tmp_folder)
sort_on_date(tmp_folder)
set_record_date(tmp_folder)
print("Completed...!")

#get_input_file()	



