import os

"""
Description:
	Python 3.8.5 
	The program gets the working directory and uses the walk cmd to display
	the path, directories and filenames of each directory and sub directories in 
	the current working directory
	
os arguments:
	chdir				changes the working directory
	makedir			creates a directory
	rmdir				deletes directory
	makerdirs			creates directory even with sub dirs
	removedirs			deletes directory/sub directories
	listdir			returns a list with the names of the files inside pwd
	rename('<old>','<new>') 	renames the specified file
	stat('<file>').<tag| >		shows file specific information
	walk				recursive returns  a tuple with dirpath, dirnames and filesnames
	path.join(<path>,'file|dir')	creates a path 
Notes:
	use print(dir(os)) to see all available methods within os module
	same with dir(os.path)	
	subprocess module is intended to replace os
"""

#print(dir(os.path))
pwd = os.getcwd()
for dirpath, dirnames, filenames in os.walk(pwd):
	print('Current path:',dirpath)
	print('Directories:',dirnames)
	print('Files:',filenames,'\n')



