# Milestone 3
# Date Created: 04/16/2017
# Date Last Modified: 04/23/2017
# Names: Steven Krenn, Wendy Wei

# Ported from 3B

# The purpose of this tool is to help clients to obtain patent information based on
# keywords and inventor names. For each keyword/inventor will link to an html page
# should list ALL of the patent application name(s), application number(s), and inventor(s)
# that are linked to that keyword/inventor.





# imports the re library
import re
# imports the csv library
import csv
# imports the requests library
import requests
# imports the BeautifulSoup library
from bs4 import BeautifulSoup

# the get_links function scrapes the website using the requests library
# then parses the website to get the 15 important patent links out of it
# then saves all of the text of each patent file to output.txt
def get_links():
	# Scrape the patent website
	r = requests.get('http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.html&r=0&p=1&f=S&l=50&Query=aanm%2F%22carnegie+mellon%22+AND+PD%2F4%2F1%2F2016-%3E6%2F30%2F2016&d=PG01')
	content = r.text
	# creates a beautiful soup object on the scraped website
	soup = BeautifulSoup(content,'html.parser')
	# initialization of a links list
	links = []
	# appends all of the links on the site
	# as a list
	for link in soup.find_all('a'):
		links.append(link.get('href'))

	# initialization of a header string that will be added to
	# all of the patent links
	header = 'http://appft.uspto.gov/'

	# the links list has all of the links in the website in it
	# we only need links to the patents that is links 8 through 39
	links = links[8:39]
	# the links in the list are repeated twice because the scraped website prints
	# the same link for the patent number, and the title
	# so this saves the list as every other object in the list
	# e.g. [1, 1, 2, 2, 3, 3] would be [1, 2, 3]
	links = links[1::2]
	# for every link in the links list
	for link in links:
		# print which link is being processes
		print(links.index(link))
		# create a requests object with the header + the link
		newlink = requests.get(header + link)
		# get the text from the requests object
		content =  newlink.text
		# create a BeautifulSoup object form the content and parse it
		newlinksoup = BeautifulSoup(content,'html.parser')
		# Create or append a text file called output.txt
		fileout = open('output.txt', 'a')
		# write all of the information from the BeautifulSoup object
		# to a text file named 'output.txt'
		fileout.write(newlinksoup.get_text())
		# close the file
		fileout.close()



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


def get_patent_info():

	titles = get_patent_title()
	appl_num = get_app_num()
	inventor_names = get_inventors()

	# zips all three of the lists together
	allPatentInfo = zip(titles,appl_num,inventor_names)
	return allPatentInfo


	# gets the patent information then maps it to a dictionary
	# used in the main function to compare indexes to the dictionary
	# def get_patent_map():

	# so the first section of this function finds the lines
	# where the titles, appl. numbers, and inventors are.
	# it takes those 3 different lists and zips them together

	#========= Get Patent Titiles ==============
	with open('output.txt','r') as f:	# split patent file content by line break
		lines = f.read().split("\n")


	word = 'United States Patent Application' # word of interest to anchor the line number for each patent name
	# initialization of the title array
	titles =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			#print(lines[i+17])
			titles.append(lines[i+17]) # obtain a list of title indexes

	# sets the search file for application numbers
	word = 'Appl. No.:'
	# initialization of the application number array
	appl_num = []

	for i, line in enumerate(lines):
		if word in line:
			#print(lines[i+2])
			appl_num.append(lines[i + 2])


	# sets the end search points for inventors
	word = 'Applicant:'
	# initialization of the inventor number array
	invent_num_ending_index = []

	for i, line in enumerate(lines):
		if word in line:
			#print(i)
			invent_num_ending_index.append(i)



	# sets the search file for inventors
	word = 'Inventors:'
	# initialization of the inventor number array
	invent_num = []

	index_accum = 0
	for i, line in enumerate(lines):
		if word in line:
			#print(lines[i+1:invent_num_ending_index[index_accum]])
			#print()
			inventorlist = lines[i+1:invent_num_ending_index[index_accum]]
			invent_num.append(inventorlist)
			index_accum += 1

	# zips all three of the lists together
	allPatentInfo = zip(titles,appl_num,invent_num)
	#print(allPatentInfo)

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
# def get_patent_info():


# searches the mapp dictionary for the 'word' and outputs
# the patent data that it finds
def search(mapp, word):

	#=========== Get Keywords =============
	# this is kinda rough, may slow down the code
	with open('output.txt','r') as f:	# split patent file content by line break
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
				#print(result.append(mapp[m]))
				#print()
	result = set(result)

	# returns the list of patents that have the keyword in them
	return result

def get_inventors_old():

	patentfile = open('output.txt', 'r', encoding = "utf-8", errors = "ignore")
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
	mapp_pat = get_patent_map_new()
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

	if s[0] == ' ':
		s = s[1:]

	# remove all non-word characters (everything except numbers and letters)
	s = re.sub(r"[^\w\s]", '', s)

	# replace all runs of whitespace with a single dash
	s = re.sub(r"\s+", '-', s)


	if s[0] == '-':
		s = s[1:]
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

	# scrape the internet for the list of links
	get_links()

	inventors_list = get_inventors()

	#========== INPUT FILE =============
	patentfile = open('output.txt', 'r', encoding = "utf-8", errors = "ignore")
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
	mapp = get_patent_map_new()

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
								if titleHeading == 1:
									new.writelines(str(i))
								else:
									# write the list normally
									#new.writelines(str(i))
									for elem in inventors_list:
										splitted_i = str(i).split(',')
										splitted_elem = elem.split(',')
										if splitted_i == splitted_elem:
											for splitted_elem_i in splitted_elem:
												new.write('     <a href="' + urlify(str(splitted_elem_i)) + '.html">' + str(splitted_elem_i) + '</a>\n')

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
	inventor_patIndex = get_inventors_old()

	# use the inventor_patIndex as an input for the creation
	# of the inventor html files
	create_inventors_html(inventor_patIndex)


# calls the main function
main()
