def OpenAndParse():
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

        print(beginning_index)
        print(ending_index)

        names = []

        names = file_contents[beginning_index: ending_index]

        names = names.split(';')

        print(range(len(names)))

        i = 0

        while i < len(names):
            fullname.append(names[i] + names[i + 1] + names[i + 2])
            i += 3

            #print(*fullname, sep='\n')

        # counters
        current_beginning_index = beginning_index
        current_ending_index = ending_index + 1
        repeat += 1

    print(*fullname, sep='\n')

OpenAndParse()
