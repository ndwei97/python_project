def get_patent_map_new():

	# so the first section of this function finds the lines
	# where the titles, appl. numbers, and inventors are.
	# it takes those 3 different lists and zips them together

	#========= Get Patent Titiles ==============
	with open('output.txt','r') as f:	# split patent file content by line break
		lines = f.read().split("\n")

	# sets the end search points for inventors
	word = 'Abstract:'
	# initialization of the inventor number array
	invent_num_ending_index = []

	for i, line in enumerate(lines):
		if word in line:
			#print(i)
			invent_num_ending_index.append(i)



	word = ' United States Patent Application' # word of interest to anchor the line number for each patent name
	# initialization of the title array
	titles =[]
	# iterate over lines, and print out line numbers which contain
	# the word of interest.
	for i,line in enumerate(lines):
		if word in line:
			if lines[i+18] != '':
				print(str(lines[i+17]) + str(lines[i+18]))
				print()
				titles.append(lines[i+17] + lines[i+18]) # obtain a list of title indexes
			else:
				titles.append(lines[i+17])
				print(str(lines[i+17]))
				print()
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
	#print(*allPatentInfo)

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

new_mapp = get_patent_map_new()

old_mapp = get_patent_map()

with open('new_mapp.txt', 'w') as new_f:
	for x in new_mapp:
		new_f.writelines(str(x))
		new_f.writelines('\n')
		for y in new_mapp[x]:
			new_f.writelines(str(y))
		new_f.writelines('\n')

with open('old_mapp.txt', 'w') as old_f:
	for x in old_mapp:
		old_f.writelines(str(x))
		old_f.writelines('\n')
		for y in old_mapp[x]:
			old_f.writelines(str(y))
		old_f.writelines('\n')
