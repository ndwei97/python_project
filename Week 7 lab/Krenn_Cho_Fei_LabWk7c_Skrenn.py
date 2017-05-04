# Steven Krenn
# Sangmin Cho
# Eric Mingfei
# Date created: 5/2/17
# Data modified: 5/2/17
# gets gallons of gasoline from the user, and converts it
# to liters, barrels, co2, energy, and USD.
# Has a main menu function that lets the user pick
# if they want to convert 1 at a time, or a list of gas values at once.
# The one value function converts the gasoline one value at a time.
# the list values function converts the gasoline at a
# list of values at one time.


# function to convert to liters
def convert_to_liters(gallon):
    return round(float(gallon) * 3.7854, 3)

# function to convert to barrels
def convert_to_barrels(gallon):
    return round(float(gallon) / 19.5, 3)

# function to convert to CO2
def convert_to_CO2(gallon):
    return round(float(gallon)*20, 3)

# function to convert to energy
def convert_to_energy(gallon):
    energy = float(gallon) * 115000 / 75700
    return round(energy, 2)

# function to convert to USD
def convert_to_USD(gallon):
    return round(float(gallon) * 4, 2)

# a function that converts the gas from a list of values
def list_values():
    # list taking all the input values
    value_list = []
    # input the number of values
    num_input = input("Please enter the number of values to input\n")
    num = 0
    while int(num) < int(num_input):
        try:
            # enter each of the values
            value = input("Enter value " + str(num + 1)+"\n")
            # convert it to float
            float_value = float(value)
            # ignore the negative values
            # add the value to the list
            if float_value > 0:
                num += 1
                value_list.append(value)
            else:
                print("please input a positive number!")
        except:
            print("Not a valid, please re-enter!")

    while True:
        try:

            # print out the menu
            print("1. Number of liters")
            print("2. Number of barrels of oil required to produce the gallons of gasoline specified")
            print("3. Number of pounds of CO2 produced")
            print("4. Equivalent energy amount of ethanol gallons")
            print("5. Price of the gasoline in US dollars")
            # ask the user to choose from the menu
            choice = int(input("Please choose the type of convert\n"))
            # call each of the methods on each of the choices
            if choice == 1:
                print("Results are: ")
                for value in value_list:
                    result = convert_to_liters(value)
                    print(round(result, 4), end=", ")
                    print()
            elif choice == 2:
                print("Results are: ")
                for value in value_list:
                    result = convert_to_barrels(value)
                    print(round(result, 4))
                    print()
            elif choice == 3:
                print("Results are: ")
                for value in value_list:
                    result = convert_to_CO2(value)
                    print(round(result, 4))
                    print()
            elif choice == 4:
                print("Results are: ")
                for value in value_list:
                    result = convert_to_energy(value)
                    print(round(result, 4))
                    print()
            elif choice == 5:
                print("Results are: ")
                for value in value_list:
                    result = convert_to_USD(value)
                    print(round(result, 4))
                    print()
            else:
                print('Not a valid choice!')

            # check to see if the user wants to repeat the calculations
            repeat = str(input("Do you want to have another conversion? Type 'n' for no \n"))
            # if the user inputs n, then break the while loop
            if repeat == 'n':
                break
        except ValueError:
            print("Not a valid option, try again!")

# function that gets user input and does the gas conversion on 1 value
# at a time
def one_value():
        while True:
            # try to do the calculations on valid inputs
            try:
                # gets the gallons of gasoline from the user
                gallons = float(input("Input gallons of gas: "))

                # check to see if the number of gallons is positive
                if gallons < 0:
                    raise ValueError

                # prints the menu to the screen
                print('Chose an option below: \n')
                # gets the user's choice from the menu
                choice = int(input("1. Convert to liters\n2. Convert to barrels\n3. Convert to pounds of C02\n4. Convert to energy amount of ethanol gallons\n5. Convert USD\n"))
                # if the user's choice is 1, then convert to liters
                if choice == 1:
                    print('converted to liters:')
                    print(str(convert_to_liters(gallons)) + '\n')
                # if the user's choice is 2, then convert to barrels
                elif choice == 2:
                    print('converted to barrels:')
                    print(str(convert_to_barrels(gallons)) + '\n')
                # if the user's choice is 3, then convert to CO2
                elif choice == 3:
                    print('converted to CO2:')
                    print(str(convert_to_CO2(gallons)) + '\n')
                # if the user's choice is 4, then convert to energy
                elif choice == 4:
                    print('converted to energy:')
                    print(str(convert_to_energy(gallons)) + '\n')
                # if the user's choice is 5, then convert to USD
                elif choice == 5:
                    print('convert to USD:')
                    print(str(convert_to_USD(gallons)) + '\n')
                # if the user did not choose a valid choice
                else:
                    print("It is not a valid choice!")

                # check to see if the user wants to repeat the calculations
                repeat = str(input("Do you want to have another conversion? Type 'n' for no \n"))
                # if the user inputs n, then break the while loop
                if repeat == 'n':
                    break
            # if the user does not input a valid input gallon number,
            # then run this exception
            except ValueError:
                print("Not a valid number, try again!")

# main function
def main():
    print("Hello! \n")
    # main loop if user does not enter a valid option
    while True:
        # try to have the user enter valid input, if not loop again
        try:
            # main menu question
            print("Would you like to convert one value, or a list of values?")
            # get user's menu reponse
            menu = int(input('1 for 1 value, 2 for list of values \n'))
            # if it's 1 then convert 1 value at a time
            if menu == 1:
                # call the one value function
                one_value()
                # leave the main loop
                break
            # if it's 2 then convert a list of values at a time
            if menu == 2:
                # call the list values function
                list_values()
                # leave the main loop
                break
            # if they didn't choose 1 or 2.
            else:
                print('Not a valid option.')
        # if they entered an option that wasn't a number
        except ValueError:
            print('Not a valid number, try again!')



# calls the main function
main()
