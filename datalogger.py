#Rahul Kanianchalil
#Each folder contains either a .zip file or a .csv/.3gp file
#This script checks what the folder contains and makes the
#naming sequence simplified to make further data analysis easier
import zipfile
import os.path
import os
import errno

def move(dirName, fname):

	try:
		os.mkdir(dirName + "/DataFiles")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	os.rename(dirName + "/" + fname, dirName + "/DataFiles/" + fname)


def unzip(filePath, saveToPath):
	zfile = zipfile.ZipFile(filePath)
	for name in zfile.namelist():
		(dirName, fileName) = os.path.split(name)

#		if not os.path.exists(dirName):
#			print("Running")
#			os.mkdir(dirName)
		try:
			os.mkdir(dirName)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise

		zfile.extract(name, saveToPath)

def main():
	extracted = 0
	sortedFiles = 0
	rootDir = "/home/oem28/Documents/DataDrop"
	for dirName, subdirlist, fileList in os.walk(rootDir):
		for fname in fileList:
			if ".zip" in fname:
				unzip(dirName + "/" + fname, dirName + "/")
				print("DirName: " + dirName)
				print("Fname: " + fname)
				extracted = extracted+ 1
			else:
				move(dirName, fname)
				
	print("Unzipped " + str(extracted) + " file(s)!")
	print("Sorted " + str(sortedFiles) + " file(s)!")

main()

#Future Update/In Free Time:
#Make one method instead of a separate move/unzip method
#Check if directory exists once, if statement to check type
#of file
