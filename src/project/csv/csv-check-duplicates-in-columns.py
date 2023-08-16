import csv
import sys

# Check for duplicates in columns of a CSV file
# Specify the csv file to check and columns separated by a space
# when calling the script

def check_duplicates(csv_file, column_names):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for column_name in column_names:
            if column_name not in header:
                print(f"The column name '{column_name}' does not exist in the CSV file.")
                # Remove the column from the list of columns to check
                column_names.remove(column_name)
        column_values = {column_name: [] for column_name in column_names}
        duplicates = {column_name: [] for column_name in column_names}
        for column_name in column_names:
                line_numbers = []
                line_contents = []
                for i, row in enumerate(reader, start=1):
                    for column_name in column_names:
                        column_value = row[column_name]
                        if column_value in column_values[column_name]:
                            duplicates[column_name].append(column_value)
                            line_numbers.append(i)
                            line_contents.append(row)
                        else:
                            column_values[column_name].append(column_value)
                for column_name in column_names:
                    if duplicates[column_name]:
                        print(f"The following {column_name} values are duplicated: {', '.join(duplicates[column_name])}")
                if line_numbers:
                    print("The following lines contain duplicates:")
                    for i, line_number in enumerate(line_numbers):
                        print(f"Line {line_number}: {line_contents[i]}")
                else:
                    print("No duplicates found in the selected columns.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please provide the path to the CSV file and the column names as arguments.\nExample: python check-user-files.py users.csv email username")
    else:
        csv_file = sys.argv[1]
        column_names = sys.argv[2:]
        check_duplicates(csv_file, column_names)