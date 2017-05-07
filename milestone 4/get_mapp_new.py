# we need re library for the new mapp
import re

def get_patent_title():

	with open('output.txt','r') as f:	# split patent file content by line break
		lines = f.read().split("\n")

	word = ' United States Patent Application' # word of interest to anchor the line number for each patent name
	# initialization of the title array
	titles =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			if lines[i+18] != '':
				# print(str(lines[i+17]) + str(lines[i+18]))
				# print()
				titles.append(lines[i+17] + lines[i+18]) # obtain a list of title indexes
			else:
				titles.append(lines[i+17])
				# print(str(lines[i+17]))
				# print()
	return titles
def get_app_num():
	with open('output.txt','r') as f:	# split patent file content by line break
		lines = f.read().split("\n")

	# sets the search file for application numbers
	word = 'Appl. No.:'
	# initialization of the application number array
	appl_num = []

	for i, line in enumerate(lines):
		if word in line:
			#print(lines[i+2])
			appl_num.append(lines[i + 2])
	return appl_num

def get_inventors():
	patentfile = open('output.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read())		# store all 15 patents' contents

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
		names = re.sub('\n', ' ', names).strip()	#get rid of all the white space in the inventor blocks
		names = names.split(';')
		del names[2::3] 	# delete address in name list
		names =[ ''.join(x) for x in zip(names[0::2], names[1::2]) ] 	# join first name and last name into one element
		names = ','.join(names)		# join all inventor names for this patent and seperate them by ','
		inventor_names.append(names)  	# store all formated names of inventors from this patent
	return inventor_names


def get_patent_map_new():

	# so the first section of this function finds the lines
	# where the titles, appl. numbers, and inventors are.
	# it takes those 3 different lists and zips them together
	titles = get_patent_title()
	appl_num = get_app_num()
	inventor_names = get_inventors()
	
	# zips all three of the lists together
	allPatentInfo = zip(titles,appl_num,inventor_names)


	#========== Get Patent Line Number =============
	with open('output.txt','r') as f:	# split patent file content by line break
		lines = f.read().split("\n")

	word = '* * * * *' #  word of interest to anchor the last line of each patent
	patent_i =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			patent_i.append(i+1)	# obtain a list of ending line indexes for each patent

	start = patent_i[:-1] 	# create a list of starting line indexes for each paten
	start.insert(0,0)
	end = patent_i
	intervals = list(zip(start,end))	# create a list of index intervals for each patent
	mapp = dict(zip(intervals,allPatentInfo))	# link each interval to associate patent title

	# returns mapp dictionary
	return mapp



def main():
	new_mapp = get_patent_map_new()

	with open('new_mapp.txt', 'w') as new_f:
		for x in new_mapp:
			new_f.writelines(str(x))
			new_f.writelines('\n')
			for y in new_mapp[x]:
				new_f.writelines(str(y))
			new_f.writelines('\n')

main()
