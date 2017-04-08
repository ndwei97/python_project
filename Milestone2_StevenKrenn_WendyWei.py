def openAndParse():
    infile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding="utf-8", errors="ignore")
    file_contents = infile.read()
    fullname = []

    current_beginning_index = 0
    current_ending_index = 0
    repeat = 0

    #####
    while repeat < 15:

        beginning_index = file_contents.find("Inventors:", current_beginning_index)
        beginning_index += 11
        ending_index = file_contents.find("Applicant:", current_ending_index)

        # print(beginning_index)
        # print(ending_index)

        names = []

        names = file_contents[beginning_index: ending_index - 1]

        names = names.split(';')

        # print(range(len(names)))

        formatted_names = []

        for names_i in names:
            if names.index(names_i) != 0:
                if not names.index(names_i) % 3:
                    # print(names_i[1:])
                    formatted_names.append(names_i[1:])
                else:
                    # print(names_i)
                    formatted_names.append(names_i)
            else:
                # print(names_i)
                formatted_names.append(names_i)

        i = 0
        while i < len(formatted_names):
            fullname.append(formatted_names[i] + formatted_names[i + 1] + formatted_names[i + 2])
            i += 3

            #print(*fullname, sep='\n')

        # counters
        current_beginning_index = beginning_index
        current_ending_index = ending_index + 1
        repeat += 1

    print(*fullname, sep='\n')

    print("\n")
    print('Total number of Inventors: ' + str(len(fullname)))

def getApplicationNumbers():
    infile = open('Milestone2_StevenKrenn_WendyWei.txt', 'r', encoding="utf-8", errors="ignore")
    file_contents = infile.read()
    fullApplList = []

    current_beginning_index = 0
    current_ending_index = 0
    repeat = 0

    #####
    while repeat < 15:

        beginning_index = file_contents.find("Appl. No.:	", current_beginning_index)
        beginning_index += 11
        ending_index = beginning_index + 10

        # print(beginning_index)
        # print(ending_index)

        applNumbers = []

        applNumbers = file_contents[beginning_index: ending_index - 1]

        # print(names)
        fullApplList.append(applNumbers)

        # counters
        current_beginning_index = beginning_index
        current_ending_index = ending_index + 1
        repeat += 1

    print(*fullApplList, sep='\n')

getApplicationNumbers()
openAndParse()
