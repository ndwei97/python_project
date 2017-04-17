# Milestone 2
# Date Created: 04/06/2017
# Date Last Modified: 04/07/2017
# Names: Steven Krenn, Wendy Wei

# Creates and calls three functions.

# find_inventors() opens a txt file that parses and finds inventors from
# that txt file. It then creates a dictionary from the inventors and how many
# applications they have. Then it returns that dictionary back to main.

# getApplicationNumbers() opens a txt file and parses and finds application numbers
# then it returns that list back to main.

# filePrinter() takes both the find_inventors() dictionary, and the getApplicationNumbers() list
# and prints them to the command line, and an output report file

# The main function calls all three of the functions



# imports the re library
import re

def main():
	# calls the find_inventors function and returns a dictionary
	# of the inventors names as the key, and the number of applications as values
	counts = find_inventors()

	# calls the getApplicationNumbers function and returns a list of
	# application numbers
	appl_numbers = getApplicationNumbers()

	# calls filePrinter function, and takes in both the application numbers list
	# and the inventors dictionary for command line and file report outputting
	filePrinter(appl_numbers, counts)


def find_inventors():

	patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read())		# store all 15 patents' contents

	#============= Inventor Names==============
	begining_indexes = []
	ending_indexes =[]
	for m in re.finditer('Inventors:', file_content):	# find all begining indexes of investors' names
		begining_indexes.append(m.end()+1)
	for m in re.finditer('Applicant:', file_content):	# find all ending indexes of investors' names
		ending_indexes.append(m.start()-1)


	inventor_names = []		# store all formated names of inventors from those 15 patents
	for i in range(len(begining_indexes)):
		names = []
		first = begining_indexes[i]
		last = ending_indexes[i]
		names = file_content[first:last]	# find the block of text containing only inventor names from each patent
		names = names.split('; ')

		n = 0
		while n < len(names):	# group each investor's last name, first name, and location together
			inventor_names.append(names[n] + ' ' + names[n+1]+ ' ' + names[n+2])
			n += 3
	# print(inventor_names)

	#============= Application Number ========
	counts = dict()
	for j in inventor_names:	#  Create a dictionary of invertor names assoricated with the number of applications
		counts[j] = counts.get(j, 0) + 1

	patentfile.close()
	return counts

def getApplicationNumbers():
	# opens the txt file for processing
	infile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding="utf-8", errors="ignore")
	# reads the txt file
	file_contents = infile.read()
	# initialization of a application list to return
	fullApplList = []

	# initialization of indexes and a repeat counter
	current_beginning_index = 0
	current_ending_index = 0
	repeat = 0

	# loop this 15 times to get all the application numbers
	while repeat < 15:
		# find "Appl. No.:	" starting from the beginning_index
		# which the first iteration is 0
		beginning_index = file_contents.find("Appl. No.:	", current_beginning_index)
		# add 11 character spaces to offset the "Appl. No.:	" characters
		beginning_index += 11
		# make and ending_index 10 spaces off of the beginning_index
		# because the application number is 10 spaces long
		ending_index = beginning_index + 10

		# initialization of the application number list
		applNumbers = []
		# set application numbers list to the contents from the
		# beginning_index to the ending_index - 1
		# the minus 1 is to not take in to account the \n at the end
		applNumbers = file_contents[beginning_index: ending_index - 1]

		# append the current application number list to a full
		# application number list
		fullApplList.append(applNumbers)

		# update the iteration counters
		current_beginning_index = beginning_index
		current_ending_index = ending_index + 1
		repeat += 1

	# close the file
	infile.close()

	# return the full application numbers list to main
	return fullApplList

def filePrinter(appl_numbers, counts):
	# creates an output file named output.txt
	outfile = open('output.txt', 'w')

	# prints the total number of inventors to the command line
	# and prints to the output.txt file report
	print('Total number of Inventors: ' + str(len(counts)) + '\n')
	outfile.write('Total number of Inventors: ' + str(len(counts)) + '\n' + '\n')

	# prints the application numbers to the command line
	# and prints to the output.txt file report
	print('Application numbers: \n')
	print(*appl_numbers, sep='\n')

	outfile.write('Application numbers: \n')
	for elem in appl_numbers:
		outfile.write(str(elem) + '\n')

	# formatting for both command line
	# and for output.txt file report
	print('\n')
	outfile.write('\n')

	# prints the inventors and their application count to the command line
	# and prints to the output.txt file report
	print('Inventors and how many applications per inventor: \n')
	outfile.write('Inventors and how many applications per inventor: \n')

	for inventor, applications in counts.items():
		print(str(inventor) + ' ' + str(applications))
		outfile.write(str(inventor) + ' ' + str(applications) + '\n')

	# closes the output.txt file
	outfile.close()


# call the main function
main()
