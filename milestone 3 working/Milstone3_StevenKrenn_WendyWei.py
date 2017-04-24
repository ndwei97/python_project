# Milestone 3
# Date Created: 04/16/2017
# Date Last Modified: 04/23/2017
# Names: Steven Krenn, Wendy Wei


# This tool allows user to input a txt file and extract keywords out of it and then output it in an html file.
# Before extracting the keywords, this tool first performs text analysis using the delete junk words and substituting miss-spelling words.
# Then it pull out a list of keywords and order them so the most frequent word appears first.
# Finally, this tool output all the keywords into an html file.

# imports re and csv
import re
import csv

# gets the patent information then maps it to a dictionary
# used in the main function to compare indexes to the dictionary
def get_patent_map():

	# so the first section of this function finds the lines
	# where the titles, appl. numbers, and inventors are.
	# it takes those 3 different lists and zips them together

	#========= Get Patent Titiles ==============
	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:	# split patent file content by line break
	    lines = f.read().split("\n")


	word = 'United States Patent Application' # word of interest to anchor the line number for each patent name
	# initialization of the title array
	titles =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
	    if word in line:
	        titles.append(lines[i+3]) # obtain a list of title indexes

	# sets the search file for application numbers
	word = 'Appl. No.:	'
	# initialization of the application number array
	appl_num = []

	for i, line in enumerate(lines):
		if word in line:
			appl_num.append(lines[i])

	# sets the search file for inventors
	word = 'Applicant:	'
	# initialization of the inventor number array
	invent_num = []

	for i, line in enumerate(lines):
		if word in line:
			invent_num.append(lines[i-1])

	# zips all three of the lists together
	allPatentInfo = zip(titles,appl_num,invent_num)

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

	# returns mapp dictionary
	return mapp

# this is the same as the last function, however it only zips the
# three lists together then just returns that 3 dimensionial list
def get_patent_info():
	#========= Get Patent Titiles ==============
	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:
	    lines = f.read().split("\n")

	word = 'United States Patent Application'
	titles =[]

	for i,line in enumerate(lines):
	    if word in line:
	        titles.append(lines[i+3])

	word = 'Appl. No.:	'
	appl_num = []

	for i, line in enumerate(lines):
		if word in line:
			appl_num.append(lines[i])

	word = 'Applicant:	'
	invent_num = []

	for i, line in enumerate(lines):
		if word in line:
			invent_num.append(lines[i-1])

	allPatentInfo = zip(titles,appl_num,invent_num)

	# returns the 3 dimensionial list
	return allPatentInfo

# searches the mapp dictionary for the 'word' and outputs
# the patent data that it finds
def search(mapp, word):

	#=========== Get Keywords =============
	# this is kinda rough, may slow down the code
	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:	# split patent file content by line break
	    lines = f.read().split("\n")

	key_i =[]
		# iterate over lines, and print out line numbers which contain
		# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			key_i.append(i+1)	# obtain a list of keyword indexes

	result = []
	for k in key_i:
	    for m in mapp:
	        if m[0] < k < m[1]:		# find each keyword index in each of the patent intervals
	            result.append(mapp[m])	# obtain a list of patent titles which have keyword included in their content

	result = set(result)

	# returns the list of patents that have the keyword in them
	return result

def get_inventors():

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

	# zips up the word list and the index that the word occured in to a
	# 2 dimensionial list
	inventor_patIndex = zip(word_result, indx_result)

	# returns the 2 dimensionial list
	return inventor_patIndex

# this function is used to take the inventors names
# and make them URL safe.
def urlify(s):

     # remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)

     # replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '-', s)

	 # returns the url safe string
     return s

# this function creates html pages for each inventor
# and lists their associated patent data
# it takes the 2 dimensionial inventor_patIndex
# as an input to the function
def create_inventors_html(inventor_patIndex):

	# get the patent info 3 dimensionial list
	patent_info = get_patent_info()

	# casts the zip object to a list
	patent_info = list(patent_info)

	# for every inventor in the 2d list
	# urlify the text,
	# create/append a new html file for them,
	# write the patent data for each inventor
	for elem,i in inventor_patIndex:
		# make the string url safe
		elem = urlify(str(elem))

		# create/append a new html file for them
		new = open(str(elem) + ".html", 'a')

		# set output to the patent_info 3d list at
		# index of i (which is the second dimension of inventor_patIndex)
		output = patent_info[i]

		# set/initialize the begining loop of each data to 0
		titleHeading = 0

		# for every elem of the output list
		for output_i in output:
			# write a p tag
			new.writelines('<p>')

			# if it's the first time looping the output list
			# make it a heading
			if titleHeading == 0:
				# write a heading tag
				new.writelines('<h3>')
				# write the output list index output_i in string
				new.writelines(str(output_i))
				# write an end heading tag
				new.writelines('</h3>')
			# if it's not the first time looping the output list
			else:
				# just write the output list index
				new.writelines(str(output_i))
			# write an ending p tag
			new.writelines('</p>')
			# accumulate the heading variable
			titleHeading += 1

			# write a new line
			new.writelines('\n')


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

	#=========== KEY WORDS ===============
	counts = dict()
	for j in replaced_content:	#  Create a dictionary of keywords assoricated with counts
		counts[j] = counts.get(j, 0) + 1


	sorted_x = sorted(counts.items(),key=lambda x: x[1], reverse=True)	# ordering the key words so the most frequent ones appear first

	# get the patent dictionary map
	mapp = get_patent_map()

	# open up base.html and open index.html
	# base.html is the base no keyword version of index.html
	# we are injecting the keywords in a loop to index.html
	with open('base.html') as fin, open('index.html','w') as fout:	 	# output  each key word into index.html
		# find and get to the dropdown menu in index.html for the loop
		# to add keywords to.
		for line in fin:
			fout.write(line)
			if line == '        <div id="myDropdown" class="dropdown-content">\n':
				next_line = next(fin)
				if next_line == '          <a href="index.html">Home </a>\n':
					# for every element in the sorted keyword dictionary
					for elem in sorted_x:
						# write a new line in index.html linking the keyword
						fout.write('     <a href="' + str(elem[0]) + '.html">' + str(elem[0]) + '</a>\n')

						# create a new keyword.html file for every elem in sorted_x (the keywords)
						new = open(str(elem[0]) + ".html", 'w')

						# the output of the keyword.html file
						# we make a list out of the ouput from the search function
						# the search function takes the mapp dictionary and a string
						# of the current keyword in the loop
						output = list(search(mapp, str(elem[0])))

						# for every elem in the output list we just searched for
						for output_i in output:
							# write a p tag to the html file
							new.writelines('<p>')

							# initialize/reset the heading flag
							# if it's the first time elem in the list
							# we are going to make it bold and bigger
							# with the h3 html tag
							titleHeading = 0

							# for every elem inside of the output_i list
							for i in output_i:
								# write a p tag in the html file
								new.writelines('<p>')

								# if it's the first time looping this,
								# write the text inside of an h3 tag
								if titleHeading == 0:
									# write the h3 tag to the file
									new.writelines('<h3>')
									# write the string inside of the index i
									# inside of output_i
									new.writelines(str(i))
									# write an ending h3 tag
									new.writelines('</h3>')
								# if it's not the first time looping the list
								# just write it normally
								else:
									# write the list normally
									new.writelines(str(i))
								# write an ending p tag
								new.writelines('</p>')
								# accummulate the titleHeading variable
								titleHeading += 1
							# write a new line character
							new.writelines('\n')
							# write an ending p tag in the html files
							new.writelines('</p>')

					# move to the next line
					fout.write(next_line)


	# get the inventor lists and return it to
	# the inventor_patIndex variable
	inventor_patIndex = get_inventors()

	# use the inventor_patIndex as an input for the creation
	# of the inventor html files
	create_inventors_html(inventor_patIndex)


# calls the main function
main()
