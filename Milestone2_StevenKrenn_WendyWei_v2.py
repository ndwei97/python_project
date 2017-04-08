# Milestone 2 
# Date: 04/07/2017
# Names: Steven Krenn, Wendy Wei
# 
import re

def main():
	
	find_inventors()		

def find_inventors():


	patentfile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding = "utf-8", errors = "ignore")
	file_content = str(patentfile.read())		# store all 15 patents' contents 

	#============= Inventor Names==============
	begining_indexes = []
	ending_indexes =[]
	for m in re.finditer('Inventors:', file_content):	# find all begining indexes of investors' names
		begining_indexes.append(m.end()+1)
	for m in re.finditer('Applicant:', file_content):	# find all ending indexes of investors' names
		ending_indexes.append(m.start()-1)

	
	inventor_names = []		# store all formated names of inventors from those 15 patents
	for i in range(0,15): 
		names = []
		first = begining_indexes[i]		
		last = ending_indexes[i]
		names = file_content[first:last]	# find the block of text containing only inventor names from each patent
		names = names.split('; ')	
		
		n = 0
		while n < len(names):	# group each investor's last name, first name, and location together
			inventor_names.append(names[n] + ' ' + names[n+1]+ ' ' + names[n+2])
			n += 3
	# print(inventor_names)

	#============= Application Number ========
	counts = dict()
	for j in inventor_names:	#  Create a dictionary of invertor names assoricated with the number of applications 
		counts[j] = counts.get(j, 0) + 1
	print(counts)	

main();
