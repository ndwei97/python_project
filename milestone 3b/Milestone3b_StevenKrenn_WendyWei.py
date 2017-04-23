# Milestone 2 
# Date: 04/22/2017
# Names: Steven Krenn, Wendy Wei
import re

def main():
	
	find_patents()		


def find_patents():

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
	mapp = dict(zip(intervals,titles))	# link each interval to associate patent title
	# print(mapp)

#=========== Get Keywords =============
	word = 'Pittsburgh' # word of interest to anchor the line index for each key words
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

	print(result)



main();