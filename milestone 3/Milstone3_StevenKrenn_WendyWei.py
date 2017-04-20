# Milestone 2
# Date: 04/16/2017
# Names: Steven Krenn, Wendy Wei
#
import re
import csv
#import operator

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
# <<<<<<< Updated upstream
# 	#print(counts)

	sorted_x = sorted(counts.items(),key=lambda x: x[1], reverse=True)
	# sorted_x = sorted(counts.items(), key=operator.itemgetter(1))

	with open('index.html') as fin, open('index_1.html','w') as fout:
		for line in fin:
			fout.write(line)
			if line == '        <div id="myDropdown" class="dropdown-content">\n':
				next_line = next(fin)
				if next_line == '          <a href="index.html">Home </a>\n':
					for elem in sorted_x:
						fout.write('     <a href="index.html">' + str(elem[0]) + '</a>\n')
					fout.write(next_line)

	# for elem in sorted_x[-30:]:
	# 	print(elem)




main();
