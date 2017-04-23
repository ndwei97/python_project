# Milestone 2
# Date: 04/22/2017
# Names: Steven Krenn, Wendy Wei
import re

def main():

	find_patents()


def find_patents():
	# patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', \
	# 							encoding = "utf-8", errors = "ignore")
	# file_content = str(patentfile.read()) # store all 15 patents' contents

	# begining_indexes = []
	# ending_indexes =[]
	# for m in re.finditer('\n'+'Abstract', file_content):	# find all begining indexes of investors' names
	# 	begining_indexes.append(m.end()-11)
	# print(file_content[119:129])

	with open('Milestone2_StevenKrenn_WendyWei.txt','r') as f:
		lines = f.read().split("\n")


	print("Number of lines is {}".format(len(lines)))

	word = 'United States Patent Application' # dummy word. you take it from input
	title =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
		if word in line: # or word in line.split() to search for full words
			# print("Word \"{}\" found in line {}".format(word, i+1))
			# print(str(i-1))
			# print("\n")
			# print(lines[i+3])
			title.append(lines[i+3])

	print(title)

	word = 'Pittsburgh'

	newindexes = []

	for i,line in enumerate(lines):
		if word in line: # or word in line.split() to search for full words
			# print("Word \"{}\" found in line {}".format(word, i+1))
			# print(str(i-1))
			# print("\n")
			# print(lines[i+3])
			newindexes.append(i+1)

	print(newindexes)

	word = '* * * * *'

	starindex = []

	for i,line in enumerate(lines):
		if word in line: # or word in line.split() to search for full words
			# print("Word \"{}\" found in line {}".format(word, i+1))
			# print(str(i-1))
			# print("\n")
			# print(lines[i+3])
			starindex.append(i+1)

	print(starindex)

	starindex.insert(0, 0)

	print(starindex)

	mainchecker = dict(zip(title, starindex))


	mapp = dict()

	for i in range(len(starindex)):
		mapp[starindex[i]] = i

	print(mapp)
	# # mapp = {(0,100): 1, (100,400): 2, (400,800): 3}
	# lst = [3.5, 5.4, 300.12, 500.78, 600.45, 900.546]
	result = []
	for l in newindexes:
	    for m in mapp:
	        if m[0] < l < m[1]:
	            result.append(mapp[m])

	print(result)




main();
