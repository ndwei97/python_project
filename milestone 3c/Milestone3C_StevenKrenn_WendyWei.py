# Milestone 3c
# Date Created: 4/26/17
# Date Last Modified: 4/30/17
# Names: Steven Krenn, Wendy Wei


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


def delete_noise_and_replacemnts():
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
	return replaced_content

def keywords(replaced_content):
	#=========== KEY WORDS ===============
	counts = dict()
	for j in replaced_content:	#  Create a dictionary of keywords assoricated with counts
		counts[j] = counts.get(j, 0) + 1


	sorted_x = sorted(counts.items(),key=lambda x: x[1], reverse=True)	# ordering the key words so the most frequent ones appear first

	return sorted_x


def main():
	# scrape the internet for the list of links
	get_links()
	# get rid of any noise and miss-spellings in the scraped text file
	replaced_content = delete_noise_and_replacemnts()

	# get a sorted dictionary of keywords
	sorted_x = keywords(replaced_content)

	# open the base.html file and create the index.html file
	with open('base.html') as fin, open('index.html','w') as fout:	 	# output  each key word into index.html
		# replace each line in base with index
		for line in fin:
			fout.write(line)
			# find in the file to output all of the keywords to index.html
			# if the link is:
			if line == '        <div id="myDropdown" class="dropdown-content">\n':
				next_line = next(fin)
				# and the next line is:
				if next_line == '          <a href="index.html">Home </a>\n':
					# for every element in sorted_x write a line for each keyword
					for elem in sorted_x:
						fout.write('     <a href="' + str(elem[0]) + '.html">' + str(elem[0]) + '</a>\n')
					# finish writing base.html to index.html
					fout.write(next_line)


# calls the main function
main()
