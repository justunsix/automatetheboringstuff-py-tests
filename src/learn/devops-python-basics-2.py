# DevOps: Learning Basics of Python
# with https://www.techworld-with-nana.com/devops-bootcamp

# Variables
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


# Support Functions

# Return number of units in days as string
# Parameter num_of_days must be a postive integer
def days_to_units_text_validated(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # Do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units_text_validated(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0. Enter a positive number")
        else:
            print("You entered a negative number. Enter a positive number.")
    except ValueError:
        print("Error: Your input is not a valid number.")


# Basic list operations
def basic_list_operations():
    # Create
    list_of_months = ["January", "February", "March"]

    # Access items of list, Get first item (January)
    print(list_of_months[0])

    # Add items
    list_of_months.append("April")

    # Remove items
    list_of_months.remove("January")

    # Change items
    list_of_months[0] = "New January"

    print(list_of_months)

#######################
# Lists and For Loops #
#######################

# Allow user to provide a list of values
# Validate all values and return calculation

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days or list of them separated by commas and\n "
                       "this program will convert to hours or type exit to stop\n")
    # user_input is a string and split(,) will provide a list splitting on comma
    # by default can also work on spaces
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
