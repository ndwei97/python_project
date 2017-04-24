# Milestone 3
# Date Created: 04/16/2017
# Date Last Modified: 04/19/2017
# Names: Steven Krenn, Wendy Wei
# This tool allows user to input a txt file and extract keywords out of it and then output it in an html file.
# Before extracting the keywords, this tool first performs text analysis using the delete junk words and substituting miss-spelling words.
# Then it pull out a list of keywords and order them so the most frequent word appears first.
# Finally, this tool output all the keywords into an html file.
import re
import csv

def get_patent_info():
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

	return allPatentInfo

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
	#print(*inventor_patIndex, sep ='\n')

	return inventor_patIndex

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)

     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '-', s)

     return s

def create_investors_html(inventor_patIndex):
	patent_info = get_patent_info()

	patent_info = list(patent_info)

	for elem,i in inventor_patIndex:
		elem = urlify(str(elem))
		#print(elem)

		new = open(str(elem) + ".html", 'a')

		output = patent_info[i]

		titleHeading = 0
		for output_i in output:
			new.writelines('<p>')

			if titleHeading == 0:
				new.writelines('<h3>')
				new.writelines(str(output_i))
				new.writelines('</h3>')
			else:
				new.writelines(str(output_i))
			new.writelines('</p>')
			titleHeading += 1

			new.writelines('\n')
			#new.writelines('</p>')


		#print(patent_info[i-1])
		#print("\n")


def main():

	#========== INPUT FILE =============
	patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read()).lower()		# store all 15 patents' contents
	file_content = re.split('\W+', file_content)	# split the text content and exclude all the special characters.

	#========== DELECT NOISE =============
	noisefile = open('noise_words.txt','r')
	noise_words = str(noisefile.read()).split()

	noiseless_content = []
	for w in file_content:	# find every word in file
		if w.lower() not in noise_words:	# convert each word to lower case and determine if it is noise word.
			noiseless_content.append(w) 	# if the word is not in noise word list, append it to the content list.
	# print(*noiseless_content, sep = '\n')

	#========== WORD REPLACEMENT ===========

	with open('replacements.csv',encoding = "utf-8", errors = "ignore") as csvfile:		# open csv file
		readCSV = csv.reader(csvfile, delimiter =',')	# seperate each column by ','
		old = []
		new = []
		for row in readCSV:
			old.append(row[0])	# convert the first column to a list of words that needs to be changed
			new.append(row[1]) 	# convert the second column to a list of words that needs to be changed into

	replaced_content = str(noiseless_content)
	mapping = dict(zip(old,new))	# create a dictionary with the keys being old words and values being new words
	for k, v in mapping.items():
		replaced_content = replaced_content.replace(k, v)	# replace each old word in file with the new word
	replaced_content = re.split('\W+', replaced_content)
	# print(len(replaced_content))

	#=========== KEY WORDS ===============
	counts = dict()
	for j in replaced_content:	#  Create a dictionary of keywords assoricated with counts
		counts[j] = counts.get(j, 0) + 1


	sorted_x = sorted(counts.items(),key=lambda x: x[1], reverse=True)	# ordering the key words so the most frequent ones appear first
	# sorted_x = sorted(counts.items(), key=operator.itemgetter(1))

	mapp = get_patent_map()


	with open('base.html') as fin, open('index.html','w') as fout:	 	# output  each key word into index.html
		for line in fin:
			fout.write(line)
			if line == '        <div id="myDropdown" class="dropdown-content">\n':
				next_line = next(fin)
				if next_line == '          <a href="index.html">Home </a>\n':
					for elem in sorted_x:
						fout.write('     <a href="' + str(elem[0]) + '.html">' + str(elem[0]) + '</a>\n')
						new = open(str(elem[0]) + ".html", 'w')
						output = list(search(mapp, str(elem[0])))

						for output_i in output:
							new.writelines('<p>')
							titleHeading = 0
							for i in output_i:
								new.writelines('<p>')
								if titleHeading == 0:
									new.writelines('<h3>')
									new.writelines(str(i))
									new.writelines('</h3>')
								else:
									new.writelines(str(i))
								new.writelines('</p>')
								titleHeading += 1

							new.writelines('\n')
							new.writelines('</p>')
					fout.write(next_line)


	inventor_patIndex = get_investors()

	create_investors_html(inventor_patIndex)



main();
