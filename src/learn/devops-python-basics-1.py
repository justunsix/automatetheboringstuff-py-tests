# DevOps: Learning Basics of Python
# with https://www.techworld-with-nana.com/devops-bootcamp

##############################################################
# String/number data types, variables, functions, parameters #
##############################################################

# Number of units in a day
# Integer variable, global scope variable
calculation_to_units = 24 * 60 * 60
# String variable
name_of_unit = "seconds"


def days_to_units_20():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")


# Define a new function called days_to_units
# Function parameter is num_of_days, a local scope variable
def days_to_units(num_of_days: object, custom_message: object) -> object:
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


def scope_check(number_of_days):
    my_local_variable = "variable inside function"
    print(my_local_variable)
    print(calculation_to_units)
    print(number_of_days)


# Call functions to see number of seconds in days
days_to_units_20()
days_to_units(20, "Awesome!")
days_to_units(110, "Nice!")

scope_check(54)


#########
# Input #
#########


# Return number of units in days as string
def days_to_units_text(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


# Ask users for input and store user's input in a variable
# The input function always returns a string variable
user_input = input("Input a number of days and I will convert it to seconds\n")
print(user_input)

# To use the user_input as a number
# use casting, call the int function to convert the string to an integer
user_input_number = int(user_input)

calculated_value = days_to_units_text(user_input_number)
print(calculated_value)


###################################################
# Conditionals (if / else) and Boolean Data Type  #
# Input validation                                #
###################################################


# Return number of units in days as string
# Validate input is a positive number
def days_to_units_text_checked(num_of_days):
    # Check if parameter is a positive number
    # assumes num_of_days is an integer data type
    condition_check = num_of_days > 0
    # Print the data type of the condition_check variable
    print(type(condition_check))
    # Conditional to check if parameter is a positive number and evaluates to a boolean
    # true: parameter is a positive number
    # false: parameter is not a positive number
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a 0. Enter a positive number"
    else:
        return "You entered a negative or other data type. Enter a positive number."


# Validate input is an integer
# isdigit() method returns True if all characters in a string are digits
if user_input.isdigit():
    user_input_number = int(user_input)
    checked_calculated_value = days_to_units_text_checked(user_input_number)
    print(checked_calculated_value)
else:
    print("Your input is not a valid number. Enter a positive number.")


##################
# Cleaned up Code


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            checked_calculated_value = days_to_units_text_validated(user_input_number)
            print(checked_calculated_value)
        elif user_input_number == 0:
            print("You entered a 0. Enter a positive number")
    else:
        print("Your input is not a valid number. Enter a positive number.")


# Return number of units in days as string
# Parameter num_of_days must be a postive integer
def days_to_units_text_validated(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


validate_and_execute()


##################################
# Error Handling with Try-Except #
##################################


def validate_and_execute_try_except():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units_text_validated(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0. Enter a positive number")
        else:
            print("You entered a negative number. Enter a positive number.")
    except ValueError:
        print("Error: Your input is not a valid number.")


validate_and_execute_try_except()

###############
# While Loops #
###############

# Prepare user's input variable
# for while loop evaluation
user_input = ""
# Run continously until user inputs exit
while user_input != "exit":
    user_input = input("Enter number of days that this program will convert to hours or type exit to stop\n")
    validate_and_execute_try_except()

#######################
# Lists and For Loops #
#######################
