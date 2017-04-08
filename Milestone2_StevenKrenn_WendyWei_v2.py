# Milestone 2 
# Date: 04/07/2017
# Names: Steven Krenn, Wendy Wei
# 
import re

def main():
			
	find_inventors()

def find_inventors():

	begining_indexes = []
	ending_indexes =[]
	patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read())

	for m in re.finditer('Inventors:', file_content):
		begining_indexes.append(m.end()+1)
	for m in re.finditer('Applicant:', file_content):
		ending_indexes.append(m.start()-1)

	
	inventor_names = []
	for i in range(0,15): 
		names = []
		first = begining_indexes[i]
		last = ending_indexes[i]
		names = file_content[first:last]
		names = names.split('; ')
		
		n = 0
		while n < len(names):
			inventor_names.append(names[n] + ' ' + names[n+1]+ ' ' + names[n+2])
			n += 3


main();
