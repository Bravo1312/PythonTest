import re, os, shutil, send2trash

fileRegex = re.compile(r'capitals.*?(_answer)?(\d*)?')

abspathdir = os.path.abspath('.')
path = os.getcwd()
print(path)
for file in os.listdir('.'):
	fileFound = fileRegex.search(file)
	print(fileFound)
	if fileFound == None:
		continue
#	filepath = os.path.join(abspathdir, file)
#	print(filepath)
#	send2trash.send2trash(filepath)
	send2trash.send2trash(file)
		
