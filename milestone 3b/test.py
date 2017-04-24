import re
import csv

def get_patent_map():

	#========= Get Patent Titiles ==============
	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:	# split patent file content by line break
	    lines = f.read().split("\n")

	word = 'United States Patent Application' # word of interest to anchor the line number for each patent name
	titles =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
	    if word in line:
	        titles.append(lines[i+3]) # obtain a list of title indexes

	word = 'Appl. No.:	'
	appl_num = []

	for i, line in enumerate(lines):
		if word in line:
			appl_num.append(lines[i])
	#print(appl_num)

	word = 'Applicant:	'
	invent_num = []

	for i, line in enumerate(lines):
		if word in line:
			invent_num.append(lines[i-1])
	#print(invent_num)

	allPatentInfo = zip(titles,appl_num,invent_num)

	#print(*allPatentInfo, sep = '\n\n')

	#========== Get Patent Line Number =============
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

	return mapp

def search(mapp, word):
	#=========== Get Keywords =============
	#word = 'cells' # word of interest to anchor the line index for each key words

	# this is kinda rough, may slow down the code
	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:	# split patent file content by line break

		lines = f.read().split("\n")
		# lines = [s.strip(';') for s in lines]
		# lis = ['sssss;','aaaa;','cccd;']
		# lis = [s.strip(';') for s in lis]
		# print(*lines[:100], sep = '\n')
		# investors = str(lines[8])
		# investors = [s.strip(';') for s in investors]


	key_i =[]
		# iterate over lines, and print out line numbers which contain
		# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			key_i.append(i+1)	# obtain a list of keyword indexes
	# print(key_i)

	result = []
	for k in key_i:
	    for m in mapp:
	        if m[0] < k < m[1]:		# find each keyword index in each of the patent intervals
	            result.append(mapp[m])	# obtain a list of patent titles which have keyword included in their content

	result = set(result)

	#print(*result, sep='\n\n')

	return result


def get_investors():

	patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read())		# store all 15 patents' contents
	file_content = file_content.lower()

	#============= Inventor Names==============
	begining_indexes = []
	ending_indexes =[]
	for m in re.finditer('inventors:', file_content):	# find all begining indexes of investors' names
		begining_indexes.append(m.end()+1)
	for m in re.finditer('applicant:', file_content):	# find all ending indexes of investors' names
		ending_indexes.append(m.start()-1)


	inventor_names = []		# store all formated names of inventors from those 15 patents
	roster = []
	for i in range(len(begining_indexes)):
		names = []
		first = begining_indexes[i]
		last = ending_indexes[i]
		names = file_content[first:last]	# find the block of text containing only inventor names from each patent
		names = names.split('; ')
		del names[2::3] # delete the third element(location) in name list
		names = [i + ' ' + j for i,j in zip(names[::2], names[1::2])] # merge first name and last name into one element in the name list
		inventor_names.append(names)
		roster.extend(names)

	roster = list(set(roster)) # unique list of inventor names
	# print(len(roster))
	# print(*roster, sep ='\n')

	mapp_inv = tuple(enumerate(inventor_names)) # link each list of inventors with application index
	# print(*mapp, sep = '\n')

	indx_result = []
	word_result = []
	mapp_pat = get_patent_map()
	n = 0

	for n in range(len(roster)):
		word = roster[n]
		for i,patent in mapp_inv:
			if word in patent:
				# print(word,i)
				# info = dict.values(mapp_pat)
				word_result.append(word)
				indx_result.append(i)

	inventor_patIndex = zip(word_result, indx_result)
	print(*inventor_patIndex, sep ='\n')


def main():


	get_investors()


main();
