# Milestone 2
# Date: 04/22/2017
# Names: Steven Krenn, Wendy Wei
import re

def main():

	mapp = get_patent_map()

	search1 = search(mapp, 'cells')

	print(search1, sep='\n\n')
	print('\n\n\n\n\n')

	search2 = search(mapp, 'grain')
	print(search2, sep='\n\n')




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




main();
