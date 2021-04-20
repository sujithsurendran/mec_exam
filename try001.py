#try001
from MyFunctions import *



#   Set intial values
ROOMS = (201,210,211,301,309,310,311,312,314,315,409,410,509,510,511)

settings = read_previous_settings()
DataFolderName = input("Data Folder " + settings['DataFolderName'] + "?")
SourceFileName = input("Source File Name " + settings['SourceFileName'] + "?")

settings['DataFolderName'] = DataFolderName if DataFolderName != "" else  settings['DataFolderName']
settings['SourceFileName'] = SourceFileName if SourceFileName != "" else  settings['SourceFileName']


write_settings(settings)	



#get_input_file()	

#set_fields(data)


