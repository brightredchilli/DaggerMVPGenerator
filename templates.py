from string import Template
import os
import sys

def template(inputFileName):
	root_dir = 'templates'
	try:
		os.mkdir(inputFileName[0].upper() + inputFileName[1:])
	except:
		print("Folder exists, continue")

	for directory, subdirectories, files in os.walk(root_dir):
		for file in files:
			makeFileFromTemplate(inputFileName, directory, file)

def makeFileFromTemplate(inputFileName, directory, file):

	rawTemplate = open(os.path.join(directory, file), 'rb')
	template = Template(rawTemplate.read())
	rawTemplate.close()
	fileName = inputFileName
	upperFileName = fileName[0].upper() + fileName[1:]
	lowerFileName = fileName[0].lower() + fileName[1:]

	filledTemplate = template.substitute(filename=upperFileName, lowercaseFilename=lowerFileName)
	
	newFileName = makeNewFileName(upperFileName, file)

	outputfile = open(newFileName, 'w')
	outputfile.write(filledTemplate)
	outputfile.close()

def makeNewFileName(upperFileName, file):
	basefilename = str(file)

	return upperFileName + "/" + upperFileName + basefilename

if __name__ == "__main__":
	template(sys.argv[1])
