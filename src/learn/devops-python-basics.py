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
###################################################

