# Learning Basics of Python:
# String/number data types, variables, functions, parameters

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