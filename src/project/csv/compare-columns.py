# Compare the values in the first column of a CSV file with the same column in another CSV file
#
# - Find the values that are present in both files
# - Find values that are present in one file but not the other
#
# Uses:
# - sets for comparions

import csv

# Set the file locations for the two CSV files
file1_location = "examples/users.csv"
file1_column_to_read = "email"
file2_location = "examples/users-db.csv"
file2_column_to_read = "Email"

# Compare values from the 2 files and same and differences in values
def compare_columns(col1, col2):
    set1 = set(col1)
    set2 = set(col2)

    same_values = list(set1.intersection(set2))
    only_in_set1 = list(set1.difference(set2))
    only_in_set2 = list(set2.difference(set1))

    return same_values, only_in_set1, only_in_set2

# Read a column from a CSV file and store in a list
def read_column_from_file(file_location, column_to_read):
    col_values = []
    with open(file_location, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # add row's column value and it make a lower case and trim extra whitespace, then append to list
            row_value = row[column_to_read]
            row_value = row_value.lower().strip()
            col_values.append(row_value)
    return col_values

file1_col_values = read_column_from_file(file1_location, file1_column_to_read)
file2_col_values = read_column_from_file(file2_location, file2_column_to_read)

same_values, only_in_set1, only_in_set2 = compare_columns(file1_col_values, file2_col_values)

print("Values in both files:", same_values)
print("##########################################################################")
print("# File 1: " + file1_location)
print("# File 2: " + file2_location)
print("##########################################################################")
print("Values only in file 1:", only_in_set1)
print("##########################################################################")
print("Values only in file 2:", only_in_set2)