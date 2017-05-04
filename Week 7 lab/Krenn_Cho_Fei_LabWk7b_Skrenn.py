# Steven Krenn
# Sangmin Cho
# Eric Mingfei
# Date created: 5/2/17
# Data modified: 5/2/17
# gets gallons of gasoline from the user, and converts it
# to liters, barrels, co2, energy, and USD.
# Has a menu function that lets the user pick
# which convertion to apply.


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

# main function
def main():
    # main repeating loop
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
            repeat = str(input("Do you want to have another conversion? Type 'n' for no"))
            # if the user inputs n, then break the while loop
            if repeat == 'n':
                break
        # if the user does not input a valid input gallon number,
        # then run this exception
        except ValueError:
            print("Not a valid number, try again!")

# calls the main function
main()
