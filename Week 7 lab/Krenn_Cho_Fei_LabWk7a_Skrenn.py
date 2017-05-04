# Steven Krenn
# Sangmin Cho
# Eric Mingfei
# Date created: 5/2/17
# Data modified: 5/2/17
# gets gallons of gasoline from the user, and converts it
# to liters, barrels, co2, energy, and USD


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
    # gets the number of gallons from the user
    print('Hello! \n')

    # error check for not a number
    while True:
        try:
            # input gasoline gallons
            gallons = float(input('How many gallons of gasoline would you like to convert? \n'))
            break
        except ValueError:
            print('Not a number, try again!')

    print('\n')

    # converts to the 5 different types and prints them to the screen
    print('converted to liters:')
    print(str(convert_to_liters(gallons)) + '\n')
    print('converted to barrels:')
    print(str(convert_to_barrels(gallons)) + '\n')
    print('converted to CO2:')
    print(str(convert_to_CO2(gallons)) + '\n')
    print('converted to energy:')
    print(str(convert_to_energy(gallons)) + '\n')
    print('convert to USD:')
    print(str(convert_to_USD(gallons)) + '\n')


# calls the main function
main()
